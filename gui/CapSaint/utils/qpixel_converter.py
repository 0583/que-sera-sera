import PIL.Image
from PyQt5.QtGui import QPixmap, QImage

def convertToQPixel(im):
    im = im.convert("RGBA")
    data = im.tobytes("raw","RGBA")
    return QPixmap.fromImage(QImage(data, im.size[0], im.size[1], QImage.Format_RGBA8888))