# ================================================================
# 0. Section: Imports
# ================================================================
import numpy as np

from ...plots import save_figure_protocol, SaveConfiguration, plot_group_vs_one_metric_bar



# ================================================================
# 1. Section: Plots
# ================================================================
@save_figure_protocol
def plot_group_overlap_bar(overlaps: np.ndarray | list, mice_list: np.ndarray | list | None = None) -> tuple:
    fig, ax = plot_group_vs_one_metric_bar(
        data=overlaps,
        metric_name="Global Overlap",
        metric_type="%",
        group_names=mice_list)

    return fig, ax, _global_overlap_plot_config()

@save_figure_protocol
def plot_regional_overlap_bar(overlaps: np.ndarray | list, region: str, mice_list: np.ndarray | list | None = None) -> tuple:
    fig, ax = plot_group_vs_one_metric_bar(
        data=overlaps,
        metric_name=f"{region.title()} Overlap",
        metric_type="%",
        group_names=mice_list)

    config = _regional_overlap_plot_config(region.lower())

    return fig, ax, config


# ──────────────────────────────────────────────────────
# 1.1 Subsection: SaveConfig
# ──────────────────────────────────────────────────────
def _global_overlap_plot_config():
    config = SaveConfiguration(
        file_name="group_overlap_plot",
        save_type="none",
    )

    return config

def _regional_overlap_plot_config(region: str):
    config = SaveConfiguration(
        file_name=f"{region}_overlap_plot",
        save_type="none"
    )

    return config
