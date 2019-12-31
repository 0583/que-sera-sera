from PIL import Image
import utils.prompt
import baseimage.imagesetter
import utils.widget_helper

def openFile(filename: str):
    try:
        baseimage.imagesetter.appendImage(Image.open(filename))
        # baseimage.imagesetter.displayIt()
        utils.widget_helper.global_ce.refreshDisplay()
    except BaseException as e:
        utils.prompt.showWarning("PIL cannot open '%s'.\nDetailed Exception Message: %s" % (filename, e))