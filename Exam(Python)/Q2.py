import sys


def circleParameter(radius):
    return str(2*3.14*radius)
def recParameter(height,width):
    return str(2*(height+width))
def squParameter(side):
    return str(4*side)

def circleArea(radius):
    return str(3.14*radius*radius)
def recArea(height,width):
    return str(height*width)
def squArea(side):
    return str(side*side)


print("WELCOME TO A SIMPLE MENSURATION PROGRAM")

print("MAIN MENU")
print("1. Calculate Parameter")
print("2. Calculate Area")
print("3. Exit")

choice = int(input("Enter Choice : "))

if choice == 1:
    r = int(input("Enter circle radius : "))
    h = int(input("Enter Rectangle Height :"))
    w = int(input("Enter Rectangle width :"))
    s= int(input("Enter Square side : "))
    print(str("Circle parameter is : "+circleParameter(r)))
    print(str("Square parameter is : "+squParameter(s)))
    print(str("Rectangle parameter is : "+recParameter(h,w)))
elif choice == 2:
    r = int(input("Enter circle radius : "))
    h = int(input("Enter Rectangle Height :"))
    w = int(input("Enter Rectangle width :"))
    s = int(input("Enter Square side : "))
    print(str("Circle Area is :" +circleArea(r)))
    print(str("Square Area is : "+squArea(s)))
    print(str("Rectangle Area is :"+recArea(h,w)))
elif choice == 3:
    sys.exit("Exit")
else:
    print("out of range")