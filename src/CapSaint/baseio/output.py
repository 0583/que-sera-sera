from PIL import Image
from PyQt5.QtWidgets import QFileDialog
import utils.prompt
import baseimage.imagesetter
import utils.widget_helper


def saveImage(image):
    try:
        if image:
            fileName = QFileDialog.getSaveFileName(
                None, '匯出檔案', '', "JPEG 圖像 (*.jpg);;JPEG 圖像 (*.jpeg);;GIF 圖像 (*.gif);;PNG 圖像 (*.png);;BMP 圖像 (*.bmp);;任意 (*)")
            if len(fileName) >= 1:
                if fileName[0] == '':
                    return
                image.save(fileName[0])
        else:
            raise TypeError("No Image object to be saved currently.")
    except BaseException as e:
        utils.prompt.showWarning(
            "PIL cannot save file.\nDetailed Exception Message: %s" % (e))
