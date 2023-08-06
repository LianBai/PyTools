import io
import os
import subprocess
import sys
import threading

from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QIcon

from WidgetMain import Ui_MainWidget
from FileUtil import SearchDir
from JsonUtil import LoadConfigJsonData, SaveConfigJsonData
from TipUtil import ShowTipDialog, ShowLogDialog, ShowLogDialogNoExit
from CreatePost import ShowCreatePostsDialog

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
        self.CreatPostBtn.clicked.connect(self.CreatPostBtnClicked)

    def BlogPathSearchBtnClicked(self):
        config = LoadConfigJsonData()
        path = SearchDir("选择博客文件夹", self)
        if path:
            self.BlogPath.setText(path)
            config["BlogPath"] = path
            SaveConfigJsonData(config)

    def DebugBtnClicked(self):
        config = LoadConfigJsonData()
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
        config = LoadConfigJsonData()
        if "BlogPath" in config and os.path.exists(config["BlogPath"]):
            originalPath = os.getcwd()
            os.chdir(config["BlogPath"])
            process = subprocess.Popen("hexo clean && hexo g -d", stdout=subprocess.PIPE,
                                       stderr=subprocess.STDOUT, shell=True, stdin=subprocess.PIPE)
            ShowLogDialog("部署", process, self)
            os.chdir(originalPath)
        else:
            ShowTipDialog("博客文件夹不存在", "错误", self)

    def DeployPushBtnClicked(self):
        config = LoadConfigJsonData()
        if "BlogPath" in config and os.path.exists(config["BlogPath"]):
            originalPath = os.getcwd()
            os.chdir(config["BlogPath"])
            # 检查是否有修改
            status = subprocess.check_output(['git', 'status', '--porcelain'])
            if status:
                # 有修改，执行commit和push命令
                cmd = ("hexo clean && hexo g -d && git add . && git commit -m 'backups' && git pull --rebase origin "
                       "master && git push")
            else:
                # 没有修改，只执行clean和generate命令
                cmd = "hexo clean && hexo g -d"
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True,
                                       stdin=subprocess.PIPE)
            ShowLogDialog("部署并上传", process, self)
            os.chdir(originalPath)
        else:
            ShowTipDialog("博客文件夹不存在", "错误", self)

    def OpenBlogPathBtnClicked(self):
        config = LoadConfigJsonData()
        if "BlogPath" in config and os.path.exists(config["BlogPath"]):
            os.startfile(config["BlogPath"])
        else:
            ShowTipDialog("博客文件夹不存在", "错误", self)

    def OpenPostPathBtnClicked(self):
        config = LoadConfigJsonData()
        if "BlogPath" in config and os.path.exists(config["BlogPath"]):
            os.startfile(os.path.join(config["BlogPath"], "source", "_posts"))
        else:
            ShowTipDialog("博客文件夹不存在", "错误", self)

    def CreatPostBtnClicked(self):
        config = LoadConfigJsonData()
        if "BlogPath" in config and os.path.exists(config["BlogPath"]):
            ShowCreatePostsDialog(self)
        else:
            ShowTipDialog("博客文件夹不存在", "错误", self)
