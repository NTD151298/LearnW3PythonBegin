# Boolean Values
print("\nBoolean Values")
# In programming you often need to know if an expression is True or False.
# You can evaluate any expression in Python, and get one of two answers, True or False.
# When you compare two values, the expression is evaluated and Python returns the Boolean answer:


def test1():
    print(15 == 15)
    print(15 == 19)
    print(15 < 123)
# Chung ta có một input để nhập xong đó


def CheckOddEven():
    while (1):
        a = int(input("Nhap so can check vao "))
        if a == 0:
            print("Ket thuc vong lap kiem nhieu tien")
            break
        if a % 2 == 0:  # Chúng ta check xem nó có chẵn hay lẻ
            print("So do la so chan")
        else:
            # Chẵn chia hết cho hai lẻ thì là ngược lại khác không
            print("So do la so le")


def Evaluate_Values_and_Variables():
    print(bool("Hello"))
    print(bool(1512))
    x, y = 1998, "Niềm Tin"
    print(bool(x))
    print(bool(y))

# Most Values are True
def Most_Values_are_True():
    print("Most Values are True")
    #Almost any value is evaluated to True if it has some sort of content.
    a = ["Hell", "Blevie"]
    b = float(23.345)
    print(bool(int(b)))
    #Any string is True, except empty strings.
    print(bool(""))
    #Any number is True, except 0.
    print(bool(0))
    #Any list, tuple, set, and dictionary are True, except empty ones.
    print(bool(a[1] == ""))

def Some_Values_are_False():
    class Test11():
        def ThuNhat():
            a = 123
            print(a)
            return a
    Ketnoi = Test11()
    Ketnoi.ThuNhat
    print(Ketnoi)
    print(bool(Ketnoi))

# Functions can Return a Boolean
def Functions_can_Return_a_Boolean1():
    def Functions_can_Return_a_Boolean():
        return True
    if Functions_can_Return_a_Boolean():
        print("Yes")
    else:
        print("No")
    x = 200
    print(isinstance(x, complex))

# Đang dừng lại ở Functions can Return a Boolean

while (1):# Cái gì nhỉ ấn số với mỗi một function là một số chúng ta gửi tín hiệu kiếm tiền 
        # if xong đó có thể đó là switch  if a = 1 thì function thứ nhất 
        print("\n0. Thoát\n1. test1\n2. CheckOddEven\n3. Evaluate_Values_and_Variables\n4. Most_Values_are_True\n5. Some_Values_are_False\n6. Functions can Return a Boolean")
        a = int(input("Nhập function muốn làm  "))
        if a == 0:
            break
        if a == 1:
            print("\n1. test1:")
            test1()
        if a == 2:
            print("\n2. CheckOddEven:")
            CheckOddEven()
        if a == 3:
             print("\n3. Evaluate_Values_and_Variables:")
             Evaluate_Values_and_Variables()
        if a == 4:
             print("\n4. Most_Values_are_True:")
             Most_Values_are_True()
        if a == 5:
            print("\n5. Some_Values_are_False:")
            Some_Values_are_False()
        if a == 6:
            print("\n6. Functions can Return a Boolean:")
            Functions_can_Return_a_Boolean1()










