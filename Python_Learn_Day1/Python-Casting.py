# Specify a Variable Type
a = int(232.42)
b = int("34343")
c = int(-434)
print("\nInt: ")
print(a, type(a), b, type(b), c, type(c))

a1, b1, c1 = float(a), float(b), float(c)
d1 = float("43.34")
print("\nFloat: ")
print(a1, type(a1), b1, type(b1), c1, type(c1), d1, type(d1))

a2, b2, c2 = str(a), str(b), str(c)
d2 = float("43.34")
print("\nString: ")
print(a2, type(a2), b2, type(b2), c2, type(c2), d2, type(d2))
