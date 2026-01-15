# ================================================================
# 0. Section: Imports
# ================================================================
import numpy as np
from matplotlib import pyplot as plt



# ================================================================
# 1. Section: Plots
# ================================================================
def plot_group_overlap_bar(overlaps: np.ndarray | list, mice_list: np.ndarray | list | None = None) -> None:
    nr_data = len(overlaps)

    # Define the x labels
    if(mice_list is None):x_pos = np.arange(nr_data)
    else: x_pos = mice_list

    mean_overlap = np.mean(overlaps)
    std_overlap = np.std(overlaps)

    extended_x_pos = np.arange(-0.5, nr_data + 0.5, 1)
    print(extended_x_pos)

    plt.figure()
    plt.bar(x_pos, overlaps)
    plt.hlines(mean_overlap, -0.5, nr_data - 0.5,
        color="NR_DARK_BLUE")
    plt.fill_between(extended_x_pos, mean_overlap - std_overlap, mean_overlap + std_overlap,
        alpha=0.5,
        color="NR_DARK_BLUE",
        edgecolor=None)

    plt.ylim((0,20))
    plt.xlabel("Mice")
    plt.ylabel("Overlap Percentage (%)")

    plt.title("Study Group Brain-Skull Global Overlap")
    plt.tight_layout()
    plt.show(block=False)

    #return fig, ax
