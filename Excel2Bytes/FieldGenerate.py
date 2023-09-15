import os.path
import re
import struct
import sys

import numpy as np
import pandas as pd

from CSScriptBuilder import CSScriptBuilder
from ExcelCShapUtil import FieldExcelScript, GetFieldProperty, LNGExcelScript
from ExcelUtil import TurnBytes, IsNeedRecordSize, typeMap, GetCShapeType, TableLoadAssembly, SizeMap, GetCShapeReadType
from LanguageUtil import CNLanguage
from LogUtil import ShowLog
from PathUtil import BytesPath, LanguageXlsxPath
from enum import Enum


class GenerateScriptType(Enum):
    FieldType = 0
    FindType = 1
    LNGType = 2
    CustomType = 3


# 将Excel数据转换为二进制
def TurnBytesByExcel(excelData, startRow, startColumn, isNeedRecordSize, generateScriptType, script=None):
    rows = excelData.iloc[startRow:].iterrows() if startRow > 0 else excelData.iterrows()
    firstRow = excelData.iloc[0]
    columns_with_c = np.where(firstRow.str.contains('c', case=False))[0]
    if len(columns_with_c) < 2:
        ShowLog(f'表格数据不完整, 请检查表格: {excelData}')
        sys.exit(1)
    firstIndex = columns_with_c[0]
    secondIndex = columns_with_c[1]
    valueOldType = str(excelData.iloc[2, secondIndex])
    dataBytes = b''
    allSize = 0
    for index, row in rows:
        tBytes = b''
        tSize = 0
        if generateScriptType == GenerateScriptType.FieldType:
            GetFieldProperty(valueOldType, row[firstIndex], allSize, script)
        # 将数据添加到 Data1 对象中
        for col_index in range(startColumn, len(row)):
            if 'c' in str(excelData.iloc[0, col_index]):  # 判断是否需要的数据
                fieldType = excelData.iloc[2, col_index]
                fieldValue = row[col_index]
                data = TurnBytes(fieldType, fieldValue)
                tBytes += data[0]
                tSize += data[1]
        if isNeedRecordSize and generateScriptType != GenerateScriptType.LNGType:
            tSize += typeMap[SizeMap][1]
            dataBytes += struct.pack(f"{typeMap[SizeMap][0]}", tSize)
        dataBytes += tBytes
        allSize += tSize
    return dataBytes


# 生成单个字段的二进制文件
def GenerateFieldBytes(excelPath, sheetName, scriptName=None):
    if scriptName is None:
        scriptName = f'{os.path.basename(excelPath).split(".")[0]}{sheetName}'
    scriptName = f'Table{scriptName}'
    excelData = pd.read_excel(excelPath, sheet_name=sheetName, header=None)
    firstRow = excelData.iloc[0]
    columns_with_c = np.where(firstRow.str.contains('c', case=False))[0]
    firstIndex = columns_with_c[0]
    secondIndex = columns_with_c[1]
    firstValueOldType = str(excelData.iloc[1, firstIndex])
    firstValueType = GetCShapeReadType(firstValueOldType)
    secValueOldType = str(excelData.iloc[2, secondIndex])
    secValueType = GetCShapeReadType(secValueOldType)
    Scripts = CSScriptBuilder()
    data_bytes = TurnBytesByExcel(excelData, 4, 1, IsNeedRecordSize(excelData), GenerateScriptType.FieldType, Scripts)
    FieldExcelScript(scriptName, firstValueType, secValueType, scriptName.lower(), Scripts)
    # 将bytes保存到本地文件
    bytesPath = os.path.join(BytesPath, f'{scriptName.lower()}.bytes')
    with open(bytesPath, 'wb') as f:
        f.write(data_bytes)
    ShowLog(f'生成二进制文件: {bytesPath}')


def GenerateLNGBytes(scriptName=None):
    if scriptName is None:
        scriptName = f'{os.path.basename(LanguageXlsxPath).split(".")[0]}{CNLanguage}'
    scriptName = f'Table{scriptName}'
    excelData = pd.read_excel(LanguageXlsxPath, sheet_name=CNLanguage, header=None)
    data_bytes = TurnBytesByExcel(excelData, 4, 0, IsNeedRecordSize(excelData), GenerateScriptType.LNGType)
    LNGExcelScript(scriptName, scriptName.lower())
    # 将bytes保存到本地文件
    bytesPath = os.path.join(BytesPath, f'{scriptName.lower()}.bytes')
    with open(bytesPath, 'wb') as f:
        f.write(data_bytes)
    ShowLog(f'生成二进制文件: {bytesPath}')


# 生成字段的二进制文件
# def GenerateFieldBytes(excelPath, sheetName, bytesName=None):
#     excelData = pd.read_excel(excelPath, sheet_name=sheetName)
#     # 将数据转换为二进制
#     data_bytes = TurnBytesByExcel(excelData, 4, 0, IsNeedRecordSize(excelData), GenerateScriptType.FindType, sheetName)
#     # 将bytes保存到本地文件
#     if bytesName is None:
#         bytesName = re.sub(r'[^a-zA-Z0-9]', '', f'table{os.path.basename(excelPath).split(".")[0]}{sheetName}').lower()
#     bytesPath = os.path.join(BytesPath, f'{bytesName}.bytes')
#     with open(bytesPath, 'wb') as f:
#         f.write(data_bytes)
#     ShowLog(f'生成二进制文件: {bytesPath}')
