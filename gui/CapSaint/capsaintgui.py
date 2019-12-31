# This Python file uses the following encoding: utf-8
import sys
import mainwindow
from PyQt5 import QtWidgets

class CapSaintGui(QtWidgets.QMainWindow):
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = mainwindow.Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())

if __name__ == "__main__":
    CapSaintGui()
