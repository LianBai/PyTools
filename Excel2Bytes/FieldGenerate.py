import os.path
import re
import struct
import pandas as pd

from ExcelUtil import TurnBytes, IsNeedRecordSize, typeMap
from LogUtil import ShowLog
from PathUtil import BytesPath


# 将Excel数据转换为二进制
def TurnBytesByExcel(excelData, startRow, startColumn, isNeedRecordSize):
    rows = excelData.iloc[startRow:].iterrows() if startRow > 0 else excelData.iterrows()
    columns = excelData.columns[startColumn:] if startColumn > 0 else excelData.columns
    data_bytes = b''
    for index, row in rows:
        tBytes = b''
        tSize = 0
        # 将数据添加到 Data1 对象中
        for col in columns:
            if 'c' in col[0].lower():  # 判断是否需要的数据
                headDataArray = excelData[col].head(3)
                data = TurnBytes(headDataArray[1], row[col])
                tBytes += data[0]
                tSize += data[1]
        if isNeedRecordSize:
            data_bytes += struct.pack(f"{typeMap['byte'][0]}", tSize)
        data_bytes += tBytes
    return data_bytes


# 生成单个字段的二进制文件
def GenerateSingleFieldBytes(excelPath, sheetName, bytesName=None):
    excelData = pd.read_excel(excelPath, sheet_name=sheetName)
    # 将数据转换为二进制
    data_bytes = TurnBytesByExcel(excelData, 4, 1, IsNeedRecordSize(excelData))
    # 将bytes保存到本地文件
    if bytesName is None:
        bytesName = re.sub(r'[^a-zA-Z0-9]', '', f'table{os.path.basename(excelPath).split(".")[0]}{sheetName}').lower()
    bytesPath = os.path.join(BytesPath, f'{bytesName}.bytes')
    with open(bytesPath, 'wb') as f:
        f.write(data_bytes)
    ShowLog(f'生成二进制文件: {bytesPath}')


# 生成字段的二进制文件
def GenerateFieldBytes(excelPath, sheetName, bytesName=None):
    excelData = pd.read_excel(excelPath, sheet_name=sheetName)
    # 将数据转换为二进制
    data_bytes = TurnBytesByExcel(excelData, 4, 0, IsNeedRecordSize(excelData))
    # 将bytes保存到本地文件
    if bytesName is None:
        bytesName = re.sub(r'[^a-zA-Z0-9]', '', f'table{os.path.basename(excelPath).split(".")[0]}{sheetName}').lower()
    bytesPath = os.path.join(BytesPath, f'{bytesName}.bytes')
    with open(bytesPath, 'wb') as f:
        f.write(data_bytes)
    ShowLog(f'生成二进制文件: {bytesPath}')


