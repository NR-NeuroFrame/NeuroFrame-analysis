# ================================================================
# 0. Section: Imports
# ================================================================
import numpy as np

from scipy.ndimage import center_of_mass



# ================================================================
# 1. Section: Volume Calculations
# ================================================================
def get_volume_center(volume: np.ndarray) -> tuple[int, int, int]:
    center = center_of_mass(volume)

    return tuple(np.round(center).astype(int))



# ================================================================
# 2. Section: Lines and Skulls
# ================================================================
def get_voxels_on_line(starting_point: tuple, end_point: tuple) -> np.ndarray:
    # 1. Format the data
    starting_point = np.asarray(starting_point, dtype=float)
    end_point = np.asarray(end_point, dtype=float)

    # 2. Sample enough points to hit each voxel step
    n = int(np.max(np.abs(end_point - starting_point))) + 1
    t = np.linspace(0.0, 1.0, n)
    pts = starting_point[None, :] + (end_point - starting_point)[None, :] * t[:, None]

    idx = np.rint(pts).astype(int)

    # 3. Remove duplicates caused by rounding
    idx = np.unique(idx, axis=0)

    return idx
