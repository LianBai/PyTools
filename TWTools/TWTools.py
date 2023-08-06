import os
import sys


from PySide6.QtWidgets import QApplication

from MainWindow import MainWindow
from JsonUtil import LoadJsonData

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    config = LoadJsonData()
    if "ProPath" in config and os.path.exists(config["ProPath"]):
        main.ProPath.setText(config["ProPath"])
        main.RefreshBranch()
        main.RefreshSvnPath()
    else:
        main.ProPathSearchBtnClicked()
    if "SvnExePath" in config and os.path.exists(config["SvnExePath"]):
        main.SvnExePath.setText(config["SvnExePath"])
    main.RefreshResLink()
    main.show()
    app.focusChanged.connect(main.RefreshBranch)
    sys.exit(app.exec())

