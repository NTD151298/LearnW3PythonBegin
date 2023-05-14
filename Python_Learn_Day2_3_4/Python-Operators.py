
def Python_Operators():
    while (1):
        print("\nPython Operator")
        z = int(input("Nhap 1 de tiep tuc, so khac de ket thuc: "))
        if z == 1:
            print("Hello world")
            # Lập trình luôn một máy tính vậy
            # Input is 2 integer
            a, b = int(input("Nhap a: ")), int(input("Nhap b: "))
            print("Tong cua hai so la:", a + b)
            print("Tich cua hai so la:", a * b)
            c = "{:.2E}".format(a ** b)
            print("So mu cua hai so la:", c)
            if a >= b:
                print("Hieu cua hai so la:", a - b)
            else:
                print("Hieu cua hai so la:", b - a)
            if a >= b:
                print("Thuong cua hai so la:", a / b)
            else:
                print("Thuong cua hai so la:", b / a)
            if a >= b:
                print("So du cua hai so la:", a % b)
            else:
                print("So du cua hai so la:", b % a)
            if a >= b:
                print("Phan nguyen cua hai so la:", a // b)
            else:
                print("Phan nguyen cua hai so la:", b // a)
        else:
            print("\nEnd.")
            break

# We are stop at Python Arithmetic Operators


while (1):
    print("0. Exit")
    print("1. Python basic caculator")
    z = int(input("Input: "))
    if z == 1:
        Python_Operators()
    else:
        break
