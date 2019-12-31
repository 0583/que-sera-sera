#!/usr/bin/env python

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot, QTimer
import logging

#############
# File Menu #
#############

@pyqtSlot()
def onMenuImportTapped(self):
    logging.info("Tapped File/Import")

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

