import sys
import os

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt, QEvent, SLOT
from PySide6.QtGui import QImage, QPixmap, QFont
from PySide6.QtWidgets import (QMainWindow, QApplication,
                               QWidget, QInputDialog, QMenu,
                               QVBoxLayout, QLabel, QMessageBox,
                               QDialog, QPushButton, QMainWindow
                               )
from ui import Ui_Dialog
from ui import resources_qrc




class splashWid(QDialog, Ui_Dialog):
    """"
    A cool retro game splash screen.
    """
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        splash = QPixmap(":/icons/splash.jpeg")
        self.icon_label.setPixmap(splash)
        self.status.setFont(QFont('IBM 3270', 26))
        self._set_status("Game loading ...")
        self.show()

    def _set_status(self, text):
        """
        Update the status message.
        :param text:
        :return:
        """
        self.status.setText(text)


def main():
    app = QApplication(sys.argv)
    myWid = splashWid()
    #QtCore.QTimer.singleShot(3000, lambda: myWid._set_status("Loading maps ..."))
    #QtCore.QTimer.singleShot(3000, lambda: myWid._set_status("Ready !"))

    # This sample program automatically terminates after 10s (10,000 milliseconds).
    # The receiver is the receiving object and the member is the slot.
    # The time interval is msec milliseconds.
    QtCore.QTimer.singleShot(10000, app, SLOT("quit()"))
    # If we want just to hide the dialog
    # QtCore.QTimer.singleShot(3000, lambda: myWid.hide())
    # QtCore.QTimer.singleShot(3000, lambda: myWid.setVisible(False))
    sys.exit(app.exec())




# Entry Point
if __name__=="__main__":
    main()





