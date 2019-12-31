#!/usr/bin/env python

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot, QTimer
import logging
import varargs.varargs
import utils.widget_helper

@pyqtSlot()
def onZoomRatioChanged(value):
    logging.info("Tapped Image Zoom, current value: %.1f" % value)
    varargs.varargs.zoomRatio = max(0.1, min(value, 10.0))
    utils.widget_helper.global_ce.refreshDisplay()

@pyqtSlot()
def onColorDistinguishChecked(checked):
    logging.info("Tapped Color Distinguish Checker. value: %d" % checked)

@pyqtSlot()
def onSensitivityChanged(level):
    logging.info("Tapped Sensitivity Selector, level: %d" % level)
