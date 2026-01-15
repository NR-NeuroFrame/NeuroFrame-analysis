# ================================================================
# 0. Section: Imports
# ================================================================
import numpy as np
from skimage.filters import threshold_otsu

from ..dataclass import Misalignement



# ================================================================
# 1. Section: Obtaining the Mouse Misalignment
# ================================================================
def get_misalignment(ct: np.ndarray, brain_mask: np.ndarray) -> Misalignement:
    # 1. Extract the skull from the ct
    skull_threshold = threshold_otsu(ct[ct>0], 256)
    skull = np.where(ct > skull_threshold, 1, 0)

    # 2. Compute overlap of brain on skull
    overlap = skull * brain_mask
    overlap_count = np.sum(overlap)

    # 3. Compute the maximum possible overlap for % calculation
    max_overlap = np.sum(skull)
    misalignement = Misalignement(overlap_count, max_overlap, overlap_mask=overlap)

    return misalignement
