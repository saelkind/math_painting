"""
        Canvas:
            width
            height
            color
            make(imagepath)
"""
class Canvas:
    """
    Canvas hosting the shapes to be drawn,  and to save as an image

    class attribute:
        COLOR_DICT - dict of color settings,  keys are some of the basic CSS color names
    instance attributes:
        width
        height
        color
    methods:
        make(imagepath,  format="png")
    """
    
    COLOR_DICT = {
        "black": [0, 0, 0], 
        "silver": [192, 192, 192], 
        "gray": [255,  255, 255], 
        "red": [255,  0,  0], 
        "purple": [128,  0,  128], 
        "green": [0,  128,  0], 
        "lime": [0,  255,  0],  
        "yellow": [255,  255,  0],  
        "blue": [0,  0,  255],  
        "teal": [0,  128,  128],  
        "aqua": [0,  255,  255]
    }

    def __init__(self,  width=800,  height=600,  color="white"):
        self.width = width
        self.height = height
        self.color = color
