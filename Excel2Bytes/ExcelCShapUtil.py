from CSScriptBuilder import CSScriptBuilder
from ExcelUtil import TableLoadAssembly, GetCShapeType, TableStructAssembly, TableResLoadAssembly, OfferMap, SizeMap, \
    typeMap


def FieldExcelScript(scriptName, firstValueType, secValueType, bytesName, scriptBuilder):
    # 将数据转换为二进制
    Scripts = CSScriptBuilder()
    Scripts.AppendUsing('System.Collections.Generic')
    Scripts.AppendUsing('System.IO')
    Scripts.AppendUsing('System.Text')
    Scripts.AppendUsing(TableResLoadAssembly)
    Scripts.AppendUsing(TableLoadAssembly)
    Scripts.AppendEmptyLine()
    Scripts.BeginNamespace(TableStructAssembly)
    Scripts.BeginClass(scriptName, 'public sealed', 'ITable')
    Scripts.AppendEmptyLine()
    Scripts.AppendLine(f'private static {scriptName} s_Instance;')
    Scripts.AppendField('m_Cached', f'Dictionary<{OfferMap}, {secValueType}>', 'private')
    Scripts.AppendField('m_Reader', 'BinaryReader', 'private')
    Scripts.AppendEmptyLine()
    Scripts.AppendLine(f'public static {scriptName} Instance => s_Instance ??= new {scriptName}();')
    Scripts.AppendEmptyLine()
    Scripts.BeginConstructionMethod(scriptName, 'public')
    Scripts.AppendLine(f'TableManager.Add(this);')
    Scripts.AppendLine(f'm_Cached = new Dictionary<{OfferMap}, {secValueType}>();')
    Scripts.AppendLine(f'//这里需要走自己资源加载字节文件')
    Scripts.AppendLine(f'm_Reader = new BinaryReader(ResManager.OpenFile("{bytesName}.bytes"), Encoding.UTF8);')
    Scripts.EndMethod()
    Scripts.AppendEmptyLine()
    Scripts.BeginMethod('Dispose', 'public')
    Scripts.AppendLine(f'TableManager.Remove(this);')
    Scripts.AppendLine('m_Cached.Clear();')
    Scripts.AppendLine('m_Reader.Close();')
    Scripts.EndMethod()
    Scripts.AppendEmptyLine()
    Scripts.BeginMethod('ReadData', 'public', secValueType, f'{OfferMap} offer')
    Scripts.BeginIf(f'm_Cached.TryGetValue(offer, out var value)')
    Scripts.AppendLine(f'return value;')
    Scripts.EndIf()
    Scripts.AppendLine('m_Reader.BaseStream.Position = (long)offer;')
    Scripts.AppendLine(f'value = m_Reader.{GetTypeRead(secValueType)}();')
    Scripts.AppendLine(f'm_Cached.Add(offer, value);')
    Scripts.AppendLine(f'return value;')
    Scripts.EndMethod()
    Scripts.AppendEmptyLine()
    Scripts.AppendEnter()
    for des in scriptBuilder:
        Scripts.Append(des)
    Scripts.AppendEmptyLine()
    Scripts.EndClass()
    Scripts.EndNamespace()
    Scripts.GenerateScript(scriptName)


