from Canvas import Canvas
from Square import Square
from Rectangle import Rectangle
from Color import Color


canvas = Canvas(1920, 780, "lime")
rect1 = Rectangle(420, 300, 800, 300, "red")
rect1.draw(canvas)
rect2 = Rectangle(240, 400, 300, 600, "blue")
rect2.draw(canvas)
square1 = Square(440, 250, 250, "aqua")
square1.draw(canvas)
square2 = Square(1500, 400, 120, "yellow")
square2.draw(canvas)
rect3 = Rectangle(1200, 450, 650, 200, "springgreen")
rect3.draw(canvas)
square3 = Square(1600, 150, 150, "burntsienna")
square3.draw(canvas)
canvas.make("C:\\Temp\\rect", "gif")
