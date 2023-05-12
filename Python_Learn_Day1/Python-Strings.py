# Assign String to a VariableAssign String to a Variable
print("Hello String")
a = "Hello mot lan nua"
a1, b1, c1 = "Nguyen", "Thai", "Duong"
print(a[0], a, a[16])
print(a1, b1, c1)
abc1 = (a1, b1, c1)

# Multiline Strings
print("\nMultiline Strings")
a = """Va bay gio chung ta noi truoc day cung van noi ma cha qua vn vs thailan dang thua thoi """
print(a, "\n", abc1)

# Looping Through a String
print("\nLooping Through a String")
# Since strings are arrays, we can loop through the characters in a string, with a for loop.
for x in "Duong":
    print(x)
for x in "Nguyen":
    print(x)
for x in "Thai":
    print(x)

# String Length
print("\nString Length")
print(a)
print("leng of a is :", len(a))

b = "Va chung ta di theo dong luc cua the gioi mo ngay do la lap di lap lai"
print("leng of b is :", len(b))

c = str("Lap Di Lap Lai")
for x in c:
    print(x)
print("leng of c is : ", len(c))

d = str("Chung ta se ket thuc buoi luyen tap tranh burnout voi con game tich diem")
print(d, "\nleng d is : ", len(d))

print(len(abc1), len(a1), len(b1), len(c1))
print(33 - 15)
