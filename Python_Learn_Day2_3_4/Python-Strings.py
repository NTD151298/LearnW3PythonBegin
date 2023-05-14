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

# Split String
print("\nSplit String")


def chiachu():
    a1 = a.split("e")
    print("new a1 :", a1, type(a1))
    for x in a1:
        print(x)


chiachu()

# String Concatenation
print("String Concatenation")
a = "Nguyen"
b = "Thai"
c = "Duong"
abc = [a, b, c]
d = a + " " + b + " " + c
print(d, len(d), type(d))
print(abc, len(abc), type(abc))


def Nhandoi():
    global D, D1
    A, A1 = a.upper(), a.lower()
    B, B1 = b.upper(), b.lower()
    C, C1 = c.upper(), c.lower()
    D = A + " " + B + " " + C
    D1 = A1 + " " + B1 + " " + C1


print("Sau khi nhan doi:")
Nhandoi()
print(d, len(d), type(d))
print(D, len(D), type(D))
print(D1, len(D1), type(D1))

# String Format
print("\nString Format")
x = 24
t = "Toi nam nay {} tuoi"
xt = t.format(x)
print(xt)


def DutsoVaoChu():
    d1 = d.replace("Duong", "Duong nam nay {} tuoi")
    d2 = d1.format(x)
    print(d2)


# Cu phai thay doi ten tuoi lien tuc
DutsoVaoChu()
print(13+9+10+13+40+14+8+5+13-60)

# Escape Character
print("\nEscape Character")
# To insert characters that are illegal in a string, use an escape character.
# An escape character is a backslash \ followed by the character you want to insert.
# An example of an illegal character is a double quote inside a string that is surrounded by double quotes:
# \' Single Quote
print("Single \' Chung ta dang \' Quote")
print("Backslash of an \\ Ten tui la cham chi chang \\ what for what ")
print("\nNew Line")
print("\rCarriage Return")
print("\tTab")
print("Food\bBackspace")
print("\fForm Feed")
print("\ooo	Octal value \141\142\143\144\145\146")
print("\x63", "\x64", "\x66")
print(d)

# String Methods
print("\nString Methods")
t = "co cai gi do thoi"
t1 = "CHUNG TA DANG TU TIM HIEU"
# capitalize() Converts the first character to upper case
print(t, ".sau khi su dung capitalize() : ", t.capitalize())
# casefold() Converts string into lower case
print(d, ".sau khi su dung casefold()", d.casefold())
# center() Returns a centered string
print(d, ".sau khi su dung center(30, \"-\")", d.center(30, "-"))
# count() Returns the number of times a specified value occurs in a string
print(d, ".sau khi su dung count(\"n\")", d.count("n"))
# encode()	Returns an encoded version of the string
txt = "My name is Ståle"
print(txt, ".sau khi su dung encode()", txt.encode())
print(txt, ".sau khi su dung encode()", txt.encode(
    encoding="ascii", errors="backslashreplace"))
print(txt, ".sau khi su dung encode()", txt.encode(
    encoding="ascii", errors="ignore"))
print(txt, ".sau khi su dung encode()", txt.encode(
    encoding="ascii", errors="namereplace"))
print(txt, ".sau khi su dung encode()", txt.encode(
    encoding="ascii", errors="replace"))
print(txt, ".sau khi su dung encode()", txt.encode(
    encoding="ascii", errors="xmlcharrefreplace"))
# endswith() Returns true if the string ends with the specified value
print(d, ".sau khi su dung endswith(\"ng\")", d.endswith("ng"))
# expandtabs()	Sets the tab size of the string


def expandtabsNEW():
    d = "H\te\tl\tl\to"
    print(d, ".sau khi su dung expandtabs()", d.expandtabs())
    print(d, ".sau khi su dung expandtabs(0)", d.expandtabs(0))
    print(d, ".sau khi su dung expandtabs(1)", d.expandtabs(1))
    print(d, ".sau khi su dung expandtabs(2)", d.expandtabs(2))
    print(d, ".sau khi su dung expandtabs(3)", d.expandtabs(3))
    print(d, ".sau khi su dung expandtabs(4)", d.expandtabs(4))


expandtabsNEW()

print(d)
# find() Searches the string for a specified value and returns the position of where it was found
print(d, ".sau khi su dung find(\"Thai\")", d.find("Thai"))
print(d, ".sau khi su dung find(\"34\")", d.find("34"))
print(d, ".sau khi su dung index(\"Thai\")", d.index("Thai"))
# format()	Formats specified values in a string


def formatNEW():
    d = "Nguyen {coccon:<2f} Duong"
    print(d.format(coccon=69))


formatNEW()
print(214 - 155)

t1 = "Chung ta tin {muc_do_tin} gửi tâm linh code kiếm cho chúng ta {luong} lương hàng tháng tin vào".format(
    muc_do_tin="Tuyệt Đối", luong=10000)
print(t1)

t2 = "Every thing we do we code {0} beleving to it make us {1}".format("By", "Money")
print(t2)

t3 = "For what ever the code is we belevie {} to send it to fill our trust we will make {}".format("100%", "Money")
# https://www.w3schools.com/python/ref_string_format.asp