def LNGExcelScript(scriptName, bytesName):
    # 将数据转换为二进制
    Scripts = CSScriptBuilder()
    Scripts.AppendUsing('System')
    Scripts.AppendUsing('System.Collections.Generic')
    Scripts.AppendUsing('System.IO')
    Scripts.AppendUsing('System.Text')
    Scripts.AppendUsing(TableResLoadAssembly)
    Scripts.AppendUsing(TableLoadAssembly)
    Scripts.AppendEmptyLine()
    Scripts.BeginNamespace(TableStructAssembly)
    Scripts.BeginClass(scriptName, 'public sealed', 'ITable')
    Scripts.AppendEmptyLine()
    Scripts.AppendLine(f'private static {scriptName} s_Instance;')
    Scripts.AppendField('m_Cached', f'Dictionary<uint, string>', 'private')
    Scripts.AppendField('m_Entries', f'Dictionary<uint, ulong>', 'private')
    Scripts.AppendField('m_Reader', 'BinaryReader', 'private')
    Scripts.AppendEmptyLine()
    Scripts.AppendLine(f'public static {scriptName} Instance => s_Instance ??= new {scriptName}();')
    Scripts.AppendEmptyLine()
    Scripts.BeginConstructionMethod(scriptName, 'public')
    Scripts.AppendLine(f'TableManager.Add(this);')
    Scripts.AppendLine(f'm_Cached = new Dictionary<uint, string>();')
    Scripts.AppendLine(f'm_Entries = new Dictionary<uint, ulong>();')
    Scripts.AppendLine(f'//这里需要走自己资源加载字节文件')
    Scripts.AppendLine(f'm_Reader = new BinaryReader(ResManager.OpenFile("{bytesName}.bytes"), Encoding.UTF8);')
    Scripts.AppendLine(f'ulong allOffset = 0;')
    Scripts.BeginWhile('true')
    Scripts.BeginTry()
    Scripts.AppendLine('var key = m_Reader.ReadUInt32();')
    Scripts.BeginIf('key == 0')
    Scripts.AppendLine('break;')
    Scripts.EndIf()
    Scripts.AppendLine(f'var offset = m_Reader.{GetTypeRead(SizeMap)}();')
    Scripts.AppendLine('m_Entries.Add(key, allOffset + 4);')
    Scripts.AppendLine(f'allOffset += 4 + {typeMap[SizeMap][1]} + (ulong)offset;')
    Scripts.AppendLine('m_Reader.BaseStream.Position += offset;')
    Scripts.AppendLine('//判断是否读取完毕')
    Scripts.BeginIf('m_Reader.BaseStream.Position >= m_Reader.BaseStream.Length')
    Scripts.AppendLine('break;')
    Scripts.EndIf()
    Scripts.EndTry()
    Scripts.BeginCatch('Exception e')
    Scripts.AppendLine('m_Reader.Close();')
    Scripts.AppendLine('break;')
    Scripts.EndCatch()
    Scripts.EndWhile()
    Scripts.EndMethod()
    Scripts.AppendEmptyLine()
    Scripts.BeginMethod('Dispose', 'public')
    Scripts.AppendLine(f'TableManager.Remove(this);')
    Scripts.AppendLine('m_Cached.Clear();')
    Scripts.AppendLine('m_Reader.Close();')
    Scripts.EndMethod()
    Scripts.AppendEmptyLine()
    Scripts.BeginMethod('Find', 'public static', 'string', f'uint id, bool throwException = true')
    Scripts.BeginIf(f'Instance.m_Cached.TryGetValue(id, out var value)')
    Scripts.AppendLine(f'return value;')
    Scripts.EndIf()
    Scripts.BeginIf(f'Instance.m_Entries.TryGetValue(id, out var offset)')
    Scripts.AppendLine('Instance.m_Reader.BaseStream.Position = (long)Instance.m_Entries[id];')
    Scripts.AppendLine('value = Instance.m_Reader.ReadString();')
    Scripts.AppendLine('Instance.m_Cached.Add(id, value);')
    Scripts.AppendLine(f'return value;')
    Scripts.EndIf()
    Scripts.BeginIf('throwException')
    Scripts.AppendLine(f'throw new Exception($"Can not find {scriptName} id: {id}");')
    Scripts.EndIf()
    Scripts.AppendLine('return id.ToString();')
    Scripts.EndMethod()
    Scripts.AppendEmptyLine()
    Scripts.EndClass()
    Scripts.EndNamespace()
    Scripts.GenerateScript(scriptName)


def GetFieldProperty(fieldType, fieldName, fieldValue, script):
    valueType = GetCShapeType(fieldType)
    if 'LNGRef' in fieldType:
        script.AppendLine(
            f"public static {valueType} {fieldName} => TableLanguage.Find(Instance.ReadData({fieldValue}));")
    else:
        script.AppendLine(
            f"public static {valueType} {fieldName} => Instance.ReadData({fieldValue});")


def GetTypeRead(fieldType):
    if fieldType == 'int':
        return 'ReadInt32'
    elif fieldType == 'float':
        return 'ReadSingle'
    elif fieldType == 'double':
        return 'ReadDouble'
    elif fieldType == 'bool':
        return 'ReadBoolean'
    elif fieldType == 'long':
        return 'ReadInt64'
    elif fieldType == 'short':
        return 'ReadInt16'
    elif fieldType == 'ushort':
        return 'ReadUInt16'
    elif fieldType == 'uint':
        return 'ReadUInt32'
    elif fieldType == 'byte':
        return 'ReadByte'
    elif fieldType == 'uint8':
        return 'ReadByte'
