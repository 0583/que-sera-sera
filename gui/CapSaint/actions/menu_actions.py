#!/usr/bin/env python

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot, QTimer

import baseio.input
import baseio.output

import logging

#############
# File Menu #
#############

@pyqtSlot()
def onMenuImportTapped(self):
    logging.info("Tapped File/Import")
    
    fileName = QFileDialog.getOpenFileNames(None, 'Import Images', '', "Image Files (*.jpg *.jpeg *.gif *.png *.bmp);;Any Files (*)")
    if len(fileName) >= 1:
        if fileName[0] == '':
            return
        for singleName in fileName[0]:
            print(singleName)
            baseio.input.openFile(singleName)

@pyqtSlot()
def onMenuExportTapped(self):
    logging.info("Tapped File/Export")

@pyqtSlot()
def onMenuQuitTapped(self):
    logging.info("Tapped File/Quit")


#################
# Advanced Menu #
#################

@pyqtSlot()
def onVerboseTapped(checked):
    logging.info("Tapped Advanced/Verbose, state = %d" % checked)

#############
# Info Menu #
#############

@pyqtSlot()
def onManualMenuTapped(self):
    logging.info("Tapped Info/Manual")

@pyqtSlot()
def onAboutMenuTapped(self):
    logging.info("Tapped Info/About")

