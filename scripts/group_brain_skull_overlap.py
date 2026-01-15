# ================================================================
# 0. Section: Imports
# ================================================================
import os
import numpy as np

from matplotlib import pyplot as plt

from neuroframe_analysis import Mouse, get_overlap, get_folders, plot_group_overlap_bar



# ================================================================
# 1. Section: Computes the Group Misalignment
# ================================================================
folders = get_folders("data")

overlap_per_store = []
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

    # 3. Compute the misalignment
    overlap_data = get_overlap(ct, brain_mask)
    overlap_per_store.append(overlap_data.percentage_overlap())
    print(f"{mouse.id} had {overlap_data.percentage_overlap()}% misalignment")

# 4. Gets the mean misalignment
mean_overlap = np.round(np.mean(overlap_per_store), 2)
std_overlap = np.round(np.std(overlap_per_store), 2)
print(f"\nMean overlap: {mean_overlap}% (std: {std_overlap}%)")

plot_group_overlap_bar(overlap_per_store, folders)

plt.show()
