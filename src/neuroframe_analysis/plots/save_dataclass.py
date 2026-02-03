# ================================================================
# 0. Section: Imports
# ================================================================
from dataclasses import dataclass



# ================================================================
# 1. Section: Saving Configurations
# ================================================================
@dataclass
class SaveConfiguration():
    """Dataclass for helping with saving plots"""
    save_type: str = "all"
    main_file_type: str = "png"
    e_file_type: str = "svg"
    output_path: str = "figures/"
    file_name: str = "plot"

default_save_config = SaveConfiguration(
    save_type="all",
    main_file_type = "png",
    e_file_type = "svg", # editable file type
    output_path = "figures/",
    file_name = "plot"
)
