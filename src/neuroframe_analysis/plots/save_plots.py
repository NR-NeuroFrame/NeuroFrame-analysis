# ================================================================
# 0. Section: Imports
# ================================================================
from pathlib import Path
from matplotlib.figure import Figure
from matplotlib.axes import Axes

from .save_dataclass import SaveConfiguration



# ================================================================
# 1. Section: Saving a Plot
# ================================================================
def save_plot(fig: Figure, ax: Axes, save_config: SaveConfiguration) -> None:
    # Gets the output folder
    output_path = save_config.output_path

    # Creates one for each type of file
    main_folder = Path(output_path) / 'main'
    edit_folder = Path(output_path) / 'edit'
    main_folder.mkdir(parents=True, exist_ok=True)
    edit_folder.mkdir(parents=True, exist_ok=True)

    # Builds the file names
    main_path = main_folder / save_config.file_name
    edit_path = edit_folder / save_config.file_name
    main_file = main_path.with_suffix(f".{save_config.main_file_type}")
    editable_file = edit_path.with_suffix(f".{save_config.e_file_type}")

    # Save each one depending on the save type
    mode = save_config.save_type.lower()
    if(mode == "default"):
        fig.savefig(main_file)
    elif(mode == "edit"):
        fig.savefig(editable_file)
    elif(mode == "all"):
        fig.savefig(main_file)
        fig.savefig(editable_file)
    elif(mode == "none"):
        pass
    else:
        raise ValueError(f"Unknown save_type: {mode} (expected 'default', 'edit', 'all' or 'none')")
