from Canvas import Canvas
from Color import Color


class Rectangle:
    """
    Rectangle to be drawn on canvas.  All drawings integers only
    Instance variables:
        x: upper left x coord
        y: upper left y coord
        width: width
        height: height
        colorname: CSS name of the color, from a limited palette
    """

    def __init__(self, x: int, y: int, width: int, height: int, colorname: str):
        """Does not check for correctness of color string"""
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colorname = colorname

    def draw(self, canvas: Canvas):
        # TODO add error checking of args?  Or trust them?
        # TODO check if boundaries outside canvas, and adjust so partial rect drawn
        #   (note: if any of rect off-canvas, nothing drewn (silently?)
        canvas.canvas[self.y : self.y+self.height, self.x : self.x+self.width] = \
                        Color.get_color_codes(self.colorname)


# canvas = Canvas(1920, 780, "lime")
# rect1 = Rectangle(420, 300, 800, 300, "red")
# rect1.draw(canvas)
# rect2 = Rectangle(240, 400, 300, 600, "blue")
# rect2.draw(canvas)
# canvas.make("C:\\Temp\\rects2", "gif")
