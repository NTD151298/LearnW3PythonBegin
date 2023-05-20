list1 = ["a", "b", "c"]
list2 = [199, 18, 15, 12, 3, 23, 2, 92, 12, 3]
list2.sort(reverse=True)


def sort_new(a):
    return abs(a - 500)


thislist = ["banana", 'a',  "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key=sort_new)
print(thislist)
print(list2)
print(list1)
