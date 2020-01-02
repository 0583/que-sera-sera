import PIL
import cv2
import numpy
import logging
import utils.prompt
import algorithms.processor


def processImage(pil_image):
    open_cv_image = numpy.array(pil_image)
    # Convert RGB to BGR
    open_cv_image = open_cv_image[:, :, ::-1].copy()

    result_image = algorithms.processor.split(open_cv_image)[0]

    utils.prompt.showWarning("Congratulations! Processing successfully over.")

    logging.info(str(result_image))
    # result_image = cv2.cvtColor(result_image, cv2.COLOR_BGR2RGB)
    # result_PIL = PIL.Image.fromarray(result_image)

    # return result_PIL
    return pil_image


processedImgPointers = []
