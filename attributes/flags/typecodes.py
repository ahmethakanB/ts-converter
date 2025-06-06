from enum import IntEnum


class TypeCode(IntEnum):
    Empty = 0
    Object = 1
    DBNull = 2
    Boolean = 3
    Char = 4
    SByte = 5
    Byte = 6
    Int16 = 7
    UInt16 = 8
    Int32 = 9
    UInt32 = 10
    Int64 = 11
    UInt64 = 12
    Single = 13
    Double = 14
    Decimal = 15
    DateTime = 16
    String = 18


class InputType(IntEnum):
    text = 0
    textarea = 1
    datetime = 2
    select = 3
    multiselect = 4
    hidden = 5
