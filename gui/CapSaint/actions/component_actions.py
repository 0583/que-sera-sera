#!/usr/bin/env python

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot, QTimer
import logging

@pyqtSlot()
def onZoomRatioChanged(value):
    logging.info("Tapped Image Zoom, current value: %.1f" % value)

@pyqtSlot()
def onColorDistinguishChecked(checked):
    logging.info("Tapped Color Distinguish Checker. value: %d" % checked)

@pyqtSlot()
def onSensitivityChanged(level):
    logging.info("Tapped Sensitivity Selector, level: %d" % level)
