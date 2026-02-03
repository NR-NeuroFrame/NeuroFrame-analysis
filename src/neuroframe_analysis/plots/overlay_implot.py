# ================================================================
# 0. Section: Imports
# ================================================================
import numpy as np

from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes

from .plot_dataclass import Bounds, Viewport

TRIPLE_CMAP_DEFAULT: dict = {"level_0": "gray", "level_1": "nr_red_transparent", "level_2": "nr_blue_transparent"}
TRIPLE_ALPHA_DEFAULT: dict = {"level_0": 1, "level_1": 0.5, "level_2": 1}



# ================================================================
# 1. Section: Simple Overlays
# ================================================================
def plot_double_overlay(
    background: np.ndarray,
    foreground: np.ndarray,
    offset: int = 0,
    view: int = 0,
    background_cmap: str = 'gray',
    foreground_cmap: str = 'nr_red_transparent'
) -> tuple[Figure, Axes]:

    # 1. Generate the plot
    fig, ax = plt.subplots()
    target_slice = generate_slice(view, offset, background.shape)

    # 2. Generate the image plots
    ax.imshow(background[target_slice], cmap=background_cmap)
    ax.imshow(foreground[target_slice], cmap=foreground_cmap)

    # 3. Configure the axis
    plt.axis("off")
    plt.tight_layout()
    plt.show(block=False)

    return fig, ax

def plot_triple_overlay(
    level_0: np.ndarray,
    level_1: np.ndarray,
    level_2: np.ndarray,
    offset: int = 0,
    view: int = 0,
    cmap_dict: dict = TRIPLE_CMAP_DEFAULT,
    alpha_dict: dict = TRIPLE_ALPHA_DEFAULT
) -> tuple[Figure, Axes]:

    # 1. Generate the plot
    fig, ax = plt.subplots()
    target_slice = generate_slice(view, offset, level_0.shape)

    # 2. Generate the image plots
    ax.imshow(level_0[target_slice], cmap=cmap_dict["level_0"], alpha=alpha_dict["level_0"])
    ax.imshow(level_1[target_slice], cmap=cmap_dict["level_1"], alpha=alpha_dict["level_1"])
    ax.imshow(level_2[target_slice], cmap=cmap_dict["level_2"], alpha=alpha_dict["level_2"])

    # 3. Configure the axis
    plt.axis("off")
    plt.tight_layout()
    plt.show(block=False)

    return fig, ax

def plot_triple_overlay_zoom(
    level_0: np.ndarray,
    level_1: np.ndarray,
    level_2: np.ndarray,
    offset: int = 0,
    view: int = 0,
    zoom_roi: Bounds = Bounds(45, 65, 205, 225),
    zoom_viewport: Viewport = Viewport(0.4, 0, 0.5, 0.5),
    cmap_dict: dict = TRIPLE_CMAP_DEFAULT,
    alpha_dict: dict = TRIPLE_ALPHA_DEFAULT
) -> tuple[Figure, Axes]:

    # 1. Start the plot
    fig, ax = plt.subplots()
    target_slice = generate_slice(view, offset, level_0.shape)

    # 2. Apply the slices onto the layers
    slice_0 = level_0[target_slice]
    slice_1 = level_1[target_slice]
    slice_2 = level_2[target_slice]

    # 3. Create the background plot
    ax.imshow(slice_0, cmap=cmap_dict["level_0"], alpha=alpha_dict["level_0"])
    ax.imshow(slice_1, cmap=cmap_dict["level_1"], alpha=alpha_dict["level_1"])
    ax.imshow(slice_2, cmap=cmap_dict["level_2"], alpha=alpha_dict["level_2"])

    # 4. Define the zoom plot parameters
    axins = ax.inset_axes(
        zoom_viewport.as_list(),
        xlim=(zoom_roi.x_start, zoom_roi.x_end), ylim=(zoom_roi.y_start, zoom_roi.y_end),
        xticklabels=[], yticklabels=[])
    axins.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)

    # 5. Format to make the zoom box have white border (even when axis off by default)
    for side in ("left", "right", "top", "bottom"):
        axins.spines[side].set_visible(True)
        axins.spines[side].set_edgecolor("white")
        axins.spines[side].set_linewidth(2)
    ax.indicate_inset_zoom(axins, edgecolor="white")

    # 6. Add the data to the zoom
    axins.imshow(slice_0, cmap=cmap_dict["level_0"])
    axins.imshow(slice_1, cmap=cmap_dict["level_1"], alpha=0.5)
    axins.imshow(slice_2, cmap=cmap_dict["level_2"])

    # 7. Finish the plot
    plt.axis("off")
    plt.tight_layout()
    plt.show(block=False)

    return fig, ax


# ──────────────────────────────────────────────────────
# 1.1 Subsection: Slice helpers (for 3D)
# ──────────────────────────────────────────────────────
def generate_slice(view: int, offset: int, shape: np.ndarray) -> tuple[slice, slice, slice]:
    if view == 0: target_slice = (shape[0] // 2 + offset, slice(None), slice(None))
    elif view == 1: target_slice = (slice(None), shape[1] // 2 + offset, slice(None))
    elif view == 2: target_slice = (slice(None), slice(None), shape[2] // 2 + offset)

    return target_slice
