s = "3[as2[cd]]"
while (1):
    a = int(0)
    index = next((i for i, c in enumerate(s) if c.isdigit()), None)
    if index is not None:
        a = int(s[index])
        new_s = s[index+1:]
        s = a*new_s


print(a)
print(s)
