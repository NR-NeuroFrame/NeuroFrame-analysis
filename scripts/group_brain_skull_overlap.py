# ================================================================
# 0. Section: Imports
# ================================================================
import os
import numpy as np

from matplotlib import pyplot as plt

from neuroframe_analysis import Mouse, get_overlap, soften_edge, get_folders, plot_group_overlap_bar



# ================================================================
# 1. Section: Computes the Group Misalignment
# ================================================================
folders = get_folders("data")

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
    brain_mask = soften_edge(mouse.segmentation.volume)
    ct = mouse.micro_ct.data
    mri = mouse.mri.data

    # 3. Compute the misalignment
    misalignement = get_overlap(ct, brain_mask, mri)
    misalignment_per_store.append(misalignement.percentage_overlap())
    print(f"{mouse.id} had {misalignement.percentage_overlap()}% misalignment")

# 4. Gets the mean misalignment
mean_misalignment = np.round(np.mean(misalignment_per_store), 2)
std_misalignment = np.round(np.std(misalignment_per_store), 2)
print(f"\nMean overlap: {mean_misalignment}% (std: {std_misalignment}%)")

plot_group_overlap_bar(misalignment_per_store, folders)

plt.show()
