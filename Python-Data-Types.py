"""
Built-in Data Types
In programming, data type is an important concept.
Variables can store data of different types, and different types can do different things.
Python has the following data types built-in by default, in these categories:
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	    set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""
a = True
if 2 < 3:
    print(a)
    print(type(a))
a = 12
print(a, type(a))
a = "Hello"
print(a, type(a))
a = 3.14
print(a, type(a))
a = 123j
print(a, type(a))
a = ["ads", "sad", "123"]
print(a, type(a))
a = ("áds", "sdsd", 'dsd')
print(a, type(a))
a = range(5)
print(a, type(a))
a = {"name": "Duong", "age": 23}
print(a, type(a))
a = {"Duong", "Nguen", "Thai"}
print(a, type(a))
a = frozenset({1, 2, 3})
print(a, type(a))
a = True
print(a, type(a))
a = b'What'
print(a, type(a))
a = bytearray(6)
print(a, type(a))
a = memoryview(bytes(4))
print(a, type(a))
a = None
print(a, type(a))
print("\n\n")
a = str("Hello_World")
print(a, type(a))
a = 34
print(a, type(a))
