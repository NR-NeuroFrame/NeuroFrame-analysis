from matplotlib import pyplot as plt
from .styling import *

from .coregistration_analysis import (
    get_overlap, plot_group_overlap_bar,
    get_holes, plot_group_hole_volume_bar, plot_regional_hole_volume_bar,
    reduce_brain_segments, Overlap, plot_regional_overlap_bar)
from .mouse import Mouse
from .utils import compress_nifty, get_folders

__all__ = ["get_overlap", "get_holes", "plot_group_hole_volume_bar", "plot_regional_hole_volume_bar",
    "Mouse",
    "compress_nifty",
    "get_folders",
    "plot_group_overlap_bar", "plot_regional_overlap_bar",
    "reduce_brain_segments", "Overlap"]

plt.style.use("src/neuroframe_analysis/styling/nr_style_paper.mplstyle")
