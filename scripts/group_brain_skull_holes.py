# ================================================================
# 0. Section: Imports
# ================================================================
import os
import numpy as np
import pandas as pd

from matplotlib import pyplot as plt
from concurrent.futures import ProcessPoolExecutor, as_completed
from tqdm import tqdm

from neuroframe_analysis import (Mouse, get_folders, get_holes,
    plot_group_hole_volume_bar, reduce_brain_segments, plot_regional_hole_volume_bar)



# ================================================================
# 1. Section: Input
# ================================================================
REGION = "cerebellum"



# ================================================================
# 2. Section: Computes Individual Mouse Holes
# ================================================================
def process_global_mouse(mouse_folder_name: str) -> tuple[str, float]:
    # 1. Imports the data
    folder = os.path.join("data", mouse_folder_name)
    mid = os.path.basename(os.path.normpath(folder))
    mouse = Mouse.from_folder(id=mid, folder_path=folder)

    # 2. Extract the data
    brain_mask = mouse.segmentation.volume
    ct = mouse.micro_ct.data
    voxel_size = mouse.voxel_size[0]

    # 3. Get the hole infromation
    holes = get_holes(ct, brain_mask)
    hole_volume_mm = holes.hole_volume(voxel_size)

    return mouse_folder_name, float(hole_volume_mm)

def process_regional_mouse(mouse_folder_name: str) -> tuple[str, float]:
    # 1. Imports the data
    folder = os.path.join("data", mouse_folder_name)
    mid = os.path.basename(os.path.normpath(folder))
    mouse = Mouse.from_folder(id=mid, folder_path=folder)
    annotations_info_df = pd.read_csv("data/annotations_info.csv")

    # 2. Extract the data
    ct = mouse.micro_ct.data
    voxel_size = mouse.voxel_size[0]

    if(REGION.lower() == "isocortex"):
        focus_layer = 6
        segment_id = 315
    elif(REGION.lower() == "cerebellum"):
        focus_layer = 3
        segment_id = 512
    elif(REGION.lower() == "brain stem"):
        focus_layer = 3
        segment_id = 343

    # 3. Extract the simplified segmentation to make a mask
    reduced_brain = reduce_brain_segments(mouse.segmentation.data, annotations_info_df, focus_layer)
    regional_mask = np.where(reduced_brain == segment_id, 1, 0)

    # 3. Get the hole infromation
    regional_holes = get_holes(ct, regional_mask)
    hole_volume_mm = regional_holes.hole_volume(voxel_size)

    return mouse_folder_name, float(hole_volume_mm)



# ================================================================
# 3. Section: MAIN
# ================================================================
if __name__ == "__main__":
    folders = get_folders("data")
    #folders = ['P324']

    holes_volume_store = []
    results = []

    if(REGION.lower() == "global"): target_function = process_global_mouse
    else: target_function = process_regional_mouse

    # Use processes for CPU-bound work
    with ProcessPoolExecutor() as ex:
        futures = [ex.submit(target_function, f) for f in folders]

        for fut in tqdm(as_completed(futures), total=len(futures), desc="Computing holes"):
            folder_name, hole_volume_mm = fut.result()
            results.append((folder_name, hole_volume_mm))
            holes_volume_store.append(hole_volume_mm)

    mean_hole_volume = np.round(np.mean(holes_volume_store), 2)
    std_hole_volume = np.round(np.std(holes_volume_store), 2)
    print(f"\nMean Hole Volume: {mean_hole_volume}mm³ (std: {std_hole_volume}mm³)")

    if(REGION.lower() == "global"): plot_group_hole_volume_bar(holes_volume_store, folders)
    else: plot_regional_hole_volume_bar(holes_volume_store, REGION, folders)

    plt.show()
