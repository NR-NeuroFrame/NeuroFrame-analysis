# ================================================================
# 0. Section: Imports
# ================================================================
import matplotlib.font_manager as fm
import matplotlib.colors as mcolors

from matplotlib import colormaps

from .colormaps import alpha_red_cmap_256, nr_cmap, alpha_blue_cmap_256
from .colors import (
    NR_RED,
    NR_LIGHT_RED,
    NR_GREY,
    NR_DARK_BG,
    NR_BLUE,
    NR_DARK_BLUE
)



# ================================================================
# 1. Section: Font Initialization
# ================================================================
def init_font() -> None:
    fm.fontManager.addfont("src/neuroframe_analysis/styling/Diagramm/TTF/Diagramm-Light.ttf")
    fm.fontManager.addfont("src/neuroframe_analysis/styling/Diagramm/TTF/Diagramm-Regular.ttf")
    fm.fontManager.addfont("src/neuroframe_analysis/styling/Diagramm/TTF/Diagramm-Bold.ttf")

    # Find the actual family name Matplotlib sees
    for f in fm.fontManager.ttflist:
        if "Diagramm" in f.name:
            pass
            # print(f"Font Loaded: {f.name}, {f.weight}")   # run once to inspect



# ================================================================
# 2. Section: Color Initialization
# ================================================================
def init_colors() -> None:
    NR_COLORS = {
        "NR_RED": NR_RED,
        "NR_LIGHT_RED": NR_LIGHT_RED,
        "NR_GREY": NR_GREY,
        "NR_DARK_BG": NR_DARK_BG,
        "NR_BLUE": NR_BLUE,
        "NR_DARK_BLUE": NR_DARK_BLUE,
    }
    mcolors.get_named_colors_mapping().update(NR_COLORS)


# ================================================================
# 3. Section: Colormaps Initialization
# ================================================================
def init_colormaps() -> None:
    colormaps.register(nr_cmap, name="nr_cmap")
    colormaps.register(alpha_red_cmap_256, name="nr_red_transparent")
    colormaps.register(alpha_blue_cmap_256, name="nr_blue_transparent")


def init_style():
    init_font()
    init_colors()
    init_colormaps()
