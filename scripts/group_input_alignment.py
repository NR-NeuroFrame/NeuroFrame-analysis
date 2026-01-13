# ================================================================
# 0. Section: Imports
# ================================================================
import numpy as np

from typing import cast
from nibabel.nifti1 import Nifti1Image
from nibabel.loadsave import load as niload
from matplotlib import pyplot as plt

from neuroframe_analysis import get_misalignment


print("Starting the Script")

mri_path = "tests/integration/fixtures/test_experiment/test_mouse_p324/p324_mri.nii.gz"
ct_path = "tests/integration/fixtures/test_experiment/test_mouse_p324/p324_uCT.nii.gz"
seg_path = "tests/integration/fixtures/test_experiment/test_mouse_p324/p324_seg.nii.gz"

mri = cast(Nifti1Image, niload(mri_path)).get_fdata(dtype=np.float32)
ct = cast(Nifti1Image, niload(ct_path)).get_fdata(dtype=np.float32)
seg = cast(Nifti1Image, niload(seg_path)).get_fdata(dtype=np.float32)

brain_mask = np.where(seg > 0, 1, 0)

misalignement = get_misalignment(ct, mri, brain_mask)
print(misalignement.percentage_overlap(), "%")
plt.show()
