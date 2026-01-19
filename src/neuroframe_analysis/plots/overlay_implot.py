# ================================================================
# 0. Section: Imports
# ================================================================
import numpy as np

from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes



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


# ──────────────────────────────────────────────────────
# 1.1 Subsection: Slice helpers (for 3D)
# ──────────────────────────────────────────────────────
def generate_slice(view: int, offset: int, shape: np.ndarray) -> tuple[slice, slice, slice]:
    if view == 0: target_slice = (shape[0] // 2 + offset, slice(None), slice(None))
    elif view == 1: target_slice = (slice(None), shape[1] // 2 + offset, slice(None))
    elif view == 2: target_slice = (slice(None), slice(None), shape[2] // 2 + offset)

    return target_slice
