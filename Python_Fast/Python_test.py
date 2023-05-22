def input_s():
    while True:
        s = input("Nhập chuỗi s: ")
        if 1 <= len(s) <= 15 and all(c in ['I', 'V', 'X', 'L', 'C', 'D', 'M'] for c in s):
            return s
        print("Chuỗi s không hợp lệ. Vui lòng thử lại.")


# Sử dụng hàm input_s để nhập chuỗi s
s = input_s()
num_add = 0
print("Chuỗi s đã nhập:", s)
num_add = 0
i = 0
while i < len(s):
    if s[i] == 'M':
        num = 1000
    elif s[i] == 'D':
        num = 500
    elif s[i] == 'C':
        if i+1 < len(s) and s[i+1] == 'D':
            num = 400
            i += 1
        elif i+1 < len(s) and s[i+1] == 'M':
            num = 900
            i += 1
        else:
            num = 100
    elif s[i] == 'L':
        num = 50
    elif s[i] == 'X':
        if i+1 < len(s) and s[i+1] == 'L':
            num = 40
            i += 1
        elif i+1 < len(s) and s[i+1] == 'C':
            num = 90
            i += 1
        else:
            num = 10
    elif s[i] == 'V':
        num = 5
    elif s[i] == 'I':
        if i+1 < len(s) and s[i+1] == 'V':
            num = 4
            i += 1
        elif i+1 < len(s) and s[i+1] == 'X':
            num = 9
            i += 1
        else:
            num = 1
    num_add += num
    i += 1

print(num_add)
