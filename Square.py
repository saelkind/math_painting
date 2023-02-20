from Color import Color
from Rectangle import Rectangle

class Square(Rectangle):
    """
    Subclass of Rectangle, __init__ different in that size replaces width and height
    """

    def __init__(self, x: int, y: int, size: int, colorname: str):
        self.size = size
        super().__init__(x, y, size, size, colorname)
