import math
import os.path
import struct
import sys

from CSScriptBuilder import CSScriptBuilder
from LanguageUtil import GetLanguageKey
from PathUtil import ScriptsPath

TableAssembly = 'LBRuntime.Table'
TableLoadAssembly = 'LBRuntime.Table.Loader'
TableStructAssembly = 'LBRuntime.Table.Struct'

typeMap = {
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


# 是否需要记录大小
def IsNeedRecordSize(excelData):
    isNeedRecord = False
    for index, colum in excelData.iloc[0].items():  # 修改为第一行（索引为0）
        # 将数据添加到 Data1 对象中
        if 'c' in colum.lower():
            fieldType = excelData.iloc[2][index]  # 修改为当前行（索引为1）的当前列
            if fieldType not in typeMap and fieldType != 'LNGRef':  # 修改为当前行（索引为2）的当前列
                return True
    return False


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
            pByte += struct.pack(f"{typeMap['byte'][0]}", qSize) + qByte
            pSize += typeMap['byte'][1] + qSize
        byte = struct.pack(f"{typeMap['byte'][0]}", pSize) + pByte
        pSize += typeMap['byte'][1]
        return byte, pSize
    if '[]' in fieldType:
        singleType = fieldType[:-2]
        size = 0
        tByte = b''
        for singleValue in fieldValue.splite('|'):
            sByte, sSize = SingleTurnBytes(singleType, singleValue)
            tByte += sByte
            size += sSize
        byte = struct.pack(f"{typeMap['byte'][0]}", size) + tByte
        size += typeMap['byte'][1]
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
            byte = struct.pack(f"{typeMap['byte'][0]}", 0)
            size = typeMap['byte'][1]
            return byte, size
        value = fieldValue.encode('utf-8')
        byte = struct.pack(f"{typeMap['byte'][0]}", len(value)) + struct.pack(f'{len(value)}s', value)
        size = typeMap['byte'][1] + len(value)
        return byte, size
    elif fieldType == 'LNGRef':
        fieldValue = str(fieldValue)
        if fieldValue == 'nan':
            struct.pack('b', 0), 4
        return struct.pack('b', GetLanguageKey(fieldValue)), 4
    else:
        sys.stderr.write(f"Error: Unknown field type '{fieldType}'\n")
        input("Press Enter to exit...")
        sys.exit()


# 生成单个字段的二进制文件
def CreateTableManagerCs():
    script = CSScriptBuilder()
    script.AppendUsing('System.Collections.Generic')
    script.AppendUsing('UnityEngine')
    script.BeginNamespace(TableLoadAssembly)
    script.BeginInterface('ITable', 'public')
    script.AppendInterfaceMethod('Dispose')
    script.EndInterface()
    script.AppendEmptyLine()
    script.BeginClass('TableManager', 'public static')
    script.AppendField('s_Inited', 'bool', 'private static')
    script.AppendField('s_Cached', 'List<ITable>', 'private static', 'new List<ITable>()')
    # 添加方法
    script.AppendEmptyLine()
    script.BeginMethod("Add", parameters="ITable table")
    script.AppendLine("Debug.Assert(s_Inited, \"add but TableManager not init \");")
    script.AppendLine("s_Cached.Add(table);")
    script.EndMethod()
    script.AppendEmptyLine()
    script.BeginMethod("Remove", parameters="ITable table")
    script.AppendLine("Debug.Assert(s_Inited, \"remove but TableManager not init\");")
    script.AppendLine("if (s_Cached.Remove(table))")
    script.BeginBrace()
    script.AppendLine("table.Dispose();")
    script.EndBrace()
    script.EndMethod()
    script.AppendEmptyLine()
    script.BeginMethod("Init")
    script.AppendLine("Debug.Assert(!s_Inited, \"TableManager already init\");")
    script.AppendLine("s_Inited = true;")
    script.EndMethod()
    script.AppendEmptyLine()
    script.BeginMethod("UnInit")
    script.AppendLine("Debug.Assert(s_Inited, \"TableManager not init\");")
    script.AppendLine("s_Inited = false;")
    script.AppendLine("foreach (var table in s_Cached)")
    script.BeginBrace()
    script.AppendLine("table.Dispose();")
    script.EndBrace()
    script.AppendLine("s_Cached.Clear();")
    script.EndMethod()
    script.EndClass()
    script.EndNamespace()
    script.GenerateScript(os.path.join(ScriptsPath, 'TableManager'))
