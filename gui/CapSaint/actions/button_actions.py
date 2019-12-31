#!/usr/bin/env python

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot, QTimer
import logging

@pyqtSlot()
def analyzeCurrentTapped(self):
    logging.info("Tapped Analyze Current Button")

@pyqtSlot()
def analyzeAllTapped(self):
    logging.info("Tapped Analyze All Button")

@pyqtSlot()
def resetCurrentTapped(self):
    logging.info("Tapped Reset Current Button")

@pyqtSlot()
def resetAllTapped(self):
    logging.info("Tapped Reset All Button")

@pyqtSlot()
def previousButtonTapped(self):
    logging.info("Tapped Previous Image Button")

@pyqtSlot()
def nextButtonTapped(self):
    logging.info("Tapped Next Image Button")
