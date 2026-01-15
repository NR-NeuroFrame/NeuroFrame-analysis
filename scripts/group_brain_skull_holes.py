# ================================================================
# 0. Section: Imports
# ================================================================
import os

from neuroframe_analysis import Mouse, get_folders, get_holes



# ================================================================
# 1. Section: Computes the Group Misalignment
# ================================================================
folders = get_folders("data")
folders = ['P324']

misalignment_per_store = []
for folder in folders:
    # 1. Starts the mouse
    folder = "data/" + folder
    id = os.path.basename(os.path.normpath(folder))
    mouse = Mouse.from_folder(
        id=id,
        folder_path=folder
    )

    # 2. Extract the data
    brain_mask = mouse.segmentation.volume
    ct = mouse.micro_ct.data

    get_holes(ct, brain_mask)
