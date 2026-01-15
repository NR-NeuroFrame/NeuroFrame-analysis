# ================================================================
# 0. Section: Imports
# ================================================================
import matplotlib.font_manager as fm
import matplotlib.colors as mcolors

from matplotlib import colormaps

from .graphic_utils import tri_colormap
from .colors import (
    NR_RED,
    NR_LIGHT_RED,
    NR_GREY,
    NR_DARK_BG,
    NR_BLUE,
    NR_DARK_BLUE)



# ================================================================
# 1. Section: Font Initialization
# ================================================================
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
rwy_trimap = tri_colormap('red_white_yellow', NR_RED, "#000000", NR_BLUE)
colormaps.register(rwy_trimap, name="red_white_yellow")
