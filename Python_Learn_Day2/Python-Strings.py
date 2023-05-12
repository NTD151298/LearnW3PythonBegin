# Check String
print("Check String")
# To check if a certain phrase or character is present in a string, we can use the keyword in.
a = "Hello-World"
print("Fist" in a)
print("Hello" in a)  # Ham nay de check xem co cai chu do khong
print("He" in a)
print("eo" in a)
if "Wo" in a:
    print("Dung roi chu 'Wo' co trong string a")
if "lo-Wo" in a:
    print("Dung roi chu 'lo-Wo' co trong string a")
if "ldf" in a:
    print("Dung roi chu 'lo-Wo' co trong string a")
# Check if NOT
print("\nCheck if NOT")
if "ldf" not in a:
    print("Dung roi chu 'lo-Wo' khong co trong string a")
if "dfs" not in a:
    print("Chu 'dfs' khong o trong a")
if "sdf" not in a:
    print("ok chung ta tiep tuc")
if "ádf" not in a:
    print("Cu in ra lien tuc chung ta lap trinh chuong trinh in")
# Python - Slicing Strings
print("\nPython - Slicing Strings")
# Slicing
print("\nSlicing")
# You can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string.
b = "Nguyen Thai Duong"
print(b, "Leng of b is: ", len(b))
print(b[7:11])
print(a[0:4], b[0:6], b[12:17])
print(b[:6], b[12:], b[:11], b[7:])
# Negative Indexing
print("\nNegative Indexing")
# Use negative indexes to start the slice from the end of the string:
i = 0
j = 0 - len(b)
for x in b:
    print(x, i, j)
    i = i+1
    j = j+1

print(a[-5:], b[-6:-2], b[-17:])
print(b[-12:-8], b[7:-6], b[-6:-4])

# Python - Modify Strings
# Upper Case
# Lower Case
print("\nUpper Case, Lower Case")
print(a, b)
c = "Hom nay lam di lam lai"
print(c.upper(), a.upper(), b.upper())
print(c.lower(), a.lower(), b.lower())

# Remove Whitespace
print("\nRemove Whitespace")
d = "   Xep gach co time line thoi ma    "
print(d, "\n" + d.strip())
d1 = "                  sd                       "
print(d1, "\n" + d1.strip())
d2 = "                 34"
print(d2, "\n" + d2.strip())

# Replace String
print("\nReplace String")
print(a, b, c)


def thaythechu():
    a1 = a.replace("Hello", "Good")
    print("new a :", a1)
    b1 = b.replace("Nguyen", "Tran")
    print("new b :", b1)
    c1 = c.replace("Hom nay", "Ngay mai")
    print("new c :", c1)
    print("cai gi do khong o do :", a.replace("Ngu", "ASD"))


thaythechu()
print(a, 13 + 5 + 8 + 14 + 40 + 13 - 60)
