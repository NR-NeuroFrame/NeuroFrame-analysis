# ================================================================
# 0. Section: Imports
# ================================================================
import numpy as np
import pandas as pd

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

def reduce_brain_segments(brain_labels: np.ndarray, reference_df: pd.DataFrame, level_of_interest: int) -> np.ndarray:
    reduced_brain = np.zeros_like(brain_labels)
    for i, label in enumerate(np.unique(brain_labels)):
        # Skip background
        if(label == 0): continue

        # Extract parent at level_of_interest
        parent_dir = retrive_segment_family(label, reference_df)
        parent_id = extract_parent(parent_dir, reference_df, level_of_interest)

        # Update reduced_brain
        reduced_brain += np.where(brain_labels == label, parent_id, 0)

    return reduced_brain

def retrive_segment_family(segment_id: int, reference_df: pd.DataFrame) -> np.ndarray:
    segment_dir = [segment_id]
    while not np.isnan(segment_id):
        segment_row = reference_df[reference_df['id'] == segment_id]
        parent_segment = segment_row['parent_id'].values

        if(isinstance(parent_segment, np.ndarray) or isinstance(parent_segment, list) and len(parent_segment) > 0): parent_segment = parent_segment[0]
        else: parent_segment = np.nan

        if(not np.isnan(parent_segment)): segment_dir += [parent_segment]

        segment_id = parent_segment
    segment_dir = np.array(segment_dir, dtype=int)

    return segment_dir

def extract_parent(parent_dir: np.ndarray, reference_df: pd.DataFrame, position: int) -> int:
    if(len(parent_dir) > position): parent_id = parent_dir[-position] # Normal Condition
    elif (len(parent_dir) > 1): parent_id = parent_dir[1]             # Short array condition
    else: parent_id = parent_dir[0]                                   # The segment is the root (or at root level)
    return parent_id
