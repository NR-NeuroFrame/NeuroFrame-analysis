# ================================================================
# 0. Section: Imports
# ================================================================
import numpy as np

from scipy.signal import fftconvolve
from ..utils import gaussian_kernel_3d



# ================================================================
# 1. Section: Edge Handling
# ================================================================
def soften_edge(mask: np.ndarray, k_size: int = 9, k_sigma: float = 9.0) -> np.ndarray:
    # 1. Initiate the data and the kernel
    original_mask = mask.astype(np.float32)
    kernel = gaussian_kernel_3d(size=k_size, sigma=k_sigma)

    # 2. Blur the mask
    blured_mask = fftconvolve(original_mask, kernel, mode="same")

    # 3. Save only the inner blurred mask
    out_mask = original_mask * blured_mask

    return out_mask
