# ================================================================
# 0. Section: Imports
# ================================================================
import numpy as np

from matplotlib.figure import Figure
from matplotlib.axes import Axes

from ...plots import SaveConfiguration, save_figure_protocol, plot_double_overlay



# ================================================================
# 1. Section: Plots
# ================================================================
@save_figure_protocol
def plot_ct_mri_overlay(mri: np.ndarray, skull: np.ndarray,
    mouse_id: str | None = None,
    offset: int = 0,
    view: int = 0
) -> tuple[Figure, Axes, SaveConfiguration]:
    fig, ax = plot_double_overlay(
        background=mri,
        foreground=skull,
        offset=offset,
        view=view
    )

    return fig, ax, _ct_mri_overlay_config(mouse_id)

def _ct_mri_overlay_config(mouse_id: str | None) -> SaveConfiguration:
    if(mouse_id is None): file_name = "ct_mri_overlay_plot"
    else: file_name = f"{mouse_id}_ct_mri_overlay_plot"

    config = SaveConfiguration(
        file_name=file_name,
        save_type='none'
    )

    return config
