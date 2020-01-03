from PyQt5.QtWidgets import *
import utils.widget_helper


def showWarning(warning_info: str):
    QMessageBox.warning(utils.widget_helper.global_widget,
                        "CapSaint says...", warning_info, QMessageBox.Ok)
