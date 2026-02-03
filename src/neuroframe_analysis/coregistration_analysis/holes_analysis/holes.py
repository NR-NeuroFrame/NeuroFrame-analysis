# ================================================================
# 0. Section: Imports
# ================================================================
import numpy as np

from scipy.ndimage import distance_transform_edt, label, binary_fill_holes, center_of_mass

from ...logger import logger
from ...utils import get_volume_center, get_voxels_on_line
from ..overlap_analysis.overlap import get_local_skull
from .holes_dataclass import HolesDetails



# ================================================================
# 0. Section: Hole Between Brain and Skull
# ================================================================
def get_holes(ct: np.ndarray, brain_mask: np.ndarray) -> HolesDetails:
    # 1. Get the local skull
    skull = get_local_skull(ct, brain_mask)
    skull = binary_fill_holes(skull)

    # 2. Get the border area mask (skull space)
    skull_space = distance_transform_edt(~skull) <= 5

    # 3. Get all that is not skull, brain and is inside the skull space
    intersection = np.where(skull + brain_mask > 0, 1, 0)
    possible_holes = np.where(skull_space != intersection, 1, 0)

    # 4. Get the connected clusters
    clustered_holes, n = label(possible_holes)
    if n == 0:
        logger.critical("No clusters were found! Cannot get skull space")

    # 5. Remove the excess mask (overshoot) and the holes that do not connect to the center
    clustered_holes = np.where(clustered_holes == 1, 0, clustered_holes)
    holes_mask = filter_for_skull_holes(clustered_holes, brain_mask, skull)
    holes_labels = np.where(holes_mask, clustered_holes, 0)

    # 5. Count them and their size
    hole_voxel_volume = int(np.sum(np.where(holes_mask > 0, 1, 0)))
    nr_labels = len(np.unique(holes_labels))
    return HolesDetails(holes_mask, hole_voxel_volume, nr_labels)


# ──────────────────────────────────────────────────────
# 1.1 Subsection: Hole Filters
# ──────────────────────────────────────────────────────
def filter_for_skull_holes(labels_img: np.ndarray, brain_mask: np.ndarray, skull: np.ndarray) -> np.ndarray:
    brain_center = get_volume_center(brain_mask)

    max_label = labels_img.max()
    if max_label < 2:
        return np.zeros_like(labels_img, dtype=bool)

    # centers for labels 2..max_label in one call
    idx = np.arange(2, max_label + 1)
    # input can be ones; centers are computed per label region
    centers = center_of_mass(np.ones_like(labels_img, dtype=np.uint8), labels=labels_img, index=idx)

    kept = []
    for lab, c in zip(idx, centers):
        if np.isnan(c[0]):  # label absent (can happen)
            continue
        hole_center = tuple(np.rint(c).astype(int))

        line = get_voxels_on_line(hole_center, brain_center)  # see section 3
        if not check_line_intercect_skull(line, skull):
            kept.append(lab)

    # single pass to build final mask
    return np.isin(labels_img, kept)

def check_line_intercect_skull(line: np.ndarray, skull: np.ndarray) -> bool:
    line = np.asarray(line, dtype=int)

    z, y, x = line.T
    hits = skull[z, y, x]

    return np.any(hits)
