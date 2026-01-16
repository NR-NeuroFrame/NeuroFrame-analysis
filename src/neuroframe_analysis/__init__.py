from matplotlib import pyplot as plt
from .styling import *

from .coregistration_analysis import get_overlap, plot_group_overlap_bar, get_holes, plot_group_hole_volume_bar
from .mouse import Mouse
from .utils import compress_nifty, get_folders

__all__ = ["get_overlap", "get_holes", "plot_group_hole_volume_bar",
    "Mouse",
    "compress_nifty",
    "get_folders",
    "plot_group_overlap_bar"]

plt.style.use("src/neuroframe_analysis/styling/nr_style_paper.mplstyle")
