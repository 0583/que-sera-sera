#!/usr/bin/env python

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot, QTimer
import logging
import baseimage.imagesetter
import varargs.varargs
import utils.widget_helper
import utils.prompt
import wrapper.wrapper


@pyqtSlot()
def analyzeCurrentTapped(self):
    logging.info("Tapped Analyze Current Button")

    if varargs.varargs.currentImageIndex >= 1 and varargs.varargs.currentImageIndex <= baseimage.imagesetter.getCount():
        originImage = baseimage.imagesetter.getImageAt(
            varargs.varargs.currentImageIndex - 1)

        if originImage in wrapper.wrapper.processedImgPointers:
            utils.prompt.showWarning(
                "Cannot process image since it has been marked before.")
            return
        image = wrapper.wrapper.processImage(originImage)
        baseimage.imagesetter.setImageAt(
            varargs.varargs.currentImageIndex - 1, image)
        wrapper.wrapper.processedImgPointers.append(image)
        utils.widget_helper.global_ce.refreshDisplay()
    else:
        logging.error("Failed to remove image #%d, total count = %d" % (
            varargs.varargs.currentImageIndex, baseimage.imagesetter.getCount()))


@pyqtSlot()
def analyzeAllTapped(self):
    logging.info("Tapped Analyze All Button")


@pyqtSlot()
def resetCurrentTapped(self):
    logging.info("Tapped Reset Current Button")
    if varargs.varargs.currentImageIndex >= 1 and varargs.varargs.currentImageIndex <= baseimage.imagesetter.getCount():
        if baseimage.imagesetter.getImageAt(varargs.varargs.currentImageIndex - 1) in wrapper.wrapper.processedImgPointers:
            wrapper.wrapper.processedImgPointers.remove(
                baseimage.imagesetter.getImageAt(varargs.varargs.currentImageIndex - 1))
        baseimage.imagesetter.removeImageAt(
            varargs.varargs.currentImageIndex - 1)
        varargs.varargs.currentImageIndex = min(
            varargs.varargs.currentImageIndex, baseimage.imagesetter.getCount())
        utils.widget_helper.global_ce.refreshDisplay()
    else:
        logging.error("Failed to remove image #%d, total count = %d" % (
            varargs.varargs.currentImageIndex, baseimage.imagesetter.getCount()))


@pyqtSlot()
def resetAllTapped(self):
    logging.info("Tapped Reset All Button")
    baseimage.imagesetter.clearImageObject()
    wrapper.wrapper.processedImgPointers.clear()
    utils.widget_helper.global_ce.refreshDisplay()


@pyqtSlot()
def previousButtonTapped(self):
    logging.info("Tapped Previous Image Button")
    if varargs.varargs.currentImageIndex > 1 and varargs.varargs.currentImageIndex <= baseimage.imagesetter.getCount():
        varargs.varargs.currentImageIndex -= 1
        utils.widget_helper.global_ce.refreshDisplay()
    else:
        logging.error("invalid previous button call when current = %d" %
                      varargs.varargs.currentImageIndex)


@pyqtSlot()
def nextButtonTapped(self):
    logging.info("Tapped Next Image Button")
    if varargs.varargs.currentImageIndex >= 1 and varargs.varargs.currentImageIndex < baseimage.imagesetter.getCount():
        varargs.varargs.currentImageIndex += 1
        utils.widget_helper.global_ce.refreshDisplay()
    else:
        logging.error("invalid next button call when current = %d" %
                      varargs.varargs.currentImageIndex)
