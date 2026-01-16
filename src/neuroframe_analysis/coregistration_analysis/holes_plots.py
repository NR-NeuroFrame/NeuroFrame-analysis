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
def plot_group_hole_volume_bar(hole_volumes: np.ndarray | list, mice_list: np.ndarray | list | None = None) -> tuple:
    nr_data = len(hole_volumes)

    # Define the x labels
    if(mice_list is None):x_pos = np.arange(nr_data)
    else: x_pos = mice_list

    mean_hole_volume = np.mean(hole_volumes)
    std_hole_volume = np.std(hole_volumes)

    fig, ax = plt.subplots()

    # STD Representation
    extended_x_pos = np.arange(-0.5, nr_data + 0.5, 1)
    ax.fill_between(extended_x_pos, mean_hole_volume - std_hole_volume, mean_hole_volume + std_hole_volume,
        alpha=0.3,
        color="NR_GREY",
        edgecolor=None,
        label=f"STD of the Holes Volume: ±{np.round(std_hole_volume, 2)}mm³",
        zorder=1)

    # Mean Representation
    ax.hlines(mean_hole_volume, -0.5, nr_data - 0.5,
        color="NR_GREY",
        label=f"Mean Holes Volume {np.round(mean_hole_volume, 2)}mm³",
        linestyles='--',
        zorder=2)

    # Data Representation
    ax.bar(x_pos, hole_volumes,
        zorder=3)

    ax.set_xlabel("Mice")
    ax.set_ylabel("Holes Volume (mm³)")

    ax.set_title("Study Group Brain-Skull Holes Volume")
    ax.legend()
    fig.tight_layout()
    plt.show(block=False)

    return fig, ax, _hole_volume_plot_config()


# ──────────────────────────────────────────────────────
# 1.1 Subsection: SaveConfig
# ──────────────────────────────────────────────────────
def _hole_volume_plot_config():
    config = SaveConfiguration(
        file_name="group_hole_volume_plot"
    )

    return config
