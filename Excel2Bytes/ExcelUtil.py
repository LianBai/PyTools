import math
import struct
import sys

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
