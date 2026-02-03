# ================================================================
# 0. Section: Imports
# ================================================================
from functools import wraps

from .save_dataclass import default_save_config
from .save_plots import save_plot

from ..logger import logger



# ================================================================
# 1. Section: Saving
# ================================================================
def save_figure_protocol(func):
    @wraps(func)
    def wrapper(*args, **kwargs) -> None:
        try:
            fig, ax, config = func(*args, **kwargs)
        except (ValueError, TypeError) as e:
            logger.warning(f"{func.__name__} must return (fig, ax, config).")
            try:
                fig, ax = func(*args, **kwargs)
                config = default_save_config
            except (ValueError, TypeError) as e:
                result = func(*args, **kwargs)
                logger.critical(f"{func.__name__} must return at least (fig, ax) and is returning {result}")
                raise ValueError(f"{func.__name__} must return at least (fig, ax).") from e

        save_plot(fig, ax, config)
    return wrapper
