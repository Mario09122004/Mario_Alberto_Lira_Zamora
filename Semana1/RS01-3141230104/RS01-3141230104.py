import math

def AreaCuadrado():
    print("Calculate the area of the square")
    x = float(input("Please, write a side of the square: "))
    print("\n//////////////////////////////\nThe area of the square is: ", x*x,"\n//////////////////////////////\n")

def AreaCirculo():
    print("Calculate the area of the circle")
    x = float(input("Please, write the radius of the circle: "))
    print("\n//////////////////////////////\nThe area of the circle is: ", math.pi*x**2,"\n//////////////////////////////\n")

def AreaTriangulo():
    print("Calculate the area of the triangle")
    x = float(input("Please, write the base of the triangle: "))
    y = float(input("Please, write the height of the triangle: "))
    print("\n//////////////////////////////\nThe area of the triangle is: ", (x*y)/2,"\n//////////////////////////////\n")

while True:
    x = input("Please, write the letter of the Geometric Shapes \n a)Circle \n b)Square \n c)Triangle \n d)Exit \n")
    match x:
        case "a":
            AreaCirculo()
        case "b":
            AreaCuadrado()
        case "c":
            AreaTriangulo()
        case "d":
            print("Bye")
            break
        case _:
            print("Please, write a correct letter")
