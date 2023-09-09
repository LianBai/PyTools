import os.path
import re

import pandas as pd

from ExcelUtil import TurnBytes
from LogUtil import ShowLog
from PathUtil import BytesPath


def GenerateSingleFieldBytes(excelPath, sheetName, bytesName=None):
    excelData = pd.read_excel(excelPath, sheet_name=sheetName)
    # 将数据转换为二进制
    data_bytes = b''
    for index, row in excelData.iloc[4:].iterrows():
        # 将数据添加到 Data1 对象中
        for col in excelData.columns[1:]:
            if 'c' in col[0].lower():  # 判断是否需要的数据
                headDataArray = excelData[col].head(3)
                data_bytes += TurnBytes(headDataArray[1], row[col])[0]
    # 将bytes保存到本地文件
    if bytesName is None:
        bytesName = re.sub(r'[^a-zA-Z0-9]', '', f'table{os.path.basename(excelPath).split(".")[0]}{sheetName}').lower()
    bytesPath = os.path.join(BytesPath, f'{bytesName}.bytes')
    with open(bytesPath, 'wb') as f:
        f.write(data_bytes)
    ShowLog(f'生成二进制文件: {bytesPath}')


def GenerateFieldBytes(excelPath, sheetName, bytesName=None):
    excelData = pd.read_excel(excelPath, sheet_name=sheetName)
    # 将数据转换为二进制
    data_bytes = b''
    for index, row in excelData.iloc[4:].iterrows():
        # 将数据添加到 Data1 对象中
        for col in excelData.columns:
            if 'c' in col[0].lower():  # 判断是否需要的数据
                headDataArray = excelData[col].head(3)
                data_bytes += TurnBytes(headDataArray[1], row[col])[0]
    # 将bytes保存到本地文件
    if bytesName is None:
        bytesName = re.sub(r'[^a-zA-Z0-9]', '', f'table{os.path.basename(excelPath).split(".")[0]}{sheetName}').lower()
    bytesPath = os.path.join(BytesPath, f'{bytesName}.bytes')
    with open(bytesPath, 'wb') as f:
        f.write(data_bytes)
    ShowLog(f'生成二进制文件: {bytesPath}')
