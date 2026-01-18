# ================================================================
# 0. Section: Imports
# ================================================================
import numpy as np

from dataclasses import dataclass



# ================================================================
# 1. Section: Deatsl for Hole analysis
# ================================================================
@dataclass
class HolesDetails:
    hole_mask: np.ndarray
    nr_voxel_holes: int
    nr_holes: int

    def hole_volume(self, voxel_size: float) -> float:
        return self.nr_voxel_holes * voxel_size**3

    def mean_hole_volume_voxel(self) -> float:
        return self.nr_voxel_holes / self.nr_holes

    def mean_hole_volume_mm3(self, voxel_size: float) -> float:
        return self.mean_hole_volume_voxel() * voxel_size ** 3
