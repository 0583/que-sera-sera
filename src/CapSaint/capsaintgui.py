# This Python file uses the following encoding: utf-8
import sys
import logging
import mainwindow

import utils.prompt
import utils.widget_helper
import utils.qpixel_converter
import varargs.varargs
import baseimage

# import action handlers
import actions.button_actions
import actions.component_actions
import actions.menu_actions

from PyQt5 import QtWidgets

DEBUG = False

global_ui = None


class CapSaintGui(QtWidgets.QMainWindow):
    def __init__(self):
        global global_ui

        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()

        ui = mainwindow.Ui_MainWindow()
        global_ui = ui
        ui.setupUi(MainWindow)

        self.bind_actions()

        self.refreshDisplay()

        utils.widget_helper.global_ce = self

        MainWindow.show()
        sys.exit(app.exec_())

    def bind_actions(self):
        global global_ui
        if not global_ui:
            logging.error("bind_actions: Failed to access global_ui")
            assert(False)

        global_ui.actionImport.triggered.connect(
            actions.menu_actions.onMenuImportTapped)
        global_ui.actionExport.triggered.connect(
            actions.menu_actions.onMenuExportTapped)
        global_ui.actionQuit.triggered.connect(
            actions.menu_actions.onMenuQuitTapped)

        global_ui.actionVerbose.triggered.connect(
            lambda: actions.menu_actions.onVerboseTapped(global_ui.actionVerbose.isChecked()))
        global_ui.actionManual.triggered.connect(
            actions.menu_actions.onManualMenuTapped)
        global_ui.actionAbout.triggered.connect(
            actions.menu_actions.onAboutMenuTapped)

        global_ui.zoomIndicator.valueChanged.connect(
            lambda: actions.component_actions.onZoomRatioChanged(global_ui.zoomIndicator.value()))
        global_ui.colorDistCheckBox.stateChanged.connect(
            lambda: actions.component_actions.onColorDistinguishChecked(global_ui.colorDistCheckBox.isChecked()))
        global_ui.sensitivitySelector.currentIndexChanged.connect(
            lambda: actions.component_actions.onSensitivityChanged(global_ui.sensitivitySelector.currentIndex()))

        global_ui.analyzeThisButton.clicked.connect(
            actions.button_actions.analyzeCurrentTapped)
        global_ui.analyzeAllButton.clicked.connect(
            actions.button_actions.analyzeAllTapped)

        global_ui.resetThisButton.clicked.connect(
            actions.button_actions.resetCurrentTapped)
        global_ui.resetAllButton.clicked.connect(
            actions.button_actions.resetAllTapped)

        global_ui.previousButton.clicked.connect(
            actions.button_actions.previousButtonTapped)
        global_ui.nextButton.clicked.connect(
            actions.button_actions.nextButtonTapped)

        # initialize sensitivity = medium
        global_ui.sensitivitySelector.setCurrentIndex(1)

        # initialize verbose mode = off
        global_ui.actionVerbose.setChecked(False)

        # initialize distinguish by color = on
        global_ui.colorDistCheckBox.setChecked(True)

    def refreshDisplay(self):
        global global_ui
        logging.info("Recalled refreshDisplay")
        image_cnt = baseimage.imagesetter.getCount()
        if image_cnt == 0:
            varargs.varargs.currentImageIndex = 0
            global_ui.pageIndicatorLabel.setText("No Image")
            global_ui.pageProgressBar.setMaximum(1)
            global_ui.pageProgressBar.setValue(1)
            global_ui.pageProgressBar.setHidden(True)

            global_ui.actionExport.setEnabled(False)

            global_ui.zoomIndicator.setEnabled(False)

            global_ui.previousButton.setEnabled(False)
            global_ui.nextButton.setEnabled(False)

            global_ui.analyzeAllButton.setEnabled(False)
            global_ui.analyzeThisButton.setEnabled(False)
            global_ui.resetAllButton.setEnabled(False)
            global_ui.resetThisButton.setEnabled(False)

            global_ui.graphicsView.clear()
            logging.info("trivial call of refreshDisplay")
            return

        global_ui.actionExport.setEnabled(True)
        global_ui.zoomIndicator.setEnabled(True)
        global_ui.analyzeAllButton.setEnabled(True)
        global_ui.analyzeThisButton.setEnabled(True)
        global_ui.resetAllButton.setEnabled(True)
        global_ui.resetThisButton.setEnabled(True)
        global_ui.pageProgressBar.setHidden(False)

        if varargs.varargs.currentImageIndex < 1 or varargs.varargs.currentImageIndex > image_cnt:
            varargs.varargs.currentImageIndex = 1

        global_ui.pageIndicatorLabel.setText("%d of %d" % (
            varargs.varargs.currentImageIndex, image_cnt))
        global_ui.pageProgressBar.setMaximum(image_cnt)
        global_ui.pageProgressBar.setValue(varargs.varargs.currentImageIndex)

        if varargs.varargs.currentImageIndex == 1:
            global_ui.previousButton.setEnabled(False)
        else:
            global_ui.previousButton.setEnabled(True)

        if varargs.varargs.currentImageIndex == image_cnt:
            global_ui.nextButton.setEnabled(False)
        else:
            global_ui.nextButton.setEnabled(True)

        logging.info("preparing to refresh graphics view display")
        global_ui.graphicsView.setPixmap(utils.qpixel_converter.convertToQPixel(
            baseimage.imagesetter.getImageAt(varargs.varargs.currentImageIndex - 1), global_ui.zoomIndicator.value()))


if __name__ == "__main__":
    if DEBUG:
        logging.basicConfig(level=logging.DEBUG)

    CapSaintGui()
