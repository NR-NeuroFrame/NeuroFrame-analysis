# ================================================================
# 0. Section: Imports
# ================================================================
import os
import numpy as np
import pandas as pd

from matplotlib import pyplot as plt

from neuroframe_analysis import get_folders
from neuroframe_analysis.mouse import Mouse
from neuroframe_analysis.coregistration_analysis import (
    Overlap,
    get_overlap,
    reduce_brain_segments,
    plot_group_overlap_bar,
    plot_regional_overlap_bar
)



# ================================================================
# 1. Section: Inputs
# ================================================================
REGION = "global"



# ================================================================
# 2. Section: Computes the Group Overlap
# ================================================================
def process_global_mouse(path: str) -> Overlap:
    # 1. Starts the mouse
    folder = "data/" + path
    id = os.path.basename(os.path.normpath(folder))
    mouse = Mouse.from_folder(
        id=id,
        folder_path=folder
    )

    # 2. Extract the data
    brain_mask = mouse.segmentation.volume
    ct = mouse.micro_ct.data

    # 3. Compute the overlap
    overlap_data = get_overlap(ct, brain_mask)
    return overlap_data

def process_regional_mouse(path: str, target: str = "isocortex") -> tuple[Overlap, Overlap]:
    # 1. Starts the mouse
    folder = "data/" + path
    annotations_info_df = pd.read_csv("data/annotations_info.csv")
    id = os.path.basename(os.path.normpath(folder))
    mouse = Mouse.from_folder(
        id=id,
        folder_path=folder
    )

    # 2. Extract the data
    ct = mouse.micro_ct.data

    if(target.lower() == "isocortex"):
        focus_layer = 6
        segment_id = 315
    elif(target.lower() == "cerebellum"):
        focus_layer = 3
        segment_id = 512
    elif(target.lower() == "brain stem"):
        focus_layer = 3
        segment_id = 343

    # 3. Extract the simplified segmentation to make a mask
    # for cortex, cerebellum and brain stem
    reduced_brain = reduce_brain_segments(mouse.segmentation.data, annotations_info_df, focus_layer)
    regional_mask = np.where(reduced_brain == segment_id, 1, 0)

    # 4. Compute the overlap
    isocortex_overlap_data = get_overlap(ct, regional_mask)
    return isocortex_overlap_data




# ================================================================
# 3. Section: MAIN
# ================================================================
if __name__ == "__main__":
    folders = get_folders("data")
    folders = ["P324"]
    overlap_per_store = []

    # 1. Iterates for all mice
    for folder in folders:
        if(REGION.lower() == "global"):overlap_data = process_global_mouse(folder)
        else:overlap_data = process_regional_mouse(folder, REGION)

        overlap_per_store.append(overlap_data.percentage_overlap())
        print(f"{REGION.title()} {folder} Overlap: {overlap_data.percentage_overlap()}%")

    # 2. Gets the mean overlap
    mean_overlap = np.round(np.mean(overlap_per_store), 2)
    std_overlap = np.round(np.std(overlap_per_store), 2)
    print(f"\nMean overlap: {mean_overlap}% (std: {std_overlap}%)")

    if(REGION.lower() == "global"):plot_group_overlap_bar(overlap_per_store, folders)
    else: plot_regional_overlap_bar(overlap_per_store, REGION, folders)

    plt.show()
