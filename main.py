from Canvas import Canvas
from Square import Square
from Rectangle import Rectangle
from Color import Color


def get_checked_int_value(question: str, min: int, max:int) -> int:
    """keep asking for a value until you get an int in the requisite range"""
    result:int = 0
    while True:
        try:
            result = int(input(question))
            if min <= result <= max:
                return result
            else:
                print(f"{result} not a valid value, must be >= {min} and <= {max}")
        except Exception as e:
            print(e)
            continue


def get_color_name(shapetype: str) -> str:
    while True:
        colorname = input(f"CSS color name for {shapetype} ('?' for list of valid names): ").lower()
        if colorname == '?':
            Color.list_color_names(5)
            continue
        elif Color.get_color_codes(colorname) is None:
            print(f"{colorname} is not a valid color name")
            continue
        return colorname



welcome_str = "Welcome to Steve's version of Math Painting App"
print("\n" + welcome_str + "\n" + len(welcome_str) * "_" + "\n")

# TODO add more complete error checking
# arbitrary limits
canvas_w: int = get_checked_int_value("Width of canvas? ", 10, 1920)
canvas_h: int = get_checked_int_value("Height of canvas? ", 10, 1080)
canvas_colorname = get_color_name("Canvas background")
canvas = Canvas(canvas_w, canvas_h, canvas_colorname)

print(f"Canvas size: {canvas_w} (H) X {canvas_h} (H), color: {canvas_colorname}\n")

shapes = []
while True:
    answer: str = input("Add a shape to the picture " +
                        "((S)quare, (R)ectangle, or (D)one: ")
    answer = answer.lower()
    match answer:
        case 'r':
            print("\nSpecs for rectangle -")
            x = get_checked_int_value("\tupper left x: ", 0, canvas_w - 2)
            y = get_checked_int_value("\tupper left y: ", 0, canvas_h - 2)
            width = get_checked_int_value("\twidth: ", 1, canvas_w - x)
            height = get_checked_int_value("\theight: ", 1, canvas_h - y)
            colorname = get_color_name("Rectangle")
            rect = Rectangle(x, y, width, height, colorname)
            rect.draw(canvas)
        case 's':
            print("\nSpecs for square -")
            x = get_checked_int_value("\tupper left x: ", 0, canvas_w - 2)
            y = get_checked_int_value("\tupper left y: ", 0, canvas_h - 2)
            size = get_checked_int_value("\tsize: ", 1, canvas_w - x)
            colorname = get_color_name("Square")
            rect = Square(x, y, size, colorname)
            rect.draw(canvas)
        case 'd':
            print(f"Done adding, added {len(shapes)} shapes to the canvas")
            break
        case _:
            print("  please answer with S, s, R, r, D, or d")


print("\nNow creating picture file C:\\Temp\\rect", "gif")
canvas.make("C:\\Temp\\rect", "gif")




# canvas = Canvas(1920, 780, "lime")
# rect1 = Rectangle(420, 300, 800, 300, "red")
# rect1.draw(canvas)
# rect2 = Rectangle(240, 400, 300, 600, "blue")
# rect2.draw(canvas)
# square1 = Square(440, 250, 250, "aqua")
# square1.draw(canvas)
# square2 = Square(1500, 400, 120, "yellow")
# square2.draw(canvas)
# rect3 = Rectangle(1200, 450, 650, 200, "springgreen")
# rect3.draw(canvas)
# square3 = Square(1600, 150, 150, "burntsienna")
# square3.draw(canvas)
# canvas.make("C:\\Temp\\rect", "gif")
