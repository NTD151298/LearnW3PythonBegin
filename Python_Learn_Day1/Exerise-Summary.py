# Exerise-Summary
print("Chung ta se luyen tap khoang 30' chia ra 10 phut cach mot hoat dong sau do nghi")
a = "Chung ta dang luyen tap"
print(a, "len(a) is :", len(a))
print("Len tap chung vao cai lung nhi chung ta cu the\nVi don gian hon do la cu lam viet ra thoi")
print("La mot ke sang tao\t nhung cai chu mau me\t va co the tap chung ma")
x, x1, x2, x3 = int(34), int(43), float(93.43), complex(43j)
print("x =", x, type(x), x1, type(x1), x2, type(x2), x3, type(x3))
y, y1, y2, y3 = float(x), float(x1), int(x2), str(x3)
print("y =", y, type(y), y1, type(y1), y2, type(y2), y3, type(y3))
if y < x:
    print("1test y < x")
if y >= x:
    print("2test y >= x")
if y1 < x1:
    print("3test y1 < x1")
if y1 >= x1:
    print("4test y1 >= x1")
if y2 < x2:
    print("5test y2 < x2")
if y2 >= x2:
    print("6test y2 >= x2")


def testgloble1():
    x = int(123)
    x1 = float(3.14)
    x2 = complex(9j)
    x3 = str(2323)


print("\nIn cac so x x1 x2 x3 binh thuong:")
print("x =", x, type(x), "x1 =", x1, type(x1),
      "x2 =", x2, type(x2), "x3 =", x3, type(x3))
testgloble1()
print("\nSau khi testgloble1")
print("x =", x, type(x), "x1 =", x1, type(x1),
      "x2 =", x2, type(x2), "x3 =", x3, type(x3))


def testgloble2():
    global x, x1, x2, x3
    x = int(123)
    x1 = float(3.14)
    x2 = complex(9j)
    x3 = str(2323)


testgloble2()
print("\nSau khi testgloble2")
print("x =", x, type(x), "x1 =", x1, type(x1),
      "x2 =", x2, type(x2), "x3 =", x3, type(x3))


def testgloble3():
    y = float(x)
    y1 = str(x1)
    y2 = str(x2)
    y3 = int(x3)
    print("\nIn trong Ham testgloble3")
    print("y =", y, type(y), "y1 =", y1, type(y1),
          "y2 =", y2, type(y2), "y3 =", y3, type(y3))


testgloble3()
