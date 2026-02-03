from matplotlib import pyplot as plt
from .styling.style_initializer import init_style

from .utils import compress_nifty, get_folders

__all__ = [
    "compress_nifty",
    "get_folders"
]

# Start the Style
init_style()
plt.style.use("src/neuroframe_analysis/styling/nr_style_paper.mplstyle")
