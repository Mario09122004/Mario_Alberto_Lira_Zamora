import math

def pi():
    contador=0
    acumulador = 0.0
    divicion_actual=1.0
    suma=True

    while divicion_actual>0.00052:
        contador+=1
        divicion_actual=1/contador

        if contador%2 != 0:
            if suma:
                acumulador += divicion_actual
            else:
                acumulador -= divicion_actual
            suma = not suma

    return acumulador*4

print("calculate the area of the circle")
x = float(input("Please, write the radius of the circle: "))
print("The area of the circle is: ", pi()*x**2)
    