# ================================================================
# 0. Section: Imports
# ================================================================
from dataclasses import dataclass
import numpy as np



# ================================================================
# 1. Section: Storing Misalignment
# ================================================================
@dataclass
class Overlap:
    """Class for keeping track of overlap information"""
    nr_overlap_voxels: int
    nr_maximum_overlap_voxels: int
    overlap_mask: np.ndarray | None = None

    def percentage_overlap(self) -> float:
        return np.round((float(self.nr_overlap_voxels)/float(self.nr_maximum_overlap_voxels))*100, 2)
