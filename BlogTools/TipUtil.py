import io
import os
import sys
import subprocess

from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QTextCursor
from PySide6.QtWidgets import QDialog, QApplication

from LogWidget import Ui_LogWidget
from TipWidget import Ui_TipWidget
from CreatePostWidget import Ui_CreatePostsForm

sys.stdout = io.TextIOWrapper(io.BytesIO(), 'utf-8', errors='ignore')
sys.stderr = io.TextIOWrapper(io.BytesIO(), 'utf-8', errors='ignore')


class TipWidget(QDialog, Ui_TipWidget):
    def __init__(self, parent=None):
        super(TipWidget, self).__init__(parent)
        self.setWindowIcon(QIcon("TWTools.ico"))
        self.setupUi(self)

    def ShowTip(self, msg, title="提示"):
        self.setWindowTitle(title)
        self.label.setText(msg)


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


def ShowTipDialog(msg, title="提示", parent=None):
    tip = TipWidget(parent)
    tip.ShowTip(msg, title)
    tip.exec()


def ShowLogDialog(nameDes, process, parent=None, encoding="utf-8"):
    log = LogDialog(parent)
    log.show()
    log.append(f"开始执行：{nameDes}")
    try:
        while True:
            output = process.stdout.readline().decode(encoding, errors="ignore").strip()
            # output, error = process.communicate()
            if output:
                log.append(output)
                QApplication.processEvents()  # 处理事件循环，确保日志能够及时显示
                # 刷新标准输入缓冲区
                process.stdin.flush()
            if process.poll() is not None:
                log.append("执行完成")
                break
            # 向子进程的标准输入中写入一个空行，跳过pause命令
            # process.stdin.write(b"\n")
            # 刷新标准输入缓冲区
            process.stdin.flush()
        # 判断批处理文件执行结果
        if process.returncode == 0:
            ShowTipDialog(f"执行{nameDes}成功", "成功", log)
        else:
            ShowTipDialog(f"执行{nameDes}失败", "错误", log)
            QApplication.processEvents()  # 处理事件循环，确保日志能够及时显示
    except Exception as e:
        ShowTipDialog(f"执行{nameDes}失败{e}", "错误", log)
    log.exec()


def ShowLogDialogNoExit(nameDes, process, parent=None, encoding="utf-8"):
    log = LogDialog(parent)
    log.show()
    log.append(f"开始执行：{nameDes}")
    try:
        while True:
            output = process.stdout.readline().decode(encoding, errors='ignore').strip()
            if not output:
                break
            log.append(output)
    except Exception as e:
        ShowTipDialog(f"执行{nameDes}失败{e}", "错误", log)
    log.exec()
