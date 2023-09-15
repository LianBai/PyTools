import os
import struct
import sys

from FileUtil import CopyFile
from LanguageUtil import GetLanguageKey
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
        'uint': ('I', 4)
    }


def GetCShapeReadType(fieldType):
    if 'LNGRef' in fieldType:
        return fieldType.replace('LNGRef', 'uint')
    return fieldType


def GetCShapeType(fieldType):
    if 'LNGRef' in fieldType:
        return fieldType.replace('LNGRef', 'string')
    return fieldType


# 是否需要记录大小
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
        byte = struct.pack(f"{typeMap[SizeMap][0]}", len(value)) + struct.pack(f'{len(value)}s', value)
        size = typeMap[SizeMap][1] + len(value)
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
