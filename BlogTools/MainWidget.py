import io
import os
import subprocess
import sys
import threading

from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QIcon

from WidgetMain import Ui_MainWidget
from FileUtil import SearchDir
from JsonUtil import LoadJsonData, SaveJsonData
from TipUtil import ShowTipDialog, ShowLogDialog, ShowLogDialogNoExit

sys.stdout = io.TextIOWrapper(io.BytesIO(), 'utf-8', errors='ignore')
sys.stderr = io.TextIOWrapper(io.BytesIO(), 'utf-8', errors='ignore')


class MainWindow(QWidget, Ui_MainWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowIcon(QIcon("BlogTools.ico"))
        self.setupUi(self)
        self.BlogPathSearchBtn.clicked.connect(self.BlogPathSearchBtnClicked)
        self.DebugBtn.clicked.connect(self.DebugBtnClicked)
        self.DeployBtn.clicked.connect(self.DeployBtnClicked)
        self.DeployPushBtn.clicked.connect(self.DeployPushBtnClicked)
        self.OpenBlogPathBtn.clicked.connect(self.OpenBlogPathBtnClicked)
        self.OpenPostPathBtn.clicked.connect(self.OpenPostPathBtnClicked)

    def BlogPathSearchBtnClicked(self):
        config = LoadJsonData()
        path = SearchDir("选择博客文件夹", self)
        if path:
            self.BlogPath.setText(path)
            config["BlogPath"] = path
            SaveJsonData(config)

    def DebugBtnClicked(self):
        config = LoadJsonData()
        if "BlogPath" in config and os.path.exists(config["BlogPath"]):
            originalPath = os.getcwd()
            os.chdir(config["BlogPath"])
            process = subprocess.Popen("hexo clean && hexo g && hexo s --debug", stdout=subprocess.PIPE,
                                       stderr=subprocess.STDOUT, shell=True, stdin=subprocess.PIPE)
            # ShowLogDialogNoExit("执行调试", process)
            # 创建一个线程来实时捕获批处理文件的输出并将其打印到面板上
            thread = threading.Thread(target=ShowLogDialogNoExit, args=("执行调试", process))
            thread.start()
            os.chdir(originalPath)
        else:
            ShowTipDialog("博客文件夹不存在", "错误", self)

    def DeployBtnClicked(self):
        config = LoadJsonData()
        if "BlogPath" in config and os.path.exists(config["BlogPath"]):
            originalPath = os.getcwd()
            os.chdir(config["BlogPath"])
            process = subprocess.Popen(["hexo", "clean", "&&", "hexo", "g", "-d"], stdout=subprocess.PIPE,
                                       stderr=subprocess.STDOUT, shell=True, stdin=subprocess.PIPE)
            ShowLogDialog("部署", process, self)
            os.chdir(originalPath)
        else:
            ShowTipDialog("博客文件夹不存在", "错误", self)

    def DeployPushBtnClicked(self):
        config = LoadJsonData()
        if "BlogPath" in config and os.path.exists(config["BlogPath"]):
            originalPath = os.getcwd()
            os.chdir(config["BlogPath"])
            process = subprocess.Popen(["hexo", "clean", "&&", "hexo", "g", "-d", "&&", "git", "add", ".", "&&", "git",
                                        "status", "&&", "git", "commit", "-m", "backups", "&&", "git", "pull",
                                        "--rebase", "origin", "master", "&&", "git", "push"], stdout=subprocess.PIPE,
                                       stderr=subprocess.STDOUT, shell=True, stdin=subprocess.PIPE)
            ShowLogDialog("部署并上传", process, self)
            os.chdir(originalPath)
        else:
            ShowTipDialog("博客文件夹不存在", "错误", self)

    def OpenBlogPathBtnClicked(self):
        config = LoadJsonData()
        if "BlogPath" in config and os.path.exists(config["BlogPath"]):
            os.startfile(config["BlogPath"])
        else:
            ShowTipDialog("博客文件夹不存在", "错误", self)

    def OpenPostPathBtnClicked(self):
        config = LoadJsonData()
        if "BlogPath" in config and os.path.exists(config["BlogPath"]):
            os.startfile(os.path.join(config["BlogPath"], "source", "_posts"))
        else:
            ShowTipDialog("博客文件夹不存在", "错误", self)
