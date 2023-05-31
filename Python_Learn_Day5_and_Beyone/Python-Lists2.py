def fuc_abs_list(n):
    return (n - 50)


list1 = [32, 235, 32, 32, 42, 525, 50, 21]
list1.sort(key=fuc_abs_list)
print(list1)


class oppjeck1:
    def list_print():
        list2 = [x in x for x in list1 if x > 40]
        print(list2)


opp1 = oppjeck1
opp1.list_print()
