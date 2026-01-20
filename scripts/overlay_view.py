# ================================================================
# 0. Section: Imports
# ================================================================
from matplotlib import pyplot as plt

from neuroframe_analysis import (
    Mouse, plot_ct_mri_overlay, get_local_skull, get_holes,
    get_overlap, plot_ct_mri_effect_overlay_zoom
)

from neuroframe_analysis.plots.plot_dataclass import Bounds



# ================================================================
# 1. Section: Input
# ================================================================
MOUSE_ID: str = 'T206'
OFFSET: int = 50
VIEW: int = 0 # 0 - Axial; 1 - Coronal; 2 - Sagittal
HOLE_BOUNDS = Bounds(143, 163, 91, 111)



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

    # 2. Mask creation
    holes = get_holes(ct, brain_mask)
    holes_mask = holes.hole_mask

    overlap = get_overlap(ct, brain_mask)
    overlap_mask = overlap.overlap_mask

    # 3. Plot
    plot_ct_mri_effect_overlay_zoom(mri, skull, overlap_mask, 'overlap', MOUSE_ID, OFFSET, VIEW)
    plot_ct_mri_effect_overlay_zoom(mri, skull, holes_mask, 'hole', MOUSE_ID, OFFSET, VIEW, HOLE_BOUNDS)
    plot_ct_mri_overlay(mri, skull, MOUSE_ID, OFFSET, VIEW)

    plt.show()
