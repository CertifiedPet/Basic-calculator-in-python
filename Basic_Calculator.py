
def addition_calculator():
    print(f"this is a addition calculator")
    num0 =  int(input("please enter your first number you want to add: "))
    num1  = int(input("please enter your second number you want to add: "))
    num2 = num0 + num1
    print (f"{num0} plus {num1} is: {num2}")

def subtraction_calculator():
    print(f"this is a subtraction calculator")
    num0 = int(input("please enter your first number you want to subtract: "))
    num1 = int(input("please enter your second number you want to subtract: "))
    num2 = num0 - num1
    print (f"{num0} subtracted by {num1} is: {num2}")
    
def multiplication_Calculator():
    print("this is a multiplication calculator")
    num0 = int(input("please enter your first number you want to multiply: "))
    num1 = int(input("please enter your second number you want to multiply: "))
    num2 = num0 * num1
    print (f"{num0} multiplied by {num1} is: {num2}")

def division_calculator():
    print("this is a division calculator")
    num0 = int(input("please enter your first number you want to divide: "))
    num1 = int(input("please enter your second number you want to divide: "))
    num2 = num0 / num1
    print (f"{num0} divided by {num1} is: {num2}")

def power_caluclator():
    print("this is a power calculator")
    num0 = int(input("please enter your base: "))
    num1 = int(input("please enter your power: "))
    num2 = num0 ** num1
    print (f"{num0} divided by {num1} is: {num2}")


def calculate_sqaure_area():
    print("this calculator calculates the area of a sqare")
    num0 = int(input("please enter the side length: "))
    num1 = num0 ** 2
    print (f"the length of the sqare sides: {num0}\nthe area of the sqare is: {num1}")


def calculate_rectangle_area():
    print("this calculator calculates the area of a rectangle")
    num0 = int(input("please enter the legth of the rectangle: "))
    num1 = int(input("please enter your width of the rectangle: "))
    num2 = num0 * num1
    print (f"lenth of the rectangle: {num0}\nwidth of the rectangle: {num1}\narea of the rectangle: {num2}")



def calculate_circle_area():
    print("this calculator calculates the area of a rectangle")
    num0 = int(input("please enter your radius: "))
    num1 = 3.14159265359 * num0 ** 2
    print(f"radius of the circle: {num0}\narea of the circle: {num1}")
    




cal = int(input ("""Welcome to a basic calculator, enter the following for the appropriate calculation:
1 - Multiplication 
2 - Subtraction
3 - Addition
4 - division
5 - powers
6 - area of a square 
7 - area of circle 
8 - area of rectangle

"""))

if cal == 1:
    multiplication_Calculator()

if cal == 2:
   subtraction_calculator()

if cal == 3:
    addition_calculator()

if cal == 4:
    division_calculator()

if cal == 5:
    power_caluclator()
    
if cal == 6:

    calculate_sqaure_area()

if cal == 7:
    
    calculate_circle_area()

if cal == 8:

    calculate_rectangle_area()