
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
