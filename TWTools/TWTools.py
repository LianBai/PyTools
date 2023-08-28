import ctypes
import os
import sys

from PyQt5.QtWidgets import QApplication

from MainWindow import MainWindow
from JsonUtil import LoadJsonData, SaveJsonData

if __name__ == '__main__':
    app = QApplication(sys.argv)
    if ctypes.windll.shell32.IsUserAnAdmin() != 0:
        main = MainWindow()
        main.show(app)
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    sys.exit(app.exec())




