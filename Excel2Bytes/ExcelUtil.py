import math
import os.path
import struct
import sys

from CSScriptBuilder import CSScriptBuilder
from PathUtil import ScriptsPath

TableAssembly = 'LBRuntime.Table'
TableLoadAssembly = 'LBRuntime.Table.Loader'
TableStructAssembly = 'LBRuntime.Table.Struct'

typeMap = {
        'int': ('i', 4),
        'float': ('f', 4),
        'double': ('d', 8),
        'bool': ('?', 1),
        'long': ('q', 8),
        'short': ('h', 2),
        'ushort': ('H', 2),
        'uint': ('I', 4)
    }


def TurnBytes(fieldType, fieldValue):
    if '[]' in fieldType:
        singleType = fieldType[:-2]
        size = 0
        byte = b''
        for singleValue in fieldValue.splite('|'):
            sByte, sSize = SingleTurnBytes(singleType,singleValue)
            byte += sByte
            size += sSize
        return byte, size
    else:
        return SingleTurnBytes(fieldType, fieldValue)


def SingleTurnBytes(fieldType, fieldValue):
    if fieldType in typeMap:
        fmt, size = typeMap[fieldType]
        return struct.pack(fmt, fieldValue), size
    elif fieldType == 'string':
        fieldValue = str(fieldValue)
        if fieldValue == 'nan':
            byte = struct.pack(f"{typeMap['ushort'][0]}", 0)
            size = typeMap['ushort'][1]
            return byte, size
        value = fieldValue.encode('utf-8')
        byte = struct.pack(f"{typeMap['ushort'][0]}", len(value)) + struct.pack(f'{len(value)}s', value)
        size = typeMap['ushort'][1] + len(value)
        return byte, size
    elif fieldType == 'LNGRef':
        return struct.pack('i', 9999), 4
    else:
        sys.stderr.write(f"Error: Unknown field type '{fieldType}'\n")
        input("Press Enter to exit...")
        sys.exit()


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
