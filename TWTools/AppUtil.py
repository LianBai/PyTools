import os

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFontMetrics, QIcon, QTextCursor
from PyQt5.QtWidgets import QDialog, QFileDialog

from AppConfig_ui import Ui_AppConfig
from JsonUtil import LoadJsonData, SaveJsonData
from LogWidget_ui import Ui_LogWidget
from TipWidget_ui import Ui_TipWidget


def AutoMultipleLabelFontSize(label):
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
        rect = fm.boundingRect(label.rect(), Qt.TextWordWrap, label.text())
        if rect.width() <= label.width() and rect.height() <= label.height():
            low = mid + 1
        else:
            high = mid - 1

    # 设置QLabel的字体
    font.setPointSize(high)
    label.setFont(font)


def AutoSingleLabelFontSize(label):
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


def GetLayoutHeight(layout):
    return layout.sizeHint().height()


def HideLayout(layout):
    # 获取布局中的所有组件，并隐藏它们
    for i in range(layout.count()):
        widget = layout.itemAt(i).widget()
        if widget:
            widget.hide()

    # 禁用布局
    layout.update()


def ShowLayout(layout):
    # 获取布局中的所有组件，并隐藏它们
    for i in range(layout.count()):
        widget = layout.itemAt(i).widget()
        if widget:
            widget.show()

    # 禁用布局
    layout.setEnabled(True)
    layout.update()
    return GetLayoutHeight(layout)


def UpdateLayoutHeight(layout, height):
    rect = layout.geometry()
    rect.setHeight(height)
    layout.setGeometry(rect)
    layout.update()


class TipWidget(QDialog, Ui_TipWidget):
    def __init__(self, parent=None):
        super(TipWidget, self).__init__(parent)
        self.setWindowIcon(QIcon("TWTools.ico"))
        self.setupUi(self)


class LogWidget(QDialog, Ui_LogWidget):
    def __init__(self, parent=None):
        super(LogWidget, self).__init__(parent)
        self.setWindowIcon(QIcon("TWTools.ico"))
        self.setupUi(self)

    def append(self, msg, is_red=False):
        # 向日志窗口添加消息
        self.logText.appendPlainText(msg)
        self.logText.moveCursor(QTextCursor.End)
        if is_red:
            self.logText.setTextColor(Qt.red)
        self.logText.moveCursor(QTextCursor.End)


class ConfigAppWidget(QDialog, Ui_AppConfig):
    def __init__(self, parent=None):
        super(ConfigAppWidget, self).__init__(parent)
        self.dialog = None
        self.setWindowIcon(QIcon("TWTools.ico"))
        self.setupUi(self)
        config = LoadJsonData()
        if "SvnExePath" in config and os.path.exists(config["SvnExePath"]):
            self.SvnExePath.setText(config["SvnExePath"])
        if "HubExePath" in config and os.path.exists(config["HubExePath"]):
            self.HubPath.setText(config["HubExePath"])
        self.SvnExeSearchBtn.clicked.connect(self.SvnExeSearchBtnClicked)
        self.HubPathSearchBtn.clicked.connect(self.HubSearchBtnClicked)

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


def ShowTipDialog(title, content, parent=None):
    dialog = TipWidget(parent)
    dialog.show()
    dialog.label.setText(content)
    AutoMultipleLabelFontSize(dialog.label)
    dialog.setWindowTitle(title)
