from tabulate import tabulate

class Color:

    COLOR_DICT = {
        "black": [0, 0, 0],
        "white": [255, 255, 255],
        "silver": [192, 192, 192],
        "gray": [255,  255, 255],
        "red": [255,  0,  0],
        "orange": [255, 165, 0],
        "burntsienna":  [138,54,15],
        "purple": [128,  0,  128],
        "green": [0,  128,  0],
        "springgreen": [0, 255, 127],
        "lime": [0,  255,  0],
        "yellow": [255,  255,  0],
        "blue": [0,  0,  255],
        "teal": [0,  128,  128],
        "aqua": [0,  255,  255]
    }

    def __init__(self, color: str = "white"):
        self.color = color

    @classmethod
    def get_color_codes(cls, color_name: str) -> list:
        if color_name in cls.COLOR_DICT.keys():
            return cls.COLOR_DICT[color_name]
        else:
            return None

    @classmethod
    def list_color_table(cls):
        thead:str = f"{'Color Name':<15}{'RGB Array'}"
        print(thead + "\n" + len(thead) * "-")
        for color_name in cls.COLOR_DICT.keys():
            print(f"{color_name:<15}{cls.COLOR_DICT[color_name]}")

    @classmethod
    def list_color_names(cls, columns: int = 1):
        print('Color Names')
        names = 0
        namelists = []
        namelist = []
        # build 2D list for tabulating in columns
        for color_name in cls.COLOR_DICT.keys():
            namelist.append(color_name)
            names += 1
            if names == columns:
                names = 0
                namelists.append(namelist)
                namelist = []
        if names != 0:
            # partial list left over, append it
            namelists.append(namelist)
        print(tabulate(namelists, [], "simple_grid"))


# print(Color.get_color_codes("aqua"))
# print(Color.get_color_codes("rainbow"))
# Color.list_color_table()
# print("\n")
# Color.list_color_names()
# Color.list_color_names(3)
# Color.list_color_names(5)
# print("\nspringgreen:", Color.get_color_codes("springgreen"))
# print("sprunggreen:", Color.get_color_codes("sprunggreen"))
