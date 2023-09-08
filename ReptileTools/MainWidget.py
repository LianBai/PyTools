import datetime
import json
import os
import re
import signal
import sys
import threading
import time
import pandas as pd
import requests
import openpyxl
from PyQt5 import QtGui

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette

from PyQt5.QtWidgets import QMainWindow

from AppUtil import ShowTipDialog, exe_path
from main_ui import Ui_MainWidget


class MainWindow(QMainWindow, Ui_MainWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.app = None
        self.isClose = False
        self.setupUi(self)
        self.DJDHBtn.clicked.connect(self.CreatDJDHData)
        self.SSSQBtn.clicked.connect(self.CreateSSSQData)
        self.StatueButton.clicked.connect(self.ToggleDJDHThread)
        # 创建Event对象
        self.timer_event = threading.Event()
        # 创建线程
        self.timer_thread = threading.Thread(target=self.TimerEvent)
        # 创建一个QPalette对象
        self.palette = QPalette()
        # 设置QLabel的背景颜色为红色
        self.palette.setColor(QPalette.WindowText, Qt.darkGreen)
        # 将QPalette对象应用到QLabel上
        self.StatusLabel.setPalette(self.palette)
        # 设置QLabel的文本
        self.StatusLabel.setText('运行中...')
        self.StatueButton.setText('停止')
        # 启动线程
        self.timer_event.set()
        self.timer_thread.start()

    def show(self):
        super().show()
        savePath = os.path.join(exe_path(), "save")
        if not os.path.exists(savePath):
            os.mkdir(savePath)

    def Init(self, app):
        self.app = app

    def closeEvent(self, a0: QtGui.QCloseEvent):
        self.timer_event.clear()
        self.isClose = True
        pid = os.getpid()
        os.kill(pid, signal.SIGTERM)

    def ToggleDJDHThread(self):
        try:
            if self.timer_event.is_set():
                self.timer_event.clear()
                self.palette.setColor(QPalette.WindowText, Qt.red)
                self.StatusLabel.setPalette(self.palette)
                self.StatusLabel.setText('停止中')
                self.StatueButton.setText('启动')
            else:
                self.timer_event.set()
                self.palette.setColor(QPalette.WindowText, Qt.darkGreen)
                self.StatusLabel.setPalette(self.palette)
                self.StatusLabel.setText('运行中...')
                self.StatueButton.setText('停止')
        except Exception as e:
            ShowTipDialog('错误', f'切换线程失败：{e}', self)

    def CreatDJDHData(self, isHideTip=False):
        try:
            # 发送 HTTP 请求
            url = 'http://xxfb.mwr.cn/hydroSearch/greatRiver'
            response = requests.get(url)

            # 解析 JSON 数据
            data = json.loads(response.text)
            date = data['result']['date']
            result = data['result']['data']

            # 将数据转换为 DataFrame
            df = pd.DataFrame(result)
            df['date'] = date

            # 重命名列名
            df = df.rename(
                columns={'stnm': '站名', 'rz': '水位', 'q': '流量', 'wrz': '警戒水位', 'wq': '警戒流量', 'date': '日期'})

            # 获取当前时间
            now = datetime.datetime.now()
            # 判断文件是否存在，如果不存在就创建表格文件
            filename = f'大江河域_{now.year}-{now.month}-{now.day}-{now.hour}点.xlsx'
            filepath = os.path.join(exe_path(), "save", filename)

            # 将数据写入表格文件
            df.to_excel(filepath, index=False)
            if not isHideTip:
                ShowTipDialog('提示', f'抓取成功\n{filename}', self)
        except Exception as e:
            ShowTipDialog('错误', f'抓取失败：{e}', self)

    def CreateSSSQData(self, isHideTip=False):
        try:
            # 发送 HTTP 请求
            url = 'http://www.cjh.com.cn/sqindex.html'
            response = requests.get(url)
            # 将HTML字符串包装为文件对象
            pattern = r'var sssq = (\[.*?\]);'
            match = re.search(pattern, response.text)
            data = match.group(1)
            # 将JSON数据解析为Python对象
            data = json.loads(data)
            # 将Python对象转换为DataFrame对象
            df = pd.DataFrame(data)

            # 获取当前时间
            now = datetime.datetime.now()
            filename = f"实时水情_{now.year}-{now.month}-{now.day}-{now.hour}点.xlsx"
            filepath = os.path.join(exe_path(), "save", filename)
            # 将DataFrame对象保存到Excel文件中
            df.to_excel(filepath, index=False)
            if not isHideTip:
                ShowTipDialog('提示', f'抓取成功\n{filename}', self)
        except Exception as e:
            ShowTipDialog('错误', f'抓取失败：{e}', self)

    def TimerEvent(self):
        while not self.isClose:
            self.timer_event.wait()
            # 在每天8点5分到14点5分之间执行
            now = time.localtime()
            if now.tm_hour == 8 and 5 <= now.tm_min <= 59 or \
                    8 < now.tm_hour < 14 or \
                    now.tm_hour == 14 and 0 <= now.tm_min <= 5:
                self.CreatDJDHData(True)
            if now.tm_min == 5 and now.tm_sec == 0:
                self.CreateSSSQData(True)
            time.sleep(40)



