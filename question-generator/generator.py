
import sys
import os
import json
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtWidgets import QMainWindow, QApplication
from resources import resources_rc

from ui.generatormainwindow import Ui_MainWindow

basedir = os.path.dirname(__file__)

tick = QImage(os.path.join(basedir, "resources/tick.png"))



class MainWindow(QMainWindow, Ui_MainWindow):
    finput_name = None
    fout_name = None

    def __init__(self):
        super().__init__()
        # Load the ui from Ui_MainWindow
        self.setupUi(self)
        # Pre-populate the widget with some todo´s
        # Fill the model with the data
        # Load the data
        # Some extra button configuration
        icon = QtGui.QPixmap(":/icons/skullIcon.png")
        self.pushButton.setIcon(QtGui.QIcon(icon))
        self.pushButton.clicked.connect(self._build)
        #self.pushButton.clicked.connect(self._refresh)
        self.pushButton_2.pressed.connect(self.browse_input_file)
        self.pushButton_4.pressed.connect(self.browse_output_file)
        self.show()

    def browse_input_file(self):
        finput = QtWidgets.QFileDialog.getOpenFileName()
        self.finput_name = finput[0]
        print("Complete!")
        # text = self.lineEdit.text()
        self.lineEdit_2.setText(f"{self.finput_name}")

    def browse_output_file(self):
        fout = QtWidgets.QFileDialog.getOpenFileName()
        self.fout_name = fout[0]
        print("Complete!")
        self.lineEdit_3.setText(f"{self.fout_name}")

    def _build(self):
        print("Generating file...")



# Entry Point
if __name__=="__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.setStyle("Fusion")
    app.exec()