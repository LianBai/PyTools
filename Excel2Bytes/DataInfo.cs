// <auto-generated>
//     Generated by the protocol buffer compiler.  DO NOT EDIT!
//     source: DataInfo.proto
// </auto-generated>
#pragma warning disable 1591, 0612, 3021, 8981
#region Designer generated code

using pb = global::Google.Protobuf;
using pbc = global::Google.Protobuf.Collections;
using pbr = global::Google.Protobuf.Reflection;
using scg = global::System.Collections.Generic;
/// <summary>Holder for reflection information generated from DataInfo.proto</summary>
public static partial class DataInfoReflection {

  #region Descriptor
  /// <summary>File descriptor for DataInfo.proto</summary>
  public static pbr::FileDescriptor Descriptor {
    get { return descriptor; }
  }
  private static pbr::FileDescriptor descriptor;

  static DataInfoReflection() {
    byte[] descriptorData = global::System.Convert.FromBase64String(
        string.Concat(
          "Cg5EYXRhSW5mby5wcm90byJQCgREYXRhEhIKCGludFZhbHVlGAIgASgFSAAS",
          "FAoKZmxvYXRWYWx1ZRgDIAEoAkgAEhUKC3N0cmluZ1ZhbHVlGAQgASgJSABC",
          "BwoFdmFsdWUiJAoIRGF0YUluZm8SGAoJZXhjZWxEYXRhGAEgAygLMgUuRGF0",
          "YSoqCghEYXRhVHlwZRIHCgNJTlQQABIJCgVGTE9BVBABEgoKBlNUUklORxAC",
          "YgZwcm90bzM="));
    descriptor = pbr::FileDescriptor.FromGeneratedCode(descriptorData,
        new pbr::FileDescriptor[] { },
        new pbr::GeneratedClrTypeInfo(new[] {typeof(global::DataType), }, null, new pbr::GeneratedClrTypeInfo[] {
          new pbr::GeneratedClrTypeInfo(typeof(global::Data), global::Data.Parser, new[]{ "IntValue", "FloatValue", "StringValue" }, new[]{ "Value" }, null, null, null),
          new pbr::GeneratedClrTypeInfo(typeof(global::DataInfo), global::DataInfo.Parser, new[]{ "ExcelData" }, null, null, null, null)
        }));
  }
  #endregion

}
#region Enums
public enum DataType {
  [pbr::OriginalName("INT")] Int = 0,
  [pbr::OriginalName("FLOAT")] Float = 1,
  [pbr::OriginalName("STRING")] String = 2,
}

#endregion

