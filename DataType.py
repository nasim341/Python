"""Data Types

1.Numeric data types: int, float, complex

2.String data types: str

3.Sequence types: list, tuple, range

4.Binary types: bytes, bytearray, memoryview

5.Mapping data type: dict

6.Boolean type: bool

7.Set data types: set, frozenset

"""
#Tuple
name = ("Md","Nasim","Ahmed")
print(type(name))
#Str
surname = ("Bulbul , Islam")
print(type(surname))

#List
bio = ["Md Nasim Ahmed", "kali", "linux"]
print(type(bio))

#range
number = range(6)
print(type(number))

# dict
nam = {"system": "windows" , "operating": 10}
print(type(nam))

# set
fullName = {"windows", "Ten"}
print(type(fullName))

# frozenset
operating = frozenset({"windows","Ten"})
print(type(operating))

# nonetype
null = None
print(type(null))

#######Binary Data Tpe##############

##Byte

thislist = [4,5,3,5,5,66,77,55]
value = bytes(thislist)
print(type(value))

##ByteArray
thislist = [4,5,3,5,5,66,77,55]
value1 =bytearray(thislist)
value1[0] = 3
print(value1[0])