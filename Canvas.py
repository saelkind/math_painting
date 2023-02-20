import numpy as np
from PIL import Image
from Color import Color

class Canvas:
    """
    Canvas hosting the shapes to be drawn,  and to save as an image

    class attribute:
        SUPPORTED_FORMATS - supported list of picture formats as file extensions
    instance attributes:
        width
        height
        color
    methods:
        make(imagepath,  format="png")
    """

    SUPPORTED_FORMATS = ["png", "gif", "jpg"]
    
    def __init__(self,  width=800,  height=600,  colorname="white"):
        self.width = width
        self.height = height
        self.colorname = colorname
        self.canvas = np.zeros((height, width, 3), dtype=np.uint8)
        # print(type(Color.get_color_codes(colorname)))
        self.canvas[:] = Color.get_color_codes(colorname)

    def make(self, imagepath:str, imgformat:str = "png") -> str:
        if imgformat in Canvas.SUPPORTED_FORMATS:
            filename = imagepath + "." + imgformat
            # TODO check for ability to write the file
            image = Image.fromarray(self.canvas, 'RGB')
            image.save(imagepath + "." + imgformat)
            return "Success"
        else:
            return f"Invalid format '{imgformat}', formats allowed are:  {Canvas.SUPPORTED_FORMATS}"  \


#
# canvas = Canvas()
# canvas.make("C:\\Temp\\canv_white", "png")
#
# canvas = Canvas(1920, 780, "lime")
# canvas.make("C:\\Temp\\canv_lime", "png")
