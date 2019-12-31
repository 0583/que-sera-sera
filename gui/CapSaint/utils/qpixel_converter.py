import PIL.Image
from PyQt5.QtGui import QPixmap, QImage

def convertToQPixel(im, ratio=1.0):
    size = int(im.size[0] * ratio), int(im.size[1] * ratio)
    
    im = im.convert("RGBA").resize(size, PIL.Image.ANTIALIAS)
    data = im.tobytes("raw","RGBA")
    return QPixmap.fromImage(QImage(data, im.size[0], im.size[1], QImage.Format_RGBA8888))