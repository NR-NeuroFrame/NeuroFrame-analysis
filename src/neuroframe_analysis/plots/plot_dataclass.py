# ================================================================
# 0. Section: Imports
# ================================================================
from dataclasses import dataclass



# ================================================================
# 1. Section: Bounds Dataclass
# ================================================================
@dataclass
class Bounds:
    x_start: int
    x_end: int
    y_start: int
    y_end: int

    def as_list(self):
        return [self.x_start, self.x_end, self.y_start, self.y_end]

@dataclass
class Viewport:
    x: int
    y: int
    width: float
    height: float

    def as_list(self):
        return [self.x, self.y, self.width, self.height]
