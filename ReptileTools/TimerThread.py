import datetime
import json
import os
import re
import time

import pandas as pd
import requests
from PyQt5.QtCore import QThread, QTimer, pyqtSignal, Qt

from AppUtil import ShowTipDialog, exe_path


class TimerThread(QThread):
    tick = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.timer = QTimer(self)
        self.timer.setTimerType(Qt.PreciseTimer)
        self.timer.timeout.connect(self.tick.emit)

    def run(self):
        self.timer.start(30000)
        self.exec_()


def CreatDJDHData(isHideTip=False, parent=None):
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
            ShowTipDialog('提示', f'抓取成功\n{filename}', parent)
        print(f"抓取成功: \n{filename}")
    except Exception as e:
        ShowTipDialog('错误', f'抓取失败：{e}', parent)


def CreateSSSQData(isHideTip=False, parent=None):
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
            ShowTipDialog('提示', f'抓取成功\n{filename}', parent)
        print(f"抓取成功: \n{filename}")
    except Exception as e:
        ShowTipDialog('错误', f'抓取失败：{e}', parent)


def TimerEvent():
    # 在每天8点5分到14点5分之间执行
    while True:
        now = time.localtime()
        if (now.tm_hour == 8 and now.tm_min == 5) or (now.tm_hour == 14 and now.tm_min == 5):
            CreatDJDHData(True)
        if now.tm_min == 21:
            CreateSSSQData(True)
        # 等待1分钟
        time.sleep(40)
