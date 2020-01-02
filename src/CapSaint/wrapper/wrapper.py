import PIL
import cv2
import numpy
import logging
import utils.prompt
import varargs.varargs
import algorithms.processor


def __dirtyWrapper(rec):
    rec.x, rec.y = rec.y, rec.x
    return rec


def makeMarking(pil_image, rec):
    for tag in rec:
        rect = __dirtyWrapper(tag.rect)

        w, h = pil_image.size
        print("image size = ", w, h)
        print("gotta rect ", str(tag.rect))
        w -= 1
        h -= 1
        if tag.type == algorithms.BottleCapType.INVALID:
            # don't draw invalid stuff
            continue
        elif tag.type == algorithms.BottleCapType.NEG:
            color = (255, 255, 0)
        elif tag.type == algorithms.BottleCapType.POS:
            color = (0, 255, 255)
        elif tag.type == algorithms.BottleCapType.STANDING:
            color = (255, 0, 255)

        for x in range(rect.x, min(rect.x + rect.w, w)):
            # print("put pixel @", (x, rect.y))
            pil_image.putpixel((x, min(rect.y, h)), color)

            # print("put pixel @", (x, min(rect.y + rect.h, h)))
            pil_image.putpixel((x, min(rect.y + rect.h, h)), color)

        for y in range(rect.y, min(rect.y + rect.h, h)):
            # print("put pixel @ ", (min(rect.x, w), y))
            pil_image.putpixel((rect.x, y), color)
            # print("put pixel @ ", (min(rect.x + rect.w, w), y))
            pil_image.putpixel((min(rect.x + rect.w, w), y), color)

    print(type(pil_image))
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
