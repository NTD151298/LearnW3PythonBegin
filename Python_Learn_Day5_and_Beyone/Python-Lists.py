
# List Items - Data Types
print("String list be like: ")
my_list = ["Toi", 'Roi', 'cai', 'Gi']
print(my_list, my_list[0], my_list[1], my_list[2], my_list[3])
print("leng of list is: ", len(my_list))
print("\nInterger list be like: ")
list_Day7 = [20, 15, 12, 98, 19, 1, 2, 5, 3, 2, 5, 3, 34, 92, 43]
print(list_Day7)
print("leng of list is: ", len(list_Day7))
print("\nBoolen list be like: ")
list_boolen = [True, False, True, True, False]
print(list_boolen)
print("leng of list is: ", len(list_boolen))
print("\nSum of 3 of the list: ")
list_combie = list_Day7 + list_boolen + my_list
print(list_combie)
print("leng of list is: ", len(list_combie))

This_list = list(("aple", "man", "good", "gun"))
print("\nThis_list = list((\"aple\", \"man\", \"good\", \"gun\")): ")
print(This_list)

# There are four collection data types in the Python programming language:
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

# Python - Access List Items
print("\nPython - Access List Items")
list_cout = ['Hom', 'nay', 'la', 'mot', 'cai']
i = 0
j = - len(list_cout)
for x in list_cout:
    print(x + "\t" + str(i) + "\t" + str(j))
    i = i + 1
    j = j + 1
if "Hom" in list_cout:
    print("Hom co trong list_cout")
print("leng of list is: ", len(list_cout))  # chúng ta đang có ý
print(list_cout[2:], list_cout[-3:])
print("Hello world")

# Change Item Value
print("\nChange Item Value")
list_duong1 = ["nguyen", "thai", "duong", 1512]
i, j = 0, - len(list_duong1)
for x in list_duong1:
    print(x, "\t", i, "\t", j)
    i += 1
    j += 1
list_duong1[0], list_duong1[1] = "Tran", "Huyen"
print("\nTest new list after change the fist and second string")
i, j = 0, - len(list_duong1)
for x in list_duong1:
    print(x, "\t", i, "\t", j)
    i += 1
    j += 1
# Change a Range of Item Values
print(list_duong1[-3:-1])
list_duong1[-3:-1] = ['Binh', 'Duong']
print(list_duong1[-3:-1])
list_duong1[4:] = ['ngay', 'sinh', 'cua', 'toi', 15, 12, 1998]
print(list_duong1, len(list_duong1))
# Insert Items
print("\nInsert Items")
this_new_list = ['nguyen', 'hoang', 'duong']
print(this_new_list)
this_new_list.insert(3, 'Thanh')
print(this_new_list)
this_new_list.insert(0, 'Tran')
print(this_new_list)
this_new_list.insert(1, 'Dai')
print(this_new_list)
this_new_list[0] = 'Tran1'
print(this_new_list)

# Add List Items
print("\nAdd List Items")
# Append Items
this_new_list.append('Trieuuu')
print(this_new_list)

# Remove Specified Item
print("\nRemove Specified Item")
print("this_new_list.remove('Trieuuu'): ")
this_new_list.remove('Trieuuu')
print(this_new_list)
print("this_new_list.remove('duong')")
this_new_list.remove('duong')
print(this_new_list)
print("this_new_list.pop(0): ")
this_new_list.pop(0)
print(this_new_list)
print("del this_new_list[1]: ")
del this_new_list[1]
print(this_new_list)
print("this_new_list.clear(): ")
this_new_list.clear()
print(this_new_list)
print("del this_new_list: ")
del this_new_list
print("this_new_list = 12: ")
this_new_list = 12
print(this_new_list)

# Loop Through a List
print("\nLoop Through a List")
list_duong2 = ['code    ', 'game    ', 'dopamine', 'live    ', 'job     ']
print(list_duong2)
i, j = 0, - len(list_duong2)
for x in list_duong2:
    print(x + "\t" + str(i) + "\t" + str(j))
    i += 1
    j += 1
print("\nfor x in range(len(list_duong2)):")
for x in range(len(list_duong2)):
    print(list_duong2[x] + "\t" + str(x))
