# ================================================================
# 0. Section: Imports
# ================================================================
from matplotlib import pyplot as plt

from neuroframe_analysis import Mouse, plot_ct_mri_overlay, get_local_skull



# ================================================================
# 1. Section: Input
# ================================================================
MOUSE_ID: str = 'T206'
OFFSET: int = 0
VIEW: int = 0
# 0 - Axial; 1 - Coronal; 2 - Sagittal



# ================================================================
# 2. Section: MAIN
# ================================================================
if __name__ == "__main__":
    folder = "data/" + MOUSE_ID
    mouse = Mouse.from_folder(
        id=MOUSE_ID,
        folder_path=folder
    )

    # 1. Extract the data from the mouse
    mri = mouse.mri.data
    ct = mouse.micro_ct.data
    brain_mask = mouse.segmentation.data
    skull = get_local_skull(ct, brain_mask)

    # 2. Plot
    plot_ct_mri_overlay(mri, skull, MOUSE_ID, OFFSET, VIEW)

    plt.show()
