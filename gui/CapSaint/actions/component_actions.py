#!/usr/bin/env python

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot, QTimer
import logging

@pyqtSlot()
def onZoomRatioChanged(self):
    logging.info("Tapped Image Zoom")

@pyqtSlot()
def onColorDistinguishChecked(self):
    logging.info("Tapped Color Distinguish Checker")

@pyqtSlot()
def onSensitivityChanged(self):
    logging.info("Tapped Sensitivity Selector")
