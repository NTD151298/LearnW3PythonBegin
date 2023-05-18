
def Python_Operators():
    while (1):
        print("\n\tPython Operator\n--------------------------------------------------------------------------")
        print("\t0. exit")
        print("\t1. Continue")
        z = int(input("\tInput: "))
        if z == 1:
            print("\tHello world")
            # Lập trình luôn một máy tính vậy
            # Input is 2 integer
            a, b = int(input("\ta(1 - 10): ")), int(input("\tb(1 - 10): "))
            if 1 <= a <= 10 and 1 <= b <= 10:
                print("\n\tTong cua hai so la:", a + b)
                print("\tTich cua hai so la:", a * b)
                c = "{:.2E}".format(a ** b)
                print("\tSo mu cua hai so la:", c)
                if a >= b:
                    print("\tHieu cua hai so la:", a - b)
                else:
                    print("\tHieu cua hai so la:", b - a)
                if a >= b:
                    print("\tThuong cua hai so la:", a / b)
                else:
                    print("\tThuong cua hai so la:", b / a)
                if a >= b:
                    print("\tSo du cua hai so la:", a % b)
                else:
                    print("\tSo du cua hai so la:", b % a)
                if a >= b:
                    print("\tPhan nguyen cua hai so la:", a // b)
                else:
                    print("\tPhan nguyen cua hai so la:", b // a)
            else:
                print("\tLaw said 1 to 10, u out!")
        else:
            print("\n\tEnd.")
            return belevie

# We are stop at Python Arithmetic Operators


def Python_Assignment_Operators():
    x = int(5)
    while (1):
        print("\n\tPython Assignment Operators\n--------------------------------------------------------------------------")
        print("\t0. exit")
        print("\t1. Continue")
        z = int(input("\tInput: "))
        if z == 1:
            print("\tTa co x = 5")
            a = int(input("\tNhap so tu 1 -> 10 : "))
            if 1 <= a <= 10:
                print("\n\tOperator \t Example  \tResult")
                print("\t    =    \t  x = a   \t" + str(a))
                print("\t   +=    \t  x += a  \t" + str(x+a))
                print("\t   -=    \t  x -= a  \t" + str(x-a))
                print("\t   *=    \t  x *= a  \t" + str(x*a))
                print("\t   /=    \t  x /= a  \t" + str(x/a))
                print("\t   %=    \t  x %= a  \t" + str(x % a))
                print("\t  //=    \t  x //= a \t" + str(x//a))
                print("\t  **=    \t  x **= a \t" + str(x**a))
                print("\t   &=    \t  x &= a  \t" + str(x & a))
                print("\t   |=    \t  x |= a  \t" + str(x | a))
                print("\t   ^=    \t  x ^= a  \t" + str(x ^ a))
                print("\t  >>=    \t  x >>= a \t" + str(x >> a))
                print("\t  <<=    \t  x <<= a \t" + str(x << a))
            else:
                print("\tLaw said 1 to 10, u out!")
        else:
            print("\n\tEnd.")
            return belevie


def Python_Comparison_Operators():
    while (1):
        print("\n\tPython Comparison Operators\n----------------------------------------------------------------------------------------------------------------------------------------------------")
        print("\t0. exit")
        print("\t1. Continue")
        z = int(input("\tInput: "))
        if z == 1:
            # Input is 2 integer
            a, b = int(input("\ta: ")), int(input("\tb: "))
            if a == b:
                print("\n\ta Equal b")
            if a != b:
                print("\ta Not equal b")
            if a > b:
                print("\ta Greater than b")
            if a < b:
                print("\ta Less than b")
            if a >= b:
                print("\ta Greater than or equal to b")
            if a <= b:
                print("\ta Less than or equal to b")
        else:
            print("\n\tEnd.")
            return belevie

# Python Logical Operators


def Python_Logical_Operators():
    while (1):
        print("\n\tPython Logical Operators\n----------------------------------------------------------------------------------------------------------------------------------------------------")
        print("\t0. exit")
        print("\t1. Continue")
        z = int(input("\tInput: "))
        if z == 1:
            x = int(input("\tx: "))
            if x < 1 and x < 10:
                print("\n\tx lower than 1")
            if x < 5 or x < 4:
                print("\tx lower than 5 or 4")
            if not (x < 1 and x < 10):
                print("\tx is not bout lower than 1 and lower than 10")
        else:
            print("\n\tEnd.")
            return belevie


def Python_Membership_Operators():
    while (1):
        print("\n\tPython Membership Operators\n----------------------------------------------------------------------------------------------------------------------------------------------------")
        print("\t0. exit")
        print("\t1. Continue")
        z = int(input("\tInput: "))
        if z == 1:
            Chuan = True
            A = ["Nguyen", "Thai", "Duong"]
            print("\t", A)
            a = str(input("\tInput: "))
            if a in A:
                print("\tWord in list A. Very good")
            if a == A[0]:
                print("\tWord is Nguyen, good")
            if a == A[1]:
                print("\tWord is Thai, good")
            if a == A[2]:
                print("\tWord is Duong, good")
            if a not in A:
                print("\tWord not in list A. We end here")
        else:
            print("\n\tEnd.")
            return belevie


def Python_Bitwise_Operators():
    while (1):
        print("\n\tPython Bitwise Operators Logic Gate Logic Gate\n----------------------------------------------------------------------------------------------------------------------------------------------------")
        print("\t0. exit")
        print("\t1. Continue")
        z = int(input("\tInput: "))
        if z == 1:
            x, y = int(input("\tx: ")), int(input("\ty: "))
            print("\tAND gate: ", x & y)
            print("\tOR gate: ", x | y)
            print("\tXOR gate: ", x ^ y)
            print("\tNOT gate x: ", ~x, "NOT gate y: ", ~y)
            print("\tZero fill left shift: ", x << y)
            print("\tSigned right shift gate: ", x >> y)
        else:
            print("\n\tEnd.")
            return belevie


belevie = True
print(141 - 45 - 73)
while belevie:
    print("\n--------------------------------------------------------------------------\n--------------------------------------------------------------------------")
    print("0. Exit")
    print("1. Python basic caculator")
    print("2. Python Assignment Operators")
    print("3. Python Comparison Operators")
    print("4. Python Logical Operators")
    print("5. Python Membership Operators")
    print("6. Python Bitwise Operators Logic Gate")
    z = int(input("Input: "))
    if z == 1:
        Python_Operators()
    elif z == 2:
        Python_Assignment_Operators()
    elif z == 3:
        Python_Comparison_Operators()
    elif z == 4:
        Python_Logical_Operators()
    elif z == 5:
        Python_Membership_Operators()
    elif z == 6:
        Python_Bitwise_Operators()
    else:
        belevie = False
