import os

from FileUtil import ExePath
from LogUtil import ShowLog

SavePath = os.path.join(ExePath(), 'Save')
TablePath = os.path.join(SavePath, 'Table')
BytesPath = os.path.join(SavePath, 'Bytes')
LanguageXlsxPath = os.path.join(TablePath, 'Languages.xlsx')


def InitFileDir():
    if not os.path.exists(SavePath):
        os.mkdir(SavePath)
        ShowLog('创建文件夹: Save')
    if not os.path.exists(TablePath):
        os.mkdir(TablePath)
        ShowLog('创建文件夹: Table')
    if not os.path.exists(BytesPath):
        os.mkdir(BytesPath)
        ShowLog('创建文件夹: Bytes')