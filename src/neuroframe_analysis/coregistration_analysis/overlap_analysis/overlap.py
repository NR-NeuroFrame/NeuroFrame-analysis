# ================================================================
# 0. Section: Imports
# ================================================================
import numpy as np

from skimage.filters import threshold_otsu
from scipy.ndimage import distance_transform_edt

from ..brain_mask import soften_edge

from .overlap_dataclass import Overlap



# ================================================================
# 1. Section: Obtaining the Mouse Misalignment
# ================================================================
def get_overlap(ct: np.ndarray, brain_mask: np.ndarray) -> Overlap:
    # 1. Extract the skull from the ct
    skull = get_local_skull(ct, brain_mask)

    # 2. Softens the border between the brain and the skull
    brain_mask = soften_edge(brain_mask)

    # 3. Compute overlap of brain on skull
    overlap = skull * brain_mask
    overlap_count = np.sum(overlap)

    # 4. Compute the maximum possible overlap for % calculation
    max_overlap = np.sum(skull)
    misalignement = Overlap(overlap_count, max_overlap, overlap_mask=overlap)

    return misalignement

def get_local_skull(ct: np.ndarray, brain_mask: np.ndarray) -> np.ndarray:
    # 1. Extract all the skull present in the CT
    skull_threshold = threshold_otsu(ct[ct>0], 256)
    global_skull = np.where(ct > skull_threshold, 1, 0)

    # 2. Get only the skull that surrounds the brain
    brain_mask = np.asanyarray(brain_mask, dtype=bool)
    skull_mask = distance_transform_edt(~brain_mask) <= 10

    # 3. Get local skull
    local_skull = skull_mask * global_skull

    return local_skull
