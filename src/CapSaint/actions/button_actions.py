#!/usr/bin/env python

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot, QTimer
import logging
import baseimage.imagesetter
import varargs.varargs
import utils.widget_helper

@pyqtSlot()
def analyzeCurrentTapped(self):
    logging.info("Tapped Analyze Current Button")

@pyqtSlot()
def analyzeAllTapped(self):
    logging.info("Tapped Analyze All Button")

@pyqtSlot()
def resetCurrentTapped(self):
    logging.info("Tapped Reset Current Button")
    if varargs.varargs.currentImageIndex >= 1 and varargs.varargs.currentImageIndex <= baseimage.imagesetter.getCount():
        baseimage.imagesetter.removeImageAt(varargs.varargs.currentImageIndex - 1)
        utils.widget_helper.global_ce.refreshDisplay()
    else:
        logging.error("Failed to remove image #%d, total count = %d" % (varargs.varargs.currentImageIndex, baseimage.imagesetter.getCount()))

@pyqtSlot()
def resetAllTapped(self):
    logging.info("Tapped Reset All Button")
    baseimage.imagesetter.clearImageObject()
    utils.widget_helper.global_ce.refreshDisplay()

@pyqtSlot()
def previousButtonTapped(self):
    logging.info("Tapped Previous Image Button")
    if varargs.varargs.currentImageIndex > 1 and varargs.varargs.currentImageIndex <= baseimage.imagesetter.getCount():
        varargs.varargs.currentImageIndex -= 1
        utils.widget_helper.global_ce.refreshDisplay()
    else:
        logging.error("invalid previous button call when current = %d" % varargs.varargs.currentImageIndex)

@pyqtSlot()
def nextButtonTapped(self):
    logging.info("Tapped Next Image Button")
    if varargs.varargs.currentImageIndex >= 1 and varargs.varargs.currentImageIndex < baseimage.imagesetter.getCount():
        varargs.varargs.currentImageIndex += 1
        utils.widget_helper.global_ce.refreshDisplay()
    else:
        logging.error("invalid next button call when current = %d" % varargs.varargs.currentImageIndex)