from matplotlib import pyplot as plt
from .styling import *

from .coregistration_analysis import get_misalignment, plot_group_overlap_bar
from .mouse import Mouse
from .utils import compress_nifty, get_folders
from .brain_mask import soften_edge

__all__ = ["get_misalignment", "soften_edge",
    "Mouse",
    "compress_nifty",
    "get_folders",
    "plot_group_overlap_bar"]

plt.style.use("src/neuroframe_analysis/styling/nr_style_paper.mplstyle")
