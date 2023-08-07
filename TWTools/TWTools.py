import ctypes
import os
import sys

from PyQt5.QtWidgets import QApplication

from MainWindow import MainWindow, TipWidget
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
        if "SvnExePath" in config and os.path.exists(config["SvnExePath"]):
            main.SvnExePath.setText(config["SvnExePath"])
        main.RefreshResLink()
        main.show()
        app.focusChanged.connect(main.RefreshBranch)
    else:
        tip = TipWidget()
        tip.show()
        tip.setWindowTitle("错误")
        tip.label.setText("请以管理员身份运行程序！")
    sys.exit(app.exec())




