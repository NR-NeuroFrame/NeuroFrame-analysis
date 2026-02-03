# ================================================================
# 0. Section: Imports
# ================================================================
import numpy as np



# ================================================================
# 1. Section: Normalization Based Functions
# ================================================================
def normalize(volume:np.ndarray) -> np.ndarray:
    # Obtain the minimum and maximum values of the data
	min_val = np.min(volume)
	max_val = np.max(volume)

    # Normalize the data to the range [0, 1]
	data_normalized = ((volume - min_val) / (max_val - min_val)) * 255

	return data_normalized.astype(np.int16)



# ================================================================
# 2. Section: Convolution Based Functions
# ================================================================
def gaussian_kernel_3d(size=9, sigma=2.0) -> np.ndarray:
    assert size % 2 == 1, "size must be odd"

    r = size // 2
    ax = np.arange(-r, r + 1, dtype=np.float32)
    xx, yy, zz = np.meshgrid(ax, ax, ax, indexing="ij")
    k = np.exp(-(xx**2 + yy**2 + zz**2) / (2 * sigma**2))
    k /= k.sum()
    return k
