from Canvas import Canvas
from Color import Color


class Rectangle:

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
        left_x:int = self.x - self.width//2
        right_x: int = left_x + self.width
        hi_y = self.y - self.height//2
        lo_y = hi_y + self.height
        canvas.canvas[hi_y:lo_y, left_x:right_x] = \
                        Color.get_color_codes(self.colorname)


# canvas = Canvas(1920, 780, "lime")
# rect1 = Rectangle(420, 300, 800, 300, "red")
# rect1.draw(canvas)
# rect2 = Rectangle(240, 400, 300, 600, "blue")
# rect2.draw(canvas)
# canvas.make("C:\\Temp\\rects2", "gif")
