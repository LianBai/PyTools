import os
import re
import struct
import sys
from enum import Enum

import numpy as np

from FileUtil import CopyFile
from LanguageUtil import GetLanguageKey
from LogUtil import ShowLog
from PathUtil import ScriptsPath, ScriptsExportPath, BytesPath, BytesExportPath

TableAssembly = 'ZHRuntime.Table'
TableLoadAssembly = 'ZHRuntime.Table.Loader'
TableStructAssembly = 'ZHRuntime.Table.Struct'
TableResLoadAssembly = 'ZHUnity'

SizeMap = 'ushort'
OfferMap = 'ulong'

typeMap = {
        'uint8': ('B', 1),
        'byte': ('b', 1),
        'int': ('i', 4),
        'float': ('f', 4),
        'double': ('d', 8),
        'bool': ('?', 1),
        'long': ('q', 8),
        'short': ('h', 2),
        'ushort': ('H', 2),
        'uint': ('I', 4),
        'ulong': ('Q', 8),
        'int64': ('q', 8),
        'uint64': ('Q', 8)
    }


class GenerateScriptType(Enum):
    FieldType = 0
    FindType = 1
    LNGType = 2
    CustomType = 3


def GetCShapeReadType(fieldType):
    if 'map' in fieldType.lower():
        pattern = r"map\|(\w+)\|(\w+)"
        replacement = r"Dictionary<\1,\2>"
        fieldType = re.sub(pattern, replacement, fieldType, flags=re.IGNORECASE)
    return GetCShapeReadBaseType(fieldType)


def GetCShapeReadBaseType(fieldType):
    if 'LNGRef' in fieldType:
        return fieldType.replace('LNGRef', 'uint')
    if 'int64' in fieldType:
        return fieldType.replace('int64', 'long')
    if 'uint64' in fieldType:
        return fieldType.replace('uint64', 'ulong')
    return fieldType


def GetCShapeType(fieldType):
    if 'LNGRef' in fieldType:
        return fieldType.replace('LNGRef', 'string')
    if 'int64' in fieldType:
        return fieldType.replace('int64', 'long')
    if 'uint64' in fieldType:
        return fieldType.replace('uint64', 'ulong')
    return fieldType


def GetFieldProperty(fieldType, fieldName, fieldValue, script):
    valueType = GetCShapeType(fieldType)
    if 'LNGRef' in fieldType:
        script.AppendLine(
            f"public static {valueType} {fieldName} => TableLanguage.Find(Instance.ReadData({fieldValue}));")
    else:
        script.AppendLine(
            f"public static {valueType} {fieldName} => Instance.ReadData({fieldValue});")


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
        if generateScriptType != GenerateScriptType.FieldType and generateScriptType != GenerateScriptType.LNGType:
            tSize += typeMap[SizeMap][1]
            dataBytes += struct.pack(f"{typeMap[SizeMap][0]}", tSize)
        dataBytes += tBytes
        allSize += tSize
    return dataBytes


# 是否需要记录大小(方法：如果不是基础类型都是要记录的)
def IsNeedRecordSize(excelData):
    for index, colum in excelData.iloc[0].items():  # 修改为第一行（索引为0）
        # 将数据添加到 Data1 对象中
        if 'c' in colum.lower():
            fieldType = excelData.iloc[2, index]  # 修改为当前行（索引为1）的当前列
            if fieldType in typeMap or fieldType == 'LNGRef':  # 修改为当前行（索引为2）的当前列
                return False
    return True


