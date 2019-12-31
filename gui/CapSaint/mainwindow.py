# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menuSensitivity = QtWidgets.QMenu(self.menu_3)
        self.menuSensitivity.setObjectName("menuSensitivity")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAbout_2 = QtWidgets.QAction(MainWindow)
        self.actionAbout_2.setObjectName("actionAbout_2")
        self.actionImport = QtWidgets.QAction(MainWindow)
        self.actionImport.setObjectName("actionImport")
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionLow = QtWidgets.QAction(MainWindow)
        self.actionLow.setCheckable(True)
        self.actionLow.setObjectName("actionLow")
        self.actionMedium = QtWidgets.QAction(MainWindow)
        self.actionMedium.setCheckable(True)
        self.actionMedium.setChecked(True)
        self.actionMedium.setObjectName("actionMedium")
        self.actionHigh = QtWidgets.QAction(MainWindow)
        self.actionHigh.setCheckable(True)
        self.actionHigh.setObjectName("actionHigh")
        self.actionUse_Color_to_Distinguist = QtWidgets.QAction(MainWindow)
        self.actionUse_Color_to_Distinguist.setCheckable(True)
        self.actionUse_Color_to_Distinguist.setObjectName("actionUse_Color_to_Distinguist")
        self.actionStart_Analyze = QtWidgets.QAction(MainWindow)
        self.actionStart_Analyze.setObjectName("actionStart_Analyze")
        self.actionRest = QtWidgets.QAction(MainWindow)
        self.actionRest.setObjectName("actionRest")
        self.actionVerbose_Mode = QtWidgets.QAction(MainWindow)
        self.actionVerbose_Mode.setCheckable(True)
        self.actionVerbose_Mode.setObjectName("actionVerbose_Mode")
        self.menu.addAction(self.actionImport)
        self.menu.addAction(self.actionExport)
        self.menu.addSeparator()
        self.menu.addAction(self.actionQuit)
        self.menu_2.addAction(self.actionAbout)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.actionAbout_2)
        self.menuSensitivity.addAction(self.actionLow)
        self.menuSensitivity.addAction(self.actionMedium)
        self.menuSensitivity.addAction(self.actionHigh)
        self.menu_3.addAction(self.menuSensitivity.menuAction())
        self.menu_3.addSeparator()
        self.menu_3.addAction(self.actionUse_Color_to_Distinguist)
        self.menu_3.addAction(self.actionVerbose_Mode)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu.setTitle(_translate("MainWindow", "File"))
        self.menu_2.setTitle(_translate("MainWindow", "Info"))
        self.menu_3.setTitle(_translate("MainWindow", "Preferences"))
        self.menuSensitivity.setTitle(_translate("MainWindow", "Sensitivity"))
        self.actionAbout.setText(_translate("MainWindow", "Manual"))
        self.actionAbout_2.setText(_translate("MainWindow", "About"))
        self.actionImport.setText(_translate("MainWindow", "Import Images..."))
        self.actionExport.setText(_translate("MainWindow", "Export CurrentImage..."))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionLow.setText(_translate("MainWindow", "Low"))
        self.actionMedium.setText(_translate("MainWindow", "Medium"))
        self.actionHigh.setText(_translate("MainWindow", "High"))
        self.actionUse_Color_to_Distinguist.setText(_translate("MainWindow", "Use Color to Distinguish"))
        self.actionStart_Analyze.setText(_translate("MainWindow", "Start Analyze"))
        self.actionRest.setText(_translate("MainWindow", "Rest"))
        self.actionVerbose_Mode.setText(_translate("MainWindow", "Verbose Mode"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
