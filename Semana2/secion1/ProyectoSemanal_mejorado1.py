import math

class Escoje():
    def  __init__(self):
        while True:
            x = input("Please, write the letter of the Geometric Shapes \n a)Circle \n b)Square \n c)Triangle \n")
            match x:
                case "a":
                    Circulo.area()
                    break
                case "b":
                    Cuadrado.area()
                    break
                case "c":
                    Triangulo.area()
                    break
                case _:
                    print("Please, write a correct letter")

class Cuadrado():

    def area():
        print("Calculate the area of the square")
        x = float(input("Please, write a side of the square: "))
        print("\n//////////////////////////////\nThe area of the square is: ", x*x,"\n//////////////////////////////\n")

class Triangulo():

    def area():
        print("Calculate the area of the triangle")
        x = float(input("Please, write the base of the triangle: "))
        y = float(input("Please, write the height of the triangle: "))
        print("\n//////////////////////////////\nThe area of the triangle is: ", (x*y)/2,"\n//////////////////////////////\n")

class Circulo():

    def area():
        print("Calculate the area of the circle")
        x = float(input("Please, write the radius of the circle: "))
        print("\n//////////////////////////////\nThe area of the circle is: ", math.pi*x**2,"\n//////////////////////////////\n")

while True:
    mario = Escoje()
    y = input("Do you like repeat? y/n ")
    if y == "n" or y == "no" or y == "No" or y == "NO" or y == "no" or y == "N":
        break