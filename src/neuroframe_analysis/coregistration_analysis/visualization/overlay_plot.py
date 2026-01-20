# ================================================================
# 0. Section: Imports
# ================================================================
import numpy as np

from matplotlib.figure import Figure
from matplotlib.axes import Axes

from ...plots import(
    SaveConfiguration, save_figure_protocol, plot_double_overlay, plot_triple_overlay, plot_triple_overlay_zoom
)

from ...plots.plot_dataclass import Bounds



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

@save_figure_protocol
def plot_ct_mri_effect_overlay(mri: np.ndarray, skull: np.ndarray, effect_data: np.ndarray,
    effect_name: str = "hole",
    mouse_id: str | None = None,
    offset: int = 0,
    view: int = 0
) -> tuple[Figure, Axes, SaveConfiguration]:
    fig, ax = plot_triple_overlay(
        level_0=mri,
        level_1=skull,
        level_2=effect_data,
        offset=offset,
        view=view
    )

    return fig, ax, _ct_mri_effect_overlay_config(effect_name, mouse_id)

@save_figure_protocol
def plot_ct_mri_effect_overlay_zoom(mri: np.ndarray, skull: np.ndarray, effect_data:np.ndarray,
    effect_name: str = "hole",
    mouse_id: str | None = None,
    offset: int = 0,
    view: int = 0,
    zoom_roi: Bounds = Bounds(45, 65, 205, 225),

) -> tuple[Figure, Axes, SaveConfiguration]:
    fig, ax = plot_triple_overlay_zoom(
        level_0=mri,
        level_1=skull,
        level_2=effect_data,
        offset=offset,
        view=view,
        zoom_roi=zoom_roi
    )

    effect_name = effect_name + "_zoom"

    return fig, ax, _ct_mri_effect_overlay_config(effect_name, mouse_id)

# ──────────────────────────────────────────────────────
# 1.1 Subsection: SaveConfig
# ──────────────────────────────────────────────────────
def _ct_mri_overlay_config(mouse_id: str | None) -> SaveConfiguration:
    if(mouse_id is None): file_name = "ct_mri_overlay_plot"
    else: file_name = f"{mouse_id.lower()}_ct_mri_overlay_plot"

    config = SaveConfiguration(
        file_name=file_name,
        save_type='none'
    )

    return config

def _ct_mri_effect_overlay_config(effect: str, mouse_id: str | None = None) -> SaveConfiguration:
    if(mouse_id is None): file_name = f"ct_mri_{effect.lower()}_overlay_plot"
    else: file_name = f"{mouse_id.lower()}_ct_mri_{effect.lower()}_overlay_plot"

    config = SaveConfiguration(
        file_name=file_name,
    )

    return config