a = range(1, 20, 3)
print("\nfor x in a:")
for x in a:
    print(x)
# Using a While Loop
print("\nUsing a While Loop")
i = 0
j = - len(list_duong2)
while i < len(list_duong2):
    print(list_duong2[i] + "\t" + str(i) + "\t" + str(j))
    i += 1
    j += 1

# List Comprehension
print("List Comprehension")
list_duong_new = []
for x in list_duong2:
    if "e" in x:
        list_duong_new.append(x)
print(list_duong_new)
list_duong_new1 = []
for x in list_duong2:
    if "a" in x:
        list_duong_new1.append(x)
print(list_duong_new1)
print(list_duong2)
# The Syntax
print("\nThe Syntax")

list_duong_new2 = list(x for x in list_duong2 if x != 'job     ')
print(list_duong_new2)
list_duong_new2 = list(x for x in list_duong2 if x == 'job     ')
print(list_duong_new2)
list_duong_new2 = list(x for x in list_duong2 if x != 'dopamine')
print(list_duong_new2)
list_duong_new2 = list(x for x in list_duong2)
print(list_duong_new2)
new_list = list(x for x in range(10, 100, 10))
print(new_list)
new_list = list(x for x in range(10, 100, 10) if x < 50)
print(new_list)
new_list = list(x for x in range(10, 100, 10) if x < 80)
print(new_list)
new_list = list(x.upper() for x in list_duong2 if x != "job     ")
print(new_list)
new_list_01 = list(x.lower() for x in new_list if x != "GAME    ")
print(new_list_01)
new_list_02 = list('hello' for x in new_list_01)
print(new_list_02)
new_list_02 = list(range(1, 10, 2) for x in new_list_01)
print(new_list_02)
new_list_03 = list(x for x in new_list_01 if x != 'code    ')
print(new_list_03)
new_list_03 = list(x for x in new_list_01 if x != '123    ')
print(new_list_03)
new_list_03 = list(x if x != '123    ' else 'code    ' for x in new_list_01)
print(new_list_03)
new_list_03 = list(x if x != 'code    ' else '555    ' for x in new_list_01)
print(new_list_03)

# Sort List Alphanumerically
print("\nSort List Alphanumerically")
list_duong_new3 = ["Nguyen", "Thai", "Duong",
                   1512, 1998, 20, 1, 6, 369, "dang", "hoc", "lap", "trinh"]
print(list_duong_new3)
print(type(list_duong_new3), "Leng of list_duong_new3 is:", len(list_duong_new3))
list_duong_new3.sort(key=str)
print(list_duong_new3)
list_duong_new4 = list(x for x in list_duong_new3 if not isinstance(x, int))
list_duong_new5 = list(x for x in list_duong_new3 if not isinstance(x, str))
list_duong_new5.sort()
list_duong_new4.sort()
print(list_duong_new4)
print(list_duong_new5)
# Sort Descending
print("\nSort Descending")
abc = True
list_duong_new3.sort(key=str, reverse=abc)
print(list_duong_new3)
list_duong_new4.sort(reverse=abc)
print(list_duong_new4)
list_duong_new5.sort(reverse=abc)
print(list_duong_new5)

# Customize Sort Function
print("\nCustomize Sort Function")
# You can also customize your own function by using the keyword argument key = function.
# The function will return a number that will be used to sort the list (the lowest number first):


def funcion_001(n):
    return abs(n - 500)


number_list = [24, 15, 12, 98, 19, 60, 66, 69, 100, 50]
print(number_list)
number_list.sort(key=funcion_001)
print(number_list)

# Case Insensitive Sort
print("\nCase Insensitive Sort")
random_list = ['daui', 'Bay', 'ooks', 'QWE', 'Azlxo']
print(random_list)
random_list.sort()
print(random_list)
random_list.sort(key=str.lower)
print(random_list)
random_list.sort(key=str.upper)
print(random_list)
# Reverse Order
print("\nReverse Order")
# What if you want to reverse the order of a list, regardless of the alphabet?
# The reverse() method reverses the current sorting order of the elements.
print(random_list, len(random_list))
random_list.reverse()
print(random_list, len(random_list))
print(236 - 204)