# 将Excel数据转换为二进制
def TurnBytes(fieldType, fieldValue):
    if '[][]' in fieldType:
        singleType = fieldType[:-2]
        pSize = 0
        pByte = b''
        for singleValue in fieldValue.split('|'):
            qSize = 0
            qByte = b''
            for value in singleValue.split(':'):
                sByte, sSize = SingleTurnBytes(singleType, value)
                qByte += sByte
                qSize += sSize
            pByte += struct.pack(f"{typeMap[SizeMap][0]}", qSize) + qByte
            pSize += typeMap[SizeMap][1] + qSize
        byte = struct.pack(f"{typeMap[SizeMap][0]}", pSize) + pByte
        pSize += typeMap[SizeMap][1]
        return byte, pSize
    if '[]' in fieldType:
        singleType = fieldType[:-2]
        size = 0
        tByte = b''
        for singleValue in fieldValue.splite('|'):
            sByte, sSize = SingleTurnBytes(singleType, singleValue)
            tByte += sByte
            size += sSize
        byte = struct.pack(f"{typeMap[SizeMap][0]}", size) + tByte
        size += typeMap[SizeMap][1]
        return byte, size
    if 'slc' in fieldType.lower():
        singleType = fieldType.replace('slc|', '')
        size = 0
        tByte = b''
        for singleValue in fieldValue.splite('|'):
            sByte, sSize = SingleTurnBytes(singleType, singleValue)
            tByte += sByte
            size += sSize
        byte = struct.pack(f"{typeMap[SizeMap][0]}", size) + tByte
        size += typeMap[SizeMap][1]
        return byte, size
    if 'map' in fieldType.lower():
        pattern = r"map\|(\w+)\|(\w+)"
        matches = re.findall(pattern, fieldType, flags=re.IGNORECASE)
        type1 = matches[0][0]
        type2 = matches[0][1]
        size = 0
        tByte = b''
        for singleValue in fieldValue.split('|'):
            qByte, qSize = SingleTurnBytes(type1, singleValue.split(':')[0])
            tByte += qByte
            size += qSize
            qByte, qSize = SingleTurnBytes(type2, singleValue.split(':')[1])
            tByte += qByte
            size += qSize
        byte = struct.pack(f"{typeMap[SizeMap][0]}", size) + tByte
        size += typeMap[SizeMap][1]
        return byte, size
    if 'dictionary' in fieldType.lower():
        pattern = r"dictionary\|(\w+)\|(\w+)"
        matches = re.findall(pattern, fieldType, flags=re.IGNORECASE)
        type1 = matches[0][0]
        type2 = matches[0][1]
        size = 0
        tByte = b''
        for singleValue in fieldValue.split('|'):
            qByte, qSize = SingleTurnBytes(type1, singleValue.split(':')[0])
            tByte += qByte
            size += qSize
            qByte, qSize = SingleTurnBytes(type2, singleValue.split(':')[1])
            tByte += qByte
            size += qSize
        byte = struct.pack(f"{typeMap[SizeMap][0]}", size) + tByte
        size += typeMap[SizeMap][1]
        return byte, size
    if 'double_slc' in fieldType.lower():
        singleType = fieldType.replace('double_slc|', '')
        size = 0
        tByte = b''
        for singleValue in fieldValue.split('|'):
            qSize = 0
            qByte = b''
            for value in singleValue.split(':'):
                sByte, sSize = SingleTurnBytes(singleType, value)
                qByte += sByte
                qSize += sSize
            tByte += struct.pack(f"{typeMap[SizeMap][0]}", qSize) + qByte
            size += typeMap[SizeMap][1] + qSize
        byte = struct.pack(f"{typeMap[SizeMap][0]}", size) + tByte
        size += typeMap[SizeMap][1]
        return byte, size
    else:
        return SingleTurnBytes(fieldType, fieldValue)


# 将单个数据转换为二进制
def SingleTurnBytes(fieldType, fieldValue):
    if fieldType in typeMap:
        fmt, size = typeMap[fieldType]
        return struct.pack(fmt, fieldValue), size
    elif fieldType == 'string':
        fieldValue = str(fieldValue)
        if fieldValue == 'nan':
            byte = struct.pack(f"{typeMap[SizeMap][0]}", 0)
            size = typeMap[SizeMap][1]
            return byte, size
        value = fieldValue.encode('utf-8')
        strSize = len(str(value))
        byte = struct.pack(f"{typeMap[SizeMap][0]}", strSize) + struct.pack(f'{strSize}s', value)
        size = typeMap[SizeMap][1] + strSize
        return byte, size
    elif fieldType == 'LNGRef':
        fieldValue = str(fieldValue)
        if fieldValue == 'nan':
            struct.pack('I', 0), 4
        return struct.pack('I', GetLanguageKey(fieldValue)), 4
    else:
        sys.stderr.write(f"Error: Unknown field type '{fieldType}'\n")
        input("Press Enter to exit...")
        sys.exit()


def CopyScripts():
    for root, dirs, files in os.walk(ScriptsPath):
        for file in files:
            CopyFile(os.path.join(ScriptsPath, file), os.path.join(ScriptsExportPath, file))


def CopyBytes():
    for root, dirs, files in os.walk(BytesPath):
        for file in files:
            CopyFile(os.path.join(BytesPath, file), os.path.join(BytesExportPath, file))


def GetScriptsName(excelPath, sheetName, scriptName=None):
    if scriptName is None:
        baseName = os.path.basename(excelPath).split(".")[0]
        if baseName.lower() == sheetName.lower():
            scriptName = baseName
        else:
            scriptName = f'{baseName}{sheetName}'
    return f'Table{scriptName}'
