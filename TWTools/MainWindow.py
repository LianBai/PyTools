import io
import os
import subprocess
import sys
import requests
import json
import psutil

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QFileDialog, QTextEdit, QApplication, QAction, QMainWindow, QVBoxLayout, \
    QSpacerItem, QSizePolicy
from watchdog.observers import Observer

from FileUtil import OpenPath, MakeLink
from GitBranchHandler import GitBranchHandler
from roommain_ui import Ui_Form
from JsonUtil import SaveJsonData, LoadJsonData
from AppUtil import AutoMultipleLabelFontSize, LogWidget, TipWidget, HideLayout, ShowLayout, \
    ShowTipDialog, GetLayoutHeight, UpdateLayoutHeight

sys.stdout = io.TextIOWrapper(io.BytesIO(), 'utf-8', errors='ignore')
sys.stderr = io.TextIOWrapper(io.BytesIO(), 'utf-8', errors='ignore')

UnKnowDes = "未知"


class MainWindow(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.AppConfigTip = None
        self.event_handler = None
        self.observer = None
        self.logDialog = None
        self.dialog = None
        self.setWindowIcon(QIcon("TWTools.ico"))
        self.setupUi(self)
        self.GitLink.setWordWrap(True)
        self.ResLink.setText(UnKnowDes)
        # region 设置按钮的响应
        self.UpdateBtn.clicked.connect(self.UpdateBtnClicked)
        self.GitUpdateBtn.clicked.connect(self.UpdateGitBranch)
        self.SvnUpdateBtn.clicked.connect(self.UpdateSvnBranch)
        self.ResDevBtn.clicked.connect(self.ResDevBtnClicked)
        self.ResTrunkBtn.clicked.connect(self.ResTruckBtnClicked)
        self.ResReleaseBtn.clicked.connect(self.ResReleaseBtnClicked)
        self.ProPathSearchBtn.clicked.connect(self.ProPathSearchBtnClicked)
        self.SvnPathSearchBtn.clicked.connect(self.SvnPathSearchBtnClicked)
        self.GuideTabelBtn.clicked.connect(self.GuideTabelBtnClicked)
        self.SvnCommitBtn.clicked.connect(self.SvnCommitBtnClicked)
        self.GuideProtobufBtn.clicked.connect(self.GuideProtobufBtnClicked)
        self.OpenProPathBtn.clicked.connect(self.OpenProPathBtnClicked)
        self.OpenSvnPathBtn.clicked.connect(self.OpenSvnPathBtnClicked)
        self.OpenExcelPathBtn.clicked.connect(self.OpenExcelPathBtnClicked)
        self.OpenDevPathBtn.clicked.connect(self.OpenDevPathBtnClicked)
        self.OpenReleasePathBtn.clicked.connect(self.OpenReleasePathBtnClicked)
        self.OpenTrunkPathBtn.clicked.connect(self.OpenTrunkPathBtnClicked)
        self.OpenServerPathBtn.clicked.connect(self.OpenServerPathBtnClicked)
        self.OpenAndroidPath.clicked.connect(self.OpenAndroidPathBtnClicked)
        self.OpenServerBtn.clicked.connect(self.OpenServerBtnClicked)
        self.ExcelOpenServerBtn.clicked.connect(self.ExcelOpenServerBtnClicked)
        self.CloseServerBtn.clicked.connect(self.CloseServerBtnClicked)
        self.OpenProtobufPathBtn.clicked.connect(self.OpenProtobufPathBtnClicked)
        self.HubOpenPro.clicked.connect(self.HubOpenProBtnClicked)
        self.SvnExeSearchBtn.clicked.connect(self.SvnExeSearchBtnClicked)
        self.HubPathSearchBtn.clicked.connect(self.HubSearchBtnClicked)
        self.GroupLayout = [self.InfoLayout, self.BtnLayout, self.ResBtnLayout, self.ServerBtnLayout, self.ConfigLayout,
                            self.ExcelSearhLayout]
        # endregion
        self.menubar = self.menuBar()
        self.AddMenu("基础", self.RefreshBasicMenu)
        self.AddMenu("服务", self.RefreshServerMenu)
        self.AddMenu("配置", self.RefreshConfigMenu)
        self.AddMenu("表格", self.RefreshConfigMenu)

    def InitShow(self):
        config = LoadJsonData()
        if "SvnExePath" in config and os.path.exists(config["SvnExePath"]):
            self.SvnExePath.setText(config["SvnExePath"])
        if "HubExePath" in config and os.path.exists(config["HubExePath"]):
            self.HubPath.setText(config["HubExePath"])
        try:
            self.RefreshBasicMenu()
        except Exception as e:
            ShowTipDialog("错误", f"初始化失败！\n{e}", self)

    def show(self):
        super().show()
        self.InitShow()

    def AddMenu(self, name, func=None):
        action1 = QAction(name, self)
        action1.triggered.connect(func)
        self.menubar.addAction(action1)

    def RefreshBasicMenu(self):
        height = 50
        height += self.RefreshLayoutGroup([self.InfoLayout, self.BtnLayout, self.ResBtnLayout])
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.setMinimumSize(self.width(), height)
        self.setMaximumSize(self.width(), height)
        self.resize(self.width(), height)
        self.update()

    def RefreshServerMenu(self):
        height = 50
        height += self.RefreshLayoutGroup([self.InfoLayout, self.ServerBtnLayout])
        self.setMinimumSize(self.width(), height)
        self.setMaximumSize(self.width(), height)
        self.resize(self.width(), height)
        self.update()

    def RefreshConfigMenu(self):
        height = 40
        height += self.RefreshLayoutGroup([self.ConfigLayout])
        self.setMinimumSize(self.width(), height)
        self.setMaximumSize(self.width(), height)
        self.resize(self.width(), height)
        self.update()

    def RefreshLayoutGroup(self, showLayout):
        height = 0
        for item in self.GroupLayout:
            if item in showLayout:
                height += ShowLayout(item)
            else:
                HideLayout(item)
        return height

    def UpdateGitBranch(self):
        config = LoadJsonData()
        if "ProPath" in config and os.path.exists(config["ProPath"]):
            proPath = config["ProPath"]
            originalPath = os.getcwd()
            self.logDialog = LogWidget(self)
            self.logDialog.show()
            os.chdir(proPath)
            process = self.UpdateGit()
            if process.returncode == 0:
                ShowTipDialog("成功", "GIT更新成功！", self)
            else:
                error = process.stdout.read() or process.stderr.read()
                ShowTipDialog("错误", f"GIT更新失败！\n{error}", self)
            process.wait()
            os.chdir(originalPath)
        else:
            ShowTipDialog("错误","项目目录不存在，请重新设置", self)

    def UpdateSvnBranch(self):
        config = LoadJsonData()

        if "SvnPath" in config and os.path.exists(config["SvnPath"]):
            svnPath = config["SvnPath"]
            originalPath = os.getcwd()
            os.chdir(svnPath)
            self.logDialog = LogWidget(self)
            self.logDialog.show()
            if self.ResLink.text() != UnKnowDes:
                os.chdir(os.path.join(svnPath, self.ResLink.text()))
                process, isSuc = self.UpdateSvn(self.ResLink.text())
                if isSuc:
                    ShowTipDialog("成功", "SVN更新成功！", self)
                else:
                    error = process.stdout.read() or process.stderr.read()
                    ShowTipDialog("错误", f"SVN更新失败！\n{error}", self)
                if process is not None:
                    process.wait()
            else:
                ShowTipDialog("错误", "未设置资源链接，SVN无法更新资源...", self)
            os.chdir(originalPath)
        else:
            ShowTipDialog("错误","SVN目录不存在，请重新设置", self)

    def SwitchResLink(self, resLinkName):
        self.logDialog = LogWidget(self)
        self.logDialog.show()
        self.logDialog.logText.clear()
        self.logDialog.append("开始切换资源链接...")
        config = LoadJsonData()
        # 获取项目目录
        proPathDes = config["ProPath"]
        proPathDes = proPathDes.replace('/', '\\')
        self.logDialog.append("项目目录：" + proPathDes)
        # 获取SVN目录
        svnPath = os.path.join(config["SvnPath"], resLinkName)
        self.logDialog.append("SVN目录：" + svnPath)
        process, isSuc = self.UpdateSvn(resLinkName)
        if process is not None:
            process.wait()
        if isSuc:
            try:
                # 获取Unity工程目录
                proAssetsPath = os.path.join(proPathDes, "client", "client", "Assets")
                # 删除Unity工程中的文件夹
                self.logDialog.append("正在删除 Unity 工程中的文件夹...")
                MakeLink(os.path.join(svnPath, "_Scenes"), os.path.join(proAssetsPath, "_Scenes"), self.logDialog)
                MakeLink(os.path.join(svnPath, "_Icons"), os.path.join(proAssetsPath, "_Icons"), self.logDialog)

                # 创建资源目录软链接
                self.logDialog.append("正在创建资源目录软链接...")
                root_dir = os.path.join(svnPath, "_Resources")
                for dirname in os.listdir(root_dir):
                    src_dir = os.path.join(root_dir, dirname)
                    if os.path.isdir(src_dir):
                        dst_dir = os.path.join(proAssetsPath, "_Resources", dirname)
                        MakeLink(src_dir, dst_dir, self.logDialog)

                # 创建美术目录软链接
                self.logDialog.append("正在创建美术目录软链接...")
                root_dir = os.path.join(svnPath, "_Art")
                for dirname in os.listdir(root_dir):
                    src_dir = os.path.join(root_dir, dirname)
                    if os.path.isdir(src_dir):
                        dst_dir = os.path.join(proAssetsPath, "_Art", dirname)
                        MakeLink(src_dir, dst_dir, self.logDialog)

                # 刷新资源链接
                self.RefreshResLink()
                self.logDialog.append("资源链接切换成功")
                ShowTipDialog("成功", "资源链接切换成功！", self)
            except Exception as e:
                ShowTipDialog("错误", f"资源链接切换失败！\n{e}", self)
        self.logDialog.exec()

    def UpdateSvn(self, resLinkName):
        config = LoadJsonData()
        svnPath = config["SvnPath"]
        originalPath = os.getcwd()
        if os.path.exists(os.path.join(svnPath, resLinkName)):
            os.chdir(os.path.join(svnPath, resLinkName))
        self.logDialog.append(f"开始更新svn的{resLinkName}资源...")
        try:
            # 执行svn命令
            subprocess.check_output('svn --version', shell=True)
            if os.path.exists(os.path.join(svnPath, resLinkName, ".svn")):
                process = subprocess.Popen(['svn', 'update'], stdout=subprocess.PIPE,
                                           stderr=subprocess.STDOUT, text=True, stdin=subprocess.PIPE)
                isSuc = self.CommunicateProcessLog("svn", process)
            else:
                os.makedirs(os.path.join(svnPath, resLinkName))
                os.chdir(os.path.join(svnPath, resLinkName))
                process = subprocess.Popen(['svn', 'checkout', f"svn://10.26.15.200/svn/{resLinkName}",
                                            os.path.join(svnPath, resLinkName)], stdout=subprocess.PIPE,
                                           stderr=subprocess.STDOUT, text=True, stdin=subprocess.PIPE)
                isSuc = self.ProcessLog(process, "utf-8")

        except subprocess.CalledProcessError:
            if "SvnExePath" in config and os.path.exists(config["SvnExePath"]):
                if os.path.exists(os.path.join(svnPath, resLinkName, ".svn")):
                    process = subprocess.Popen([config["SvnExePath"], '/command:update',
                                                f"/path:{os.path.join(svnPath, resLinkName)}", "/closeonend:0"],
                                               stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
                                               stdin=subprocess.PIPE)
                    isSuc = self.CommunicateProcessLog("svn", process)
                else:
                    os.makedirs(os.path.join(svnPath, resLinkName))
                    os.chdir(os.path.join(svnPath, resLinkName))
                    process = subprocess.Popen([config["SvnExePath"], '/command:checkout',
                                                f"/url:svn://10.26.15.200/svn/{resLinkName}",
                                                f"/path:{os.path.join(svnPath, resLinkName)}"],
                                               stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
                                               stdin=subprocess.PIPE)
                    isSuc = self.CommunicateProcessLog("svn", process)

            else:
                process = None
                ShowTipDialog("错误", "请先设置TortoiseProc.exe路径！", self)
        os.chdir(originalPath)
        return process, isSuc

    def UpdateGit(self):
        self.logDialog.append("开始更新代码...")
        process = subprocess.Popen(['git', 'pull', "--rebase", "--autostash"], stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT, text=True, stdin=subprocess.PIPE)
        self.CommunicateProcessLog("git", process)
        return process

    def RefreshSvnPath(self):
        config = LoadJsonData()
        proPathDes = self.ProPath.text()
        # 将指定路径的文件夹设置为当前工作目录
        os.chdir(proPathDes)
        # 获取当前文件夹路径
        current_dir = os.getcwd()
        # 判断当前文件夹中是否有名为"svn"的文件夹
        svn_dir = os.path.join(current_dir, "svn")
        if not os.path.exists(svn_dir):
            # 获取当前文件夹的同级别文件夹路径
            parent_dir = os.path.dirname(current_dir)
            # 判断同级别文件夹中是否有名为"svn"的文件夹
            svn_dir = os.path.join(parent_dir, "svn")
            if not os.path.exists(svn_dir):
                # 如果不存在，则在当前文件夹下创建一个名为"svn"的文件夹
                os.mkdir("svn")
        self.SvnPath.setText(svn_dir)
        config["SvnPath"] = svn_dir
        SaveJsonData(config)

    def RefreshResLink(self):
        self.RefreshGitBranch()
        config = LoadJsonData()
        if "ProPath" in config and os.path.exists(config["ProPath"]):
            link_path = config["ProPath"] + "/client/client/Assets/_Icons"
            # print("路径为：" + link_path)
            # 检查路径是否是软链
            if os.path.isdir(link_path) and os.path.realpath(link_path) != link_path:
                # 获取软链的原路径
                real_path = os.path.realpath(link_path)
                # print("软链的原路径为：" + real_path)
                # 获取原路径的上一级路径
                parent_path = os.path.dirname(real_path)
                # 获取上一级路径的最后一个文件夹的名字
                second_last_folder_name = os.path.basename(os.path.normpath(parent_path))
                # 输出软链的原路径
                self.ResLink.setText(second_last_folder_name)
                return parent_path
            else:
                self.ResLink.setText(UnKnowDes)
                return None

    def BatProcess(self, name, batPath):
        originalPath = os.getcwd()
        proPath = os.path.dirname(batPath)
        os.chdir(proPath)
        self.logDialog = LogWidget(self)
        self.logDialog.show()
        self.logDialog.logText.clear()
        self.logDialog.append("开始" + name)
        # 执行批处理文件
        process = subprocess.Popen(os.path.abspath(batPath), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True,
                                   stdin=subprocess.PIPE)
        self.ProcessLog(process)
        process.wait()
        os.chdir(originalPath)

    def SvnCommitBtnClicked(self):
        config = LoadJsonData()
        if "SvnExePath" in config and os.path.exists(config["SvnExePath"]):
            tortoise_path = config["SvnExePath"]
            svn_path = self.RefreshResLink()
            # 执行TortoiseProc.exe提交命令
            command = f'"{tortoise_path}" /command:commit /path:"{svn_path}" /closeonend:2'
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True,
                                       stdin=subprocess.PIPE)

            # 获取TortoiseProc.exe提交命令输出
            stdout, stderr = process.communicate()

            # 判断TortoiseProc.exe提交命令执行结果
            if process.returncode == 0:
                # TortoiseProc.exe提交命令执行成功
                log = QTextEdit()
                log.append("TortoiseProc.exe commit completed")
                log.append(stdout.decode())
            else:
                # TortoiseProc.exe提交命令执行失败
                log = QTextEdit()
                log.append("TortoiseProc.exe commit failed")
                log.append("Error message:")
                log.append(stderr.decode())
        else:
            self.SvnExeSearchBtnClicked()

    def ProcessLog(self, process, encoding="gbk"):
        try:
            while True:
                output = process.stdout.readline().decode(encoding, errors="ignore").strip()

                if output:
                    self.logDialog.append(output)
                    QApplication.processEvents()  # 处理事件循环，确保日志能够及时显示
                    # 刷新标准输入缓冲区
                    process.stdin.flush()
                if process.poll() is not None:
                    self.logDialog.append("执行完成")
                    break
                # 向子进程的标准输入中写入一个空行，跳过pause命令
                process.stdin.write(b"\n")
                # 刷新标准输入缓冲区
                process.stdin.flush()
            # 判断批处理文件执行结果
            if process.returncode == 0:
                self.dialog = TipWidget(self.logDialog)
                self.dialog.show()
                self.dialog.label.setText("执行成功")
                self.dialog.setWindowTitle("成功")
                return True
            else:
                ShowTipDialog("错误", "执行失败", self)
                QApplication.processEvents()  # 处理事件循环，确保日志能够及时显示
                return False
        except Exception as e:
            ShowTipDialog("错误", f"执行失败{e}", self)
            return False

    def CommunicateProcessLog(self, name, process):
        output, error = process.communicate()
        while True:
            if output:
                self.logDialog.append(output)
                QApplication.processEvents()  # 处理事件循环，确保日志能够及时显示
                # 刷新标准输入缓冲区
                if not process.stdin.closed:
                    process.stdin.flush()
            if process.poll() is not None:
                break
            # 刷新标准输入缓冲区
            if not process.stdin.closed:
                process.stdin.flush()
        if process.returncode == 0:
            self.logDialog.append(f"{name}更新完成")
            return True
        else:
            self.logDialog.append(f"{name}更新失败：{error}")
            return False

    def OpenHubPro(self, proPath):
        hubPort = 0
        # 查找 Unity Hub 进程
        for proc in psutil.process_iter(['pid', 'name']):
            if proc.info['name'] == 'Unity Hub.exe':
                # 获取 Unity Hub 进程的详细信息
                proc_info = proc.as_dict(attrs=['pid', 'connections'])
                # 查找正在使用的端口号
                for conn in proc_info['connections']:
                    if conn.status == 'LISTEN':
                        hubPort = conn.laddr.port
        if hubPort == 0:
            self.OpenUnityHub()
            return

        # Unity Hub REST API 的基本 URL
        hub_api_url = f"http://localhost:{hubPort}/api/v1"
        # 规范化路径，消除路径格式的差异
        proPath = os.path.normcase(proPath)
        # 获取 Unity Hub 中的所有项目
        try:
            response = requests.get(f"{hub_api_url}/projects")
            response.raise_for_status()
            projects = json.loads(response.content)
        except requests.exceptions.RequestException as e:
            ShowTipDialog("错误", f"无法获取 Unity Hub 中的项目：{e}", self)
            self.OpenUnityHub()
            return
        # 找到要打开的项目
        project = next((p for p in projects if os.path.normcase(p["path"]) == proPath), None)
        if project:
            # 打开项目
            try:
                response = requests.post(f"{hub_api_url}/projects/{project['id']}/open")
                response.raise_for_status()
                ShowTipDialog("成功", f"成功打开项目 {project['name']}", self)
            except requests.exceptions.RequestException as e:
                ShowTipDialog("错误", f"无法打开项目 {project['name']}：{e}", self)
                self.OpenUnityHub()
        else:
            self.OpenUnityHub()

    def OpenUnityHub(self):
        # 如果 Unity Hub 中不存在要打开的项目，则尝试启动 Unity Hub 进程并打开指定的项目
        config = LoadJsonData()
        if "HubExePath" in config and os.path.exists(config["HubExePath"]):
            hub_path = config["HubExePath"]
            try:
                subprocess.Popen([hub_path])
            except Exception as e:
                ShowTipDialog("错误", f"无法启动 Unity Hub 进程：{e}", self)
        else:
            ShowTipDialog("错误", "请先设置Unity Hub.exe路径！", self)

    def RefreshGitBranch(self):
        config = LoadJsonData()
        path = config["ProPath"]
        original = os.getcwd()
        os.chdir(path)
        if os.path.exists(path) and os.path.exists(os.path.join(path, ".git")):
            result = subprocess.run(["git", "rev-parse", "--abbrev-ref", "HEAD"], stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT, shell=True,
                                    stdin=subprocess.PIPE).stdout.decode("utf-8").strip()
            self.GitLink.setText(result[result.rfind("/")+1:])
        else:
            self.GitLink.setText(UnKnowDes)
        AutoMultipleLabelFontSize(self.GitLink)
        os.chdir(original)

    def RefreshGitSwitch(self):
        config = LoadJsonData()
        if "ProPath" in config and os.path.exists(config["ProPath"]) and os.path.exists(os.path.join(config["ProPath"], ".git")):
            if self.observer is not None:
                self.observer.stop()
            self.observer = Observer()
            path = config["ProPath"]
            self.event_handler = GitBranchHandler(path, self.RefreshGitBranch)
            self.observer.schedule(self.event_handler, path, recursive=False)
            self.observer.start()

    def RefreshBranch(self):
        self.RefreshGitBranch()
        self.RefreshResLink()

    # region 菜单栏按钮的响应

    def UpdateBtnClicked(self):
        config = LoadJsonData()
        if "ProPath" in config and os.path.exists(config["ProPath"]):
            proPath = config["ProPath"]
            if "SvnPath" in config and os.path.exists(config["SvnPath"]):
                svnPath = config["SvnPath"]
                originalPath = os.getcwd()
                os.chdir(proPath)
                self.logDialog = LogWidget(self)
                self.logDialog.show()
                process = self.UpdateGit()
                process.wait()
                if self.ResLink.text() != UnKnowDes:
                    self.logDialog.append(f"开始更新svn的{self.ResLink.text()}资源...")
                    os.chdir(os.path.join(svnPath, self.ResLink.text()))
                    process, isSuc = self.UpdateSvn(self.ResLink.text())
                    if isSuc:
                        ShowTipDialog("成功", "更新完成！", self)
                    else:
                        error = process.stdout.read() or process.stderr.read()
                        ShowTipDialog("错误", f"SVN更新失败！\n{error}", self)
                    if process is not None:
                        process.wait()
                else:
                    ShowTipDialog("错误", "未设置资源链接，SVN无法更新资源...", self)
                os.chdir(originalPath)
            else:
                ShowTipDialog("错误", "SVN目录不存在，请重新设置", self)
        else:
            ShowTipDialog("错误", "项目目录不存在，请重新设置", self)

    def ResDevBtnClicked(self):
        self.SwitchResLink("dev")

    def ResTruckBtnClicked(self):
        self.SwitchResLink("trunk")

    def ResReleaseBtnClicked(self):
        self.SwitchResLink("release")

    def GuideTabelBtnClicked(self):
        config = LoadJsonData()
        if "ProPath" in config and os.path.exists(config["ProPath"]):
            path = os.path.join(config["ProPath"], "client", "tables")
            originalPath = os.getcwd()
            os.chdir(path)
            exePath = os.path.join(path, "build.bat")
            subprocess.Popen(exePath)
            os.chdir(originalPath)
        else:
            ShowTipDialog("错误", "项目目录不存在，请重新设置", self)

    def GuideProtobufBtnClicked(self):
        proPathDes = self.ProPath.text()
        self.BatProcess("导入协议", os.path.join(proPathDes, "client", "netmsg", "build.bat"))

    def OpenProPathBtnClicked(self):
        config = LoadJsonData()
        OpenPath(config["ProPath"], self)

    def OpenSvnPathBtnClicked(self):
        config = LoadJsonData()
        OpenPath(config["SvnPath"], self)

    def SvnExeSearchBtnClicked(self):
        config = LoadJsonData()
        self.dialog = QFileDialog(self, "选择TortoiseProc.exe软件", "./")
        self.dialog.setFileMode(QFileDialog.ExistingFile)
        self.dialog.setNameFilter("Executable files (TortoiseProc.exe)")
        if self.dialog.exec() == QDialog.Accepted:
            file_path = self.dialog.selectedFiles()[0]
            self.SvnExePath.setText(file_path)
            config["SvnExePath"] = file_path
            SaveJsonData(config)

    def HubSearchBtnClicked(self):
        config = LoadJsonData()
        self.dialog = QFileDialog(self, "选择Unity Hub.exe软件", "./")
        self.dialog.setFileMode(QFileDialog.ExistingFile)
        self.dialog.setNameFilter("Executable files (*.exe)")
        if self.dialog.exec() == QDialog.Accepted:
            file_path = self.dialog.selectedFiles()[0]
            self.HubPath.setText(file_path)
            config["HubExePath"] = file_path
            SaveJsonData(config)

    def OpenExcelPathBtnClicked(self):
        config = LoadJsonData()
        path = os.path.join(config["ProPath"], "client", "tables", "excel")
        OpenPath(path, self)

    def OpenDevPathBtnClicked(self):
        config = LoadJsonData()
        path = os.path.join(config["SvnPath"], "dev")
        OpenPath(path, self)

    def OpenReleasePathBtnClicked(self):
        config = LoadJsonData()
        path = os.path.join(config["SvnPath"], "release")
        OpenPath(path, self)

    def OpenTrunkPathBtnClicked(self):
        config = LoadJsonData()
        path = os.path.join(config["SvnPath"], "trunk")
        OpenPath(path, self)

    def OpenServerPathBtnClicked(self):
        config = LoadJsonData()
        path = os.path.join(config["ProPath"], "server", "bin")
        OpenPath(path, self)

    def OpenAndroidPathBtnClicked(self):
        config = LoadJsonData()
        path = os.path.join(config["ProPath"], "client", "sdk")
        OpenPath(path, self)

    @staticmethod
    def OpenServerBtnClicked():
        config = LoadJsonData()
        path = os.path.join(config["ProPath"], "server", "bin")
        originalPath = os.getcwd()
        os.chdir(path)
        exePath = os.path.join(path, "启动.bat")
        subprocess.call(exePath)
        os.chdir(originalPath)

    @staticmethod
    def ExcelOpenServerBtnClicked():
        config = LoadJsonData()
        path = os.path.join(config["ProPath"], "server", "bin")
        originalPath = os.getcwd()
        os.chdir(path)
        exePath = os.path.join(path, "导表+启动.bat")
        subprocess.call(exePath)
        os.chdir(originalPath)

    @staticmethod
    def CloseServerBtnClicked():
        config = LoadJsonData()
        path = os.path.join(config["ProPath"], "server", "bin")
        originalPath = os.getcwd()
        os.chdir(path)
        exePath = os.path.join(path, "关闭.bat")
        subprocess.call(exePath)
        os.chdir(originalPath)

    def OpenProtobufPathBtnClicked(self):
        config = LoadJsonData()
        path = os.path.join(config["ProPath"], "client", "netmsg", "protobuf")
        OpenPath(path, self)

    def HubOpenProBtnClicked(self):
        config = LoadJsonData()
        if "ProPath" in config and os.path.exists(config["ProPath"]):
            clientPath = os.path.join(config["ProPath"], "client", "client")
            if "HubExePath" in config and os.path.exists(config["HubExePath"]):
                hub_path = config["HubExePath"]
                self.OpenHubPro(clientPath)
            else:
                ShowTipDialog("错误", "请先设置Unity Hub.exe路径！", self)
        else:
            ShowTipDialog("错误", "项目目录不存在，请重新设置", self)

    def ProPathSearchBtnClicked(self):
        config = LoadJsonData()
        self.dialog = QFileDialog(self, "选择TW项目文件夹", "./")
        self.dialog.setFileMode(QFileDialog.Directory)
        if self.dialog.exec() == QFileDialog.Accepted:
            folder_path = self.dialog.selectedFiles()[0]
            self.ProPath.setText(folder_path)
            config["ProPath"] = folder_path
            SaveJsonData(config)
            self.RefreshSvnPath()
        self.RefreshGitSwitch()

    def SvnPathSearchBtnClicked(self):
        config = LoadJsonData()
        self.dialog = QFileDialog(self, "选择SVN项目文件夹", "./")
        self.dialog.setFileMode(QFileDialog.Directory)
        if self.dialog.exec() == QDialog.Accepted:
            folder_path = self.dialog.selectedFiles()[0]
            self.ProPath.setText(folder_path)
            config["SvnPath"] = folder_path
            self.RefreshSvnPath()
            SaveJsonData(config)

    # endregion
