# ================================================================
# 0. Section: Imports
# ================================================================
import numpy as np
from matplotlib import pyplot as plt

from ..plots import save_figure_protocol, SaveConfiguration



# ================================================================
# 1. Section: Plots
# ================================================================
@save_figure_protocol
def plot_group_overlap_bar(overlaps: np.ndarray | list, mice_list: np.ndarray | list | None = None) -> tuple:
    nr_data = len(overlaps)

    # Define the x labels
    if(mice_list is None):x_pos = np.arange(nr_data)
    else: x_pos = mice_list

    mean_overlap = np.mean(overlaps)
    std_overlap = np.std(overlaps)


    fig, ax = plt.subplots()

    # STD Representation
    extended_x_pos = np.arange(-0.5, nr_data + 0.5, 1)
    ax.fill_between(extended_x_pos, mean_overlap - std_overlap, mean_overlap + std_overlap,
        alpha=0.3,
        color="NR_GREY",
        edgecolor=None,
        label=f"STD of the Overlap: ±{np.round(std_overlap, 2)}%",
        zorder=1)

    # Mean Representation
    ax.hlines(mean_overlap, -0.5, nr_data - 0.5,
        color="NR_GREY",
        label=f"Mean Overlap {np.round(mean_overlap, 2)}%",
        linestyles='--',
        zorder=2)

    # Data Representation
    ax.bar(x_pos, overlaps,
        zorder=3)

    ax.set_ylim((0,25))
    ax.set_xlabel("Mice")
    ax.set_ylabel("Overlap Percentage (%)")

    ax.set_title("Study Group Brain-Skull Global Overlap")
    ax.legend()
    fig.tight_layout()
    plt.show(block=False)

    return fig, ax, _overlap_plot_config()


# ──────────────────────────────────────────────────────
# 1.1 Subsection: SaveConfig
# ──────────────────────────────────────────────────────
def _overlap_plot_config():
    config = SaveConfiguration(
        file_name="group_overlap_plot"
    )

    return config