#region Messages
public sealed partial class Data : pb::IMessage<Data>
#if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    , pb::IBufferMessage
#endif
{
  private static readonly pb::MessageParser<Data> _parser = new pb::MessageParser<Data>(() => new Data());
  private pb::UnknownFieldSet _unknownFields;
  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
  public static pb::MessageParser<Data> Parser { get { return _parser; } }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
  public static pbr::MessageDescriptor Descriptor {
    get { return global::DataInfoReflection.Descriptor.MessageTypes[0]; }
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
  pbr::MessageDescriptor pb::IMessage.Descriptor {
    get { return Descriptor; }
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
  public Data() {
    OnConstruction();
  }

  partial void OnConstruction();

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
  public Data(Data other) : this() {
    switch (other.ValueCase) {
      case ValueOneofCase.IntValue:
        IntValue = other.IntValue;
        break;
      case ValueOneofCase.FloatValue:
        FloatValue = other.FloatValue;
        break;
      case ValueOneofCase.StringValue:
        StringValue = other.StringValue;
        break;
    }

    _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
  public Data Clone() {
    return new Data(this);
  }

  /// <summary>Field number for the "intValue" field.</summary>
  public const int IntValueFieldNumber = 2;
  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
  public int IntValue {
    get { return HasIntValue ? (int) value_ : 0; }
    set {
      value_ = value;
      valueCase_ = ValueOneofCase.IntValue;
    }
  }
  /// <summary>Gets whether the "intValue" field is set</summary>
  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
  public bool HasIntValue {
    get { return valueCase_ == ValueOneofCase.IntValue; }
  }
  /// <summary> Clears the value of the oneof if it's currently set to "intValue" </summary>
  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
  public void ClearIntValue() {
    if (HasIntValue) {
      ClearValue();
    }
  }

  /// <summary>Field number for the "floatValue" field.</summary>
  public const int FloatValueFieldNumber = 3;
  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
  public float FloatValue {
    get { return HasFloatValue ? (float) value_ : 0F; }
    set {
      value_ = value;
      valueCase_ = ValueOneofCase.FloatValue;
    }
  }
  /// <summary>Gets whether the "floatValue" field is set</summary>
  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
  public bool HasFloatValue {
    get { return valueCase_ == ValueOneofCase.FloatValue; }
  }
  /// <summary> Clears the value of the oneof if it's currently set to "floatValue" </summary>
  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
  public void ClearFloatValue() {
    if (HasFloatValue) {
      ClearValue();
    }
  }

  /// <summary>Field number for the "stringValue" field.</summary>
  public const int StringValueFieldNumber = 4;
  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
  public string StringValue {
    get { return HasStringValue ? (string) value_ : ""; }
    set {
      value_ = pb::ProtoPreconditions.CheckNotNull(value, "value");
      valueCase_ = ValueOneofCase.StringValue;
    }
  }
  /// <summary>Gets whether the "stringValue" field is set</summary>
  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
  public bool HasStringValue {
    get { return valueCase_ == ValueOneofCase.StringValue; }
  }
  /// <summary> Clears the value of the oneof if it's currently set to "stringValue" </summary>
  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
  public void ClearStringValue() {
    if (HasStringValue) {
      ClearValue();
    }
  }

  private object value_;
  /// <summary>Enum of possible cases for the "value" oneof.</summary>
  public enum ValueOneofCase {
    None = 0,
    IntValue = 2,
    FloatValue = 3,
    StringValue = 4,
  }
  private ValueOneofCase valueCase_ = ValueOneofCase.None;
  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
  public ValueOneofCase ValueCase {
    get { return valueCase_; }
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
  public void ClearValue() {
    valueCase_ = ValueOneofCase.None;
    value_ = null;
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
  public override bool Equals(object other) {
    return Equals(other as Data);
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
  public bool Equals(Data other) {
    if (ReferenceEquals(other, null)) {
      return false;
    }
    if (ReferenceEquals(other, this)) {
      return true;
    }
    if (IntValue != other.IntValue) return false;
    if (!pbc::ProtobufEqualityComparers.BitwiseSingleEqualityComparer.Equals(FloatValue, other.FloatValue)) return false;
    if (StringValue != other.StringValue) return false;
    if (ValueCase != other.ValueCase) return false;
    return Equals(_unknownFields, other._unknownFields);
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
  public override int GetHashCode() {
    int hash = 1;
    if (HasIntValue) hash ^= IntValue.GetHashCode();
    if (HasFloatValue) hash ^= pbc::ProtobufEqualityComparers.BitwiseSingleEqualityComparer.GetHashCode(FloatValue);
    if (HasStringValue) hash ^= StringValue.GetHashCode();
    hash ^= (int) valueCase_;
    if (_unknownFields != null) {
      hash ^= _unknownFields.GetHashCode();
    }
    return hash;
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
  public override string ToString() {
    return pb::JsonFormatter.ToDiagnosticString(this);
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
  public void WriteTo(pb::CodedOutputStream output) {
  #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    output.WriteRawMessage(this);
  #else
    if (HasIntValue) {
      output.WriteRawTag(16);
      output.WriteInt32(IntValue);
    }
    if (HasFloatValue) {
      output.WriteRawTag(29);
      output.WriteFloat(FloatValue);
    }
    if (HasStringValue) {
      output.WriteRawTag(34);
      output.WriteString(StringValue);
    }
    if (_unknownFields != null) {
      _unknownFields.WriteTo(output);
    }
  #endif
  }

  #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
  void pb::IBufferMessage.InternalWriteTo(ref pb::WriteContext output) {
    if (HasIntValue) {
      output.WriteRawTag(16);
      output.WriteInt32(IntValue);
    }
    if (HasFloatValue) {
      output.WriteRawTag(29);
      output.WriteFloat(FloatValue);
    }
    if (HasStringValue) {
      output.WriteRawTag(34);
      output.WriteString(StringValue);
    }
    if (_unknownFields != null) {
      _unknownFields.WriteTo(ref output);
    }
  }
  #endif

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
  public int CalculateSize() {
    int size = 0;
    if (HasIntValue) {
      size += 1 + pb::CodedOutputStream.ComputeInt32Size(IntValue);
    }
    if (HasFloatValue) {
      size += 1 + 4;
    }
    if (HasStringValue) {
      size += 1 + pb::CodedOutputStream.ComputeStringSize(StringValue);
    }
    if (_unknownFields != null) {
      size += _unknownFields.CalculateSize();
    }
    return size;
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
  public void MergeFrom(Data other) {
    if (other == null) {
      return;
    }
    switch (other.ValueCase) {
      case ValueOneofCase.IntValue:
        IntValue = other.IntValue;
        break;
      case ValueOneofCase.FloatValue:
        FloatValue = other.FloatValue;
        break;
      case ValueOneofCase.StringValue:
        StringValue = other.StringValue;
        break;
    }

    _unknownFields = pb::UnknownFieldSet.MergeFrom(_unknownFields, other._unknownFields);
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
  public void MergeFrom(pb::CodedInputStream input) {
  #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    input.ReadRawMessage(this);
  #else
    uint tag;
    while ((tag = input.ReadTag()) != 0) {
      switch(tag) {
        default:
          _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, input);
          break;
        case 16: {
          IntValue = input.ReadInt32();
          break;
        }
        case 29: {
          FloatValue = input.ReadFloat();
          break;
        }
        case 34: {
          StringValue = input.ReadString();
          break;
        }
      }
    }
  #endif
  }

  #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
  void pb::IBufferMessage.InternalMergeFrom(ref pb::ParseContext input) {
    uint tag;
    while ((tag = input.ReadTag()) != 0) {
      switch(tag) {
        default:
          _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, ref input);
          break;
        case 16: {
          IntValue = input.ReadInt32();
          break;
        }
        case 29: {
          FloatValue = input.ReadFloat();
          break;
        }
        case 34: {
          StringValue = input.ReadString();
          break;
        }
      }
    }
  }
  #endif

}

public sealed partial class DataInfo : pb::IMessage<DataInfo>
#if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    , pb::IBufferMessage
#endif
{
  private static readonly pb::MessageParser<DataInfo> _parser = new pb::MessageParser<DataInfo>(() => new DataInfo());
  private pb::UnknownFieldSet _unknownFields;
  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
  public static pb::MessageParser<DataInfo> Parser { get { return _parser; } }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
  public static pbr::MessageDescriptor Descriptor {
    get { return global::DataInfoReflection.Descriptor.MessageTypes[1]; }
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
  pbr::MessageDescriptor pb::IMessage.Descriptor {
    get { return Descriptor; }
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
  public DataInfo() {
    OnConstruction();
  }

  partial void OnConstruction();

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
  public DataInfo(DataInfo other) : this() {
    excelData_ = other.excelData_.Clone();
    _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
  public DataInfo Clone() {
    return new DataInfo(this);
  }

  /// <summary>Field number for the "excelData" field.</summary>
  public const int ExcelDataFieldNumber = 1;
  private static readonly pb::FieldCodec<global::Data> _repeated_excelData_codec
      = pb::FieldCodec.ForMessage(10, global::Data.Parser);
  private readonly pbc::RepeatedField<global::Data> excelData_ = new pbc::RepeatedField<global::Data>();
  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
  public pbc::RepeatedField<global::Data> ExcelData {
    get { return excelData_; }
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
  public override bool Equals(object other) {
    return Equals(other as DataInfo);
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
  public bool Equals(DataInfo other) {
    if (ReferenceEquals(other, null)) {
      return false;
    }
    if (ReferenceEquals(other, this)) {
      return true;
    }
    if(!excelData_.Equals(other.excelData_)) return false;
    return Equals(_unknownFields, other._unknownFields);
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
  public override int GetHashCode() {
    int hash = 1;
    hash ^= excelData_.GetHashCode();
    if (_unknownFields != null) {
      hash ^= _unknownFields.GetHashCode();
    }
    return hash;
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
  public override string ToString() {
    return pb::JsonFormatter.ToDiagnosticString(this);
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
  public void WriteTo(pb::CodedOutputStream output) {
  #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    output.WriteRawMessage(this);
  #else
    excelData_.WriteTo(output, _repeated_excelData_codec);
    if (_unknownFields != null) {
      _unknownFields.WriteTo(output);
    }
  #endif
  }

  #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
  void pb::IBufferMessage.InternalWriteTo(ref pb::WriteContext output) {
    excelData_.WriteTo(ref output, _repeated_excelData_codec);
    if (_unknownFields != null) {
      _unknownFields.WriteTo(ref output);
    }
  }
  #endif

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
  public int CalculateSize() {
    int size = 0;
    size += excelData_.CalculateSize(_repeated_excelData_codec);
    if (_unknownFields != null) {
      size += _unknownFields.CalculateSize();
    }
    return size;
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
  public void MergeFrom(DataInfo other) {
    if (other == null) {
      return;
    }
    excelData_.Add(other.excelData_);
    _unknownFields = pb::UnknownFieldSet.MergeFrom(_unknownFields, other._unknownFields);
  }

  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
  public void MergeFrom(pb::CodedInputStream input) {
  #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    input.ReadRawMessage(this);
  #else
    uint tag;
    while ((tag = input.ReadTag()) != 0) {
      switch(tag) {
        default:
          _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, input);
          break;
        case 10: {
          excelData_.AddEntriesFrom(input, _repeated_excelData_codec);
          break;
        }
      }
    }
  #endif
  }

  #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
  [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
  [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
  void pb::IBufferMessage.InternalMergeFrom(ref pb::ParseContext input) {
    uint tag;
    while ((tag = input.ReadTag()) != 0) {
      switch(tag) {
        default:
          _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, ref input);
          break;
        case 10: {
          excelData_.AddEntriesFrom(ref input, _repeated_excelData_codec);
          break;
        }
      }
    }
  }
  #endif

}

#endregion


#endregion Designer generated code