# ================================================================
# 0. Section: Imports
# ================================================================
import numpy as np

from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes



# ================================================================
# 1. Section: One Metric Plot
# ================================================================
def plot_group_vs_one_metric_bar(data: np.ndarray,
    metric_name: str,
    metric_type: str = '%',
    ylim: tuple | None = None,
    group_names: np.ndarray | None = None) -> tuple[Figure, Axes]:

    # 1. Exttract statistics
    len_data = len(data)
    mean_data = np.mean(data)
    std_data = np.std(data)

    # 2. Define the X labels
    if(group_names is None): x_pos = np.arange(len_data)
    else: x_pos = group_names

    # 3. Initializes the plot
    fig, ax = plt.subplots()

    # 4. STD Representation
    extended_x_pos = np.arange(-0.5, len_data + 0.5, 1)
    ax.fill_between(extended_x_pos, mean_data - std_data, mean_data + std_data,
        alpha=0.3,
        color="NR_GREY",
        edgecolor=None,
        label=f"STD {metric_name}: ±{np.round(std_data, 2)}{metric_type}",
        zorder=1)

    # 5. Mean Representation
    ax.hlines(mean_data, -0.5, len_data - 0.5,
        color="NR_GREY",
        label=f"Mean {metric_name} {np.round(mean_data, 2)}{metric_type}",
        linestyles='--',
        zorder=2)

    # 6. Data Representation
    ax.bar(x_pos, data,
        zorder=3)

    # 7. Label and Titles Organization
    ax.legend()
    ax.set_xlabel("Mice")
    ax.set_ylabel(f"{metric_name} ({metric_type})")
    if(ylim is not None):
        ax.set_ylim(ylim)
    ax.set_title(f"Study Group Brain-Skull {metric_name}")

    # 8. Finishing it
    fig.tight_layout()
    plt.show(block=False)

    return fig, ax
