from PIL import Image
import utils.prompt
import baseimage.imagesetter
import utils.widget_helper

def saveFile(filename: str):
    try:
        if baseimage.imagesetter.isOk():
            baseimage.imagesetter.getImageObject().save(filename)
        else:
            raise TypeError("No Image object to be saved currently.")
    except BaseException as e:
        utils.prompt.showWarning("PIL cannot save file to '%s'.\nDetailed Exception Message: %s" % (filename, e))