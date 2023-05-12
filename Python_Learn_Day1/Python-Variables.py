"""
Creating Variables
Python has no command for declaring a variable.

A variable is created the moment you first assign a value to it.
"""

x = 3
y = "Mot cai gi do va viet"

print(x)
print(y)

# Variables do not need to be declared with any particular type, and can even change type after they have been set.
x = "so 3"
print(x)

# Casting
print("\nCasting")
# If you want to specify the data type of a variable, this can be done with casting.
a = int(123)
b = float(23.24)
c = int(12.23)
d = str(45)

print("a = " + str(a))
print(b)
print(c)
print(d)

#Get the Type
print("\nGet the Type")
# You can get the data type of a variable with the type() function.
x = 5
y = "Jhon"
print(type(x))
print(type(y))

#Single or Double Quotes?
print("\nSingle or Double Quotes?")
#String variables can be declared either by using single or double quotes:
x = 'so thu 3'
print("x moi:")
print(x)
print(44-23)

"""
Variable Names
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
"""
my_name = "Dương"
my_sur_name = "Nguyễn"

print(my_name + " " + my_sur_name)

my_age = 24

print(my_age + 1)

my_fist_code_line_1 = 21
my_fist_code_line_2 = 23

if (my_fist_code_line_2 > my_fist_code_line_1 ):
    print("lần code thứ 2 nhiều hơn lần code thứ nhất")

#Many Values to Multiple Variables
#Python allows you to assign values to multiple variables in one line:
print("\nMany Values to Multiple Variables ")
x, y, z = 12, 23, 34

print(x)
print(y)
print(z)

#Unpack a Collection
print("\nUnpack a Collection")
#If you have a collection of values in a list, tuple etc. 
#Python allows you to extract the values into variables. This is called unpacking.

A_Champion = ["Q", "W", "E", "R"]
A_Hero = ("Q", "W", "E", "R")
A_Player = {"Dumpe" : "Sliver" , "Skill" : 2}
a1, a2, a3, a4 = A_Champion
print(type(A_Champion))
print(type(A_Hero))
print(type(A_Player))
print(A_Player)
print(a1)
print(a2)
print(a3)
print(a4)

#Output Variables
print("\nOutput Variables")
#The Python print() function is often used to output variables.
print(a1, a2, a3, a4)
print(a1 + a2 + a3 + a4)

my_middele_name = "Thái"

print(my_sur_name, my_middele_name, my_name)

print (str(x+y+z)+" "+a1+a2+a3+a4)
print (x, "= " + a1)
print (62 - 44)

#Global Variables
print("\nGlobal Variables")
#Variables that are created outside of a function (as in all of the examples above) are known as global variables.
x = "Test 1"
def fisteverfunction():
    x = "Test 2"
    print("This is " + x)
print("khi ma gia tri x o ben ngoai = " + x )
fisteverfunction()

#The global Keyword
print("\nThe global Keyword")
#Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
#To create a global variable inside a function, you can use the global keyword.

def Test_GlobalKey_world():
    global x, my_sur_name
    my_sur_name = "Trần"
    x = "Test 3"
print("Truoc khi kich hoat Test_GlobalKey_world thi x =", x)
Test_GlobalKey_world()
print("Sau khi kich hoat Test_GlobalKey_world thi x =", x)
print(my_sur_name, my_middele_name, my_name)

#Python - Variable Exercises

carname = "Volvo"
print(93 - (44 + 18))


