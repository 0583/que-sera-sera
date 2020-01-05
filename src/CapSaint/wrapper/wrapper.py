import PIL
from PIL import ImageDraw, ImageFont
import cv2
import math
import numpy
import logging
import utils.prompt
import varargs.varargs
import algorithms.processor


def __dirtyWrapper(rec):
    rec.x, rec.y = rec.y, rec.x
    return rec


__strokeWidthRatio = 225
__textSizeRatio = 33
__textMarginRatio = 1.1


def makeMarking(pil_image: PIL.Image, rec):
    for tag in rec:
        rect = __dirtyWrapper(tag.rect)

        if varargs.varargs.useColorToDistinguish:

            b, g, r = tag.color[0], tag.color[1], tag.color[2]
            dim_r, dim_g, dim_b = math.sqrt(
                r) * 10, math.sqrt(g) * 10, math.sqrt(b) * 10

            color = (int(r), int(g), int(b))
            dim_color = (int(dim_r), int(dim_g), int(dim_b))

            # print(color)
            # print(dim_color)
        else:
            color = (127, 127, 127)
            dim_color = (97, 97, 97)

        w, h = pil_image.size

        __markTextSize = int(math.sqrt(w * h)) // __textSizeRatio
        __markFont = ImageFont.truetype("./fonts/DIN-Bold.otf", __markTextSize)

        strokeWidth = int(math.sqrt(w * h)) // __strokeWidthRatio

        drawer = PIL.ImageDraw.Draw(pil_image)

        if tag.type == algorithms.BottleCapType.INVALID:
            # don't draw invalid stuff
            continue
        elif tag.type == algorithms.BottleCapType.NEG:
            drawer.text((rect.x, rect.y - __markTextSize * __textMarginRatio), "Negative", fill=dim_color,
                        font=__markFont, align='left')
        elif tag.type == algorithms.BottleCapType.POS:
            drawer.text((rect.x, rect.y - __markTextSize * __textMarginRatio), "Positive", fill=dim_color,
                        font=__markFont, align='left')
        elif tag.type == algorithms.BottleCapType.STANDING:
            drawer.text((rect.x, rect.y - __markTextSize * __textMarginRatio), "Standing", fill=dim_color,
                        font=__markFont, align='left')

        drawer.rectangle([(rect.x, rect.y),
                          (rect.x + rect.w, rect.y + rect.h)], outline=color, width=strokeWidth)

        # def __drawPixel(x, y, color):
        #     for ax in range(max(0, x - __halfStrokeWidth), min(x + __halfStrokeWidth, w)):
        #         for ay in range(max(0, y - __halfStrokeWidth), min(y + __halfStrokeWidth, h)):
        #             pil_image.putpixel((x, y), color)

        # for x in range(rect.x, rect.x + rect.w):
        #     # print("put pixel @", (x, rect.y))
        #     __drawPixel(x, rect.y, color)

        #     # print("put pixel @", (x, min(rect.y + rect.h, h)))
        #     __drawPixel(x, rect.y + rect.h, color)

        # for y in range(rect.y, rect.y + rect.h):
        #     # print("put pixel @ ", (min(rect.x, w), y))
        #     __drawPixel(rect.x, y, color)
        #     # print("put pixel @ ", (min(rect.x + rect.w, w), y))
        #     __drawPixel(rect.x + rect.w, y, color)

    return pil_image


def processImage(pil_image):
    open_cv_image = numpy.array(pil_image)
    # Convert RGB to BGR
    open_cv_image = open_cv_image[:, :, ::-1].copy()

    identifier = algorithms.processor.Identify()
    lv = varargs.varargs.sensitivityLevel

    if lv == 0:
        identifier.threshold = 0.75
    elif lv == 1:
        identifier.threshold = 0.8
    elif lv == 2:
        identifier.threshold = 0.85
    elif lv == 3:
        identifier.threshold = 0.9

    process_output = identifier.process(open_cv_image)

    utils.prompt.showWarning("Congratulations! Processing successfully over.")

    logging.info(str(process_output))
    # result_image = cv2.cvtColor(result_image, cv2.COLOR_BGR2RGB)
    # result_PIL = PIL.Image.fromarray(result_image)

    # return result_PIL

    return makeMarking(pil_image, process_output)


processedImgPointers = []
