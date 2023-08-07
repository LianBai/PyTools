import io
import os
import subprocess
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QTextCursor, QFontMetrics
from PyQt5.QtWidgets import QDialog, QWidget, QFileDialog, QTextEdit, QApplication
from watchdog.observers import Observer

from FileUtil import OpenPath, MakeLink
from GitBranchHandler import GitBranchHandler
from roommain_ui import Ui_Form
from JsonUtil import SaveJsonData, LoadJsonData
from TipWidget_ui import Ui_TipWidget
from LogWidget_ui import Ui_LogWidget

sys.stdout = io.TextIOWrapper(io.BytesIO(), 'utf-8', errors='ignore')
sys.stderr = io.TextIOWrapper(io.BytesIO(), 'utf-8', errors='ignore')

UnKnowDes = "未知"


class TipWidget(QDialog, Ui_TipWidget):
    def __init__(self, parent=None):
        super(TipWidget, self).__init__(parent)
        self.setWindowIcon(QIcon("TWTools.ico"))
        self.setupUi(self)


class LogDialog(QDialog, Ui_LogWidget):
    def __init__(self, parent=None):
        super(LogDialog, self).__init__(parent)
        self.setWindowIcon(QIcon("TWTools.ico"))
        self.setupUi(self)

    def append(self, msg, is_red=False):
        # 向日志窗口添加消息
        self.logText.appendPlainText(msg)
        self.logText.moveCursor(QTextCursor.End)
        if is_red:
            self.logText.setTextColor(Qt.red)
        self.logText.moveCursor(QTextCursor.End)


class MainWindow(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.event_handler = None
        self.observer = None
        self.logDialog = None
        self.dialog = None
        self.setWindowIcon(QIcon("TWTools.ico"))
        self.setupUi(self)
        self.GitLink.setWordWrap(True)
        self.ResLink.setText(UnKnowDes)
        self.UpdateBtn.clicked.connect(self.UpdateBtnClicked)
        self.ResDevBtn.clicked.connect(self.ResDevBtnClicked)
        self.ResTrunkBtn.clicked.connect(self.ResTruckBtnClicked)
        self.ResReleaseBtn.clicked.connect(self.ResReleaseBtnClicked)
        self.ProPathSearchBtn.clicked.connect(self.ProPathSearchBtnClicked)
        self.SvnPathSearchBtn.clicked.connect(self.SvnPathSearchBtnClicked)
        self.SvnExeSearchBtn.clicked.connect(self.SvnExeSearchBtnClicked)
        self.ResLinkRefBtn.clicked.connect(self.RefreshResLink)
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

    def OnWindowActivate(self, hwnd, msg, wparam, lparam):
        self.RefreshGitBranch()

    def UpdateBtnClicked(self):
        config = LoadJsonData()
        if "ProPath" in config and os.path.exists(config["ProPath"]):
            proPath = config["ProPath"]
            if "SvnPath" in config and os.path.exists(config["SvnPath"]):
                svnPath = config["SvnPath"]
                originalPath = os.getcwd()
                os.chdir(proPath)
                self.logDialog = LogDialog(self)
                self.logDialog.show()
                process = self.UpdateGit()
                process.wait()
                if self.ResLink.text() != UnKnowDes:
                    self.logDialog.append(f"开始更新svn的{self.ResLink.text()}资源...")
                    os.chdir(os.path.join(svnPath, self.ResLink.text()))
                    process, isSuc = self.UpdateSvn(self.ResLink.text())
                    if process is not None:
                        process.wait()
                else:
                    self.logDialog.append("未设置资源链接，SVN无法更新资源...")

                os.chdir(originalPath)
            else:
                self.ShowTipDialog("错误","SVN目录不存在，请重新设置")
        else:
            self.ShowTipDialog("错误","项目目录不存在，请重新设置")

    def ResDevBtnClicked(self):
        self.SwitchResLink("dev")

    def ResTruckBtnClicked(self):
        self.SwitchResLink("trunk")

    def ResReleaseBtnClicked(self):
        self.SwitchResLink("release")

    def SwitchResLink(self, resLinkName):
        self.logDialog = LogDialog(self)
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
            self.ShowTipDialog("成功", "资源链接切换成功！")
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
                self.ShowTipDialog("错误", "请先设置TortoiseProc.exe路径！")
        os.chdir(originalPath)
        return process, isSuc

    def UpdateGit(self):
        self.logDialog.append("开始更新代码...")
        process = subprocess.Popen(['git', 'pull', "--rebase", "--autostash"], stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT, text=True, stdin=subprocess.PIPE)
        self.CommunicateProcessLog("git", process)
        return process

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

    def GuideTabelBtnClicked(self):
        proPathDes = self.ProPath.text()
        self.BatProcess("导入表格", os.path.join(proPathDes, "client", "tables", "build.bat"))

    def GuideProtobufBtnClicked(self):
        proPathDes = self.ProPath.text()
        self.BatProcess("导入协议", os.path.join(proPathDes, "client", "netmsg", "build.bat"))

    def BatProcess(self, name, batPath):
        originalPath = os.getcwd()
        proPath = os.path.dirname(batPath)
        os.chdir(proPath)
        self.logDialog = LogDialog(self)
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
                self.ShowTipDialog("错误", "执行失败")
                QApplication.processEvents()  # 处理事件循环，确保日志能够及时显示
                return False
        except Exception as e:
            self.ShowTipDialog("错误", f"执行失败{e}")
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

    def OpenProPathBtnClicked(self):
        config = LoadJsonData()
        OpenPath(config["ProPath"], self)

    def OpenSvnPathBtnClicked(self):
        config = LoadJsonData()
        OpenPath(config["SvnPath"], self)

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

    def ShowTipDialog(self, title, content):
        self.dialog = TipWidget(self)
        self.dialog.show()
        self.dialog.label.setText(content)
        self.dialog.setWindowTitle(title)

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
            self.GitLink.setText(result)
        else:
            self.GitLink.setText(UnKnowDes)
        self.AutoLabelFontSize(self.GitLink)
        os.chdir(original)

    @staticmethod
    def AutoLabelFontSize(label):
        # 创建一个QFont对象
        font = label.font()
        # 计算字体大小的范围
        fm = QFontMetrics(font)
        min_size = 1
        max_size = 20
        # 二分查找适应的字体大小
        low, high = min_size, max_size
        while low <= high:
            mid = (low + high) // 2
            font.setPointSize(mid)
            fm = QFontMetrics(font)
            rect = fm.boundingRect(label.text())
            if rect.width() <= label.width():
                low = mid + 1
            else:
                high = mid - 1

        # 设置QLabel的字体
        font.setPointSize(high)
        label.setFont(font)

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



