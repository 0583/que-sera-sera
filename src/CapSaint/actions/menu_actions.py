#!/usr/bin/env python

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot, QTimer

import baseio.input
import baseio.output
import varargs.varargs
import baseimage.imagesetter

import logging

#############
# File Menu #
#############


@pyqtSlot()
def onMenuImportTapped(self):
    logging.info("Tapped File/Import")

    fileName = QFileDialog.getOpenFileNames(
        None, 'Import Images', '', "Image Files (*.jpg *.jpeg *.gif *.png *.bmp);;Any Files (*)")
    if len(fileName) >= 1:
        if fileName[0] == '':
            return
        for singleName in fileName[0]:
            logging.info("going to open file %s" % singleName)
            baseio.input.openFile(singleName)


@pyqtSlot()
def onMenuExportTapped(self):
    logging.info("Tapped File/Export")
    if varargs.varargs.currentImageIndex >= 1 and varargs.varargs.currentImageIndex <= baseimage.imagesetter.getCount():
        baseio.output.saveImage(baseimage.imagesetter.getImageAt(
            varargs.varargs.currentImageIndex - 1))
    else:
        logging.error("Failed to remove image #%d, total count = %d" % (
            varargs.varargs.currentImageIndex, baseimage.imagesetter.getCount()))


@pyqtSlot()
def onMenuQuitTapped(self):
    logging.info("Tapped File/Quit")
    exit(0)


#################
# Advanced Menu #
#################

@pyqtSlot()
def onVerboseTapped(checked):
    logging.info("Tapped Advanced/Verbose, state = %d" % checked)
    varargs.varargs.verboseMode = checked

    if checked:
        logging.getLogger().setLevel(logging.DEBUG)
    else:
        logging.getLogger().setLevel(logging.ERROR)

#############
# Info Menu #
#############


@pyqtSlot()
def onManualMenuTapped(self):
    logging.info("Tapped Info/Manual")


@pyqtSlot()
def onAboutMenuTapped(self):
    logging.info("Tapped Info/About")
