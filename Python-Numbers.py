# Python Numbers
# There are three numeric types in Python: int float complex

import random
x, y, z = 21, 32.21, 45j
print(x, type(x), y, type(y), z, type(z))

x, y, z = 1323232323233232323, -123123124124124, 0
print(x, type(x), y, type(y), z, type(z))

a, b, c = float(x), complex(y), int(z)
print(a, type(a), b, type(b), c, type(c))

# Random Number
print("\nRandom Number")
# Python does not have a random() function to make a random number,
# but Python has a built-in module called random that can be used to make random numbers:

print("so ngau nhien tu 0 den 100:", random.randrange(0, 100))
print("\nExerise endless:")
x1, y1, z1 = 34, 93.23, 3j
print(x1, type(x1), y1, type(y1), z1, type(z1))
x2, y2, z2 = float(x1), complex(y1), int(y1)
print(x2, type(x2), y2, type(y2), z2, type(z2))
print(25-10)
