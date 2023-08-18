import ctypes
import os
import sys

from PyQt5.QtWidgets import QApplication

from MainWindow import MainWindow
from JsonUtil import LoadJsonData


if __name__ == '__main__':
    app = QApplication(sys.argv)
    if ctypes.windll.shell32.IsUserAnAdmin() != 0:
        main = MainWindow()
        config = LoadJsonData()
        if "ProPath" in config and os.path.exists(config["ProPath"]):
            main.ProPath.setText(config["ProPath"])
            main.RefreshBranch()
            main.RefreshSvnPath()
        else:
            main.ProPathSearchBtnClicked()
        main.RefreshResLink()
        main.show()
        app.focusChanged.connect(main.RefreshBranch)
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    sys.exit(app.exec())




