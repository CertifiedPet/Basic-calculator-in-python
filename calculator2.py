end = 1

while end == 1:
    selection = int(input(f""" 
    welcome to the calculator of calculations 
    1 - area of a square 
    2 - area of circle 
    3 - area of rectangle
    4 - area of rhombus
    5 - addition
    6 - subtraction 
    7 - square root/powers
    8 - pythagorean theorem (hypotnuse)
    9 - pythagorean theorem (leg)
    10 - multiplication
    11 - division
    666 - kill switch
    """))
    total_selections = 1 or 2 or 3 or 4

    if selection == 666:
        end = 0

    def division (a: float, b: float):
        return (a / b)

    def pythagorean_theorem (a: float, b: float):

     return (a ** 2 + b ** 2)**.5

    def pythagorean_theorem_leg (hypotnuse: float, leg: float):

     return (hypotnuse ** 2 - leg ** 2)**.5

    def square_powers (num0:float,  num1:float ):
        return num0 ** num1

    def subtraction_func (addnum0: float, addnub1: float):
        return addnum0 - addnub1

    def area_of_rhombus (plength: float, qlength ):
        return (plength * qlength) / 2

    def area_of_rectangle (length: float, width: float):
        return length * width 

    def addition (num0: float, num1: float):
        return num0 + num1

    def area_of_square (side: float): 
        return side ** 2

    def area_of_circle (radius: float):
        return 3.14159265359 * radius ** 2

    def multiplication_func (num0:float,  num1:float ):
        return num0 * num1


    if selection == 1:
        addnum0 = float(input("enter side length: "))
        print(area_of_square(float(addnum0)))

    elif selection == 2:
        addnum0 = float(input(f"enter radius: "))
        print (area_of_circle(float(addnum0)))

    elif selection == 3:
        addnum0 = (input("enter length: "))
        addnum1 = (input("enter width: "))
        area = area_of_rectangle (float(addnum0), (float)(addnum1))
        print(area)

    elif selection == 4:
        addnum0 = input("enter p length: ")
        addnum1 = input("enter q length: ")
        area = area_of_rhombus (float(addnum0), (float)(addnum1))
        print(area)
    
    elif selection == 5:
        addnum0 = input("enter number 1: ")
        addnum1 = input("enter number 2: ")
        area = addition ((float)(addnum0), (float)(addnum1))
        print(area)


    elif selection == 6:
        addnum0 = input("enter number 1: ")
        addnum1 = input("enter number 2: ")
        area = subtraction_func ((float) (addnum0), (float)(addnum1))
        print(area)

    elif selection == 7:
        addnum0 = input("enter base: ")
        addnum1 = input("enter power: ")
        area = square_powers ((float) (addnum0), (float)(addnum1))
        print(area)
    
    elif selection == 8:
        addnum0 = input("enter A: ")
        addnum1 = input("enter B: ")
        area = pythagorean_theorem ((float)(addnum0), (float)(addnum1))
        print(area)

    elif selection == 9:
        addnum0 = input("enter hypotnuse: ")
        addnum1 = input("enter leg: ")
        area = pythagorean_theorem_leg ((float)(addnum0), (float)(addnum1))
        print(area)
    
    elif selection == 10:
        addnum0 = input("enter enter number 1: ")
        addnum1 = input("enter enter number 2: ")
        area = multiplication_func ((float)(addnum0), (float)(addnum1))
        print(area)

    elif selection == 11:
        addnum0 = input("enter enter number 1: ")
        addnum1 = input("enter enter number 2: ")
        area = division ((float)(addnum0), (float)(addnum1))
        print(area)

    else: 
        if end == 1:
            print (f"{selection} is not valid ") 
