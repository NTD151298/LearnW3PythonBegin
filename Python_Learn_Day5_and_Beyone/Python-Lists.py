
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
