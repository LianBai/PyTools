import zlib

import pandas as pd
import DataInfo_pb2
import numpy as np


def GenerateNoneBytes(excelPath, sheetName, bytesName):
    excelData = pd.read_excel(excelPath, sheet_name=sheetName)
    data = []
    for index, row in excelData.iloc[4:].iterrows():
        # 将数据添加到 Data1 对象中
        for col in excelData.columns:
            if 'c' in col[0].lower():  # 判断是否需要的数据
                headDataArray = excelData[col].head(3)
                if headDataArray[1] == 'LNGRef':
                    data.append(9999)
                else:
                    data.append(row[col])
    data_bytes = bytes(str(data), 'utf-8')
    # 使用 zlib 进行压缩
    compressed_data = zlib.compress(data_bytes)
    # 将bytes保存到本地文件
    with open(f'{bytesName}.bytes', 'wb') as f:
        f.write(compressed_data)


def GenerateProtobufBytes(excelPath, sheetName, bytesName):
    data = DataInfo_pb2.DataInfo()
    excelData = pd.read_excel(excelPath, sheet_name=sheetName)
    byteData = bytearray()
    for index, row in excelData.iloc[4:].iterrows():
        # 将数据添加到 Data1 对象中
        for col in excelData.columns:
            if 'c' in col[0].lower():  # 判断是否需要的数据
                headDataArray = excelData[col].head(3)
                item = data.excelData.add()
                GenerateDataType(item, headDataArray[1], row[col])

    byteData.extend(data.SerializeToString())
    # 将bytes保存到本地文件
    with open(f'{bytesName}.bytes', 'wb') as f:
        f.write(byteData)


def GenerateDataType(item, itemType, row):
    if itemType == 'int':
        if int(row) == '0' or int(row) == '':
            item = None
        else:
            item.intValue = int(row)
    elif itemType == 'float':
        if float(row) == '0' or float(row) == '':
            item = None
        else:
            item.floatValue = float(row)
    elif itemType == 'string':
        if str(row).isspace() or str(row) == '':
            item = None
        else:
            item.stringValue = str(row)
    elif itemType == 'LNGRef':
        if str(row).isspace() or str(row) == '':
            item = None
        else:
            item.intValue = 0
    return item
