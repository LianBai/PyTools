import os
import subprocess
import sys

import psutil
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow
from AppUtil import ShowTipDialog, exe_path
from TimerThread import TimerThread, CreatDJDHData, CreateSSSQData
from main_ui import Ui_MainWidget


class MainWindow(QMainWindow, Ui_MainWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.process = None
        self.app = None
        self.isClose = False
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon(os.path.join(exe_path(), "ReptileTools.ico")))
        self.DJDHBtn.clicked.connect(self.CreatDJDHData)
        self.SSSQBtn.clicked.connect(self.CreateSSSQData)

    def show(self):
        super().show()
        savePath = os.path.join(exe_path(), "save")
        if not os.path.exists(savePath):
            os.mkdir(savePath)

    def CreatDJDHData(self):
        CreatDJDHData(False, self)

    def CreateSSSQData(self):
        CreateSSSQData(False, self)



