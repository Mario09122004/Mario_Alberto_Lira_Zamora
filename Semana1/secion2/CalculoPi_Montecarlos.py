import random
import math

cuantos=10000
cuantossi=0
for i in range(cuantos):
    x=random.random()
    y=random.random()

    y_calculada = math.sqrt(1-x*x)
    if y>y_calculada:
        None
    else:
        cuantossi += 1

cuantos_area=float(cuantossi)/float(cuantos)
print("El cuardo de pi es: ",cuantos_area)
print("Pi es: ",cuantos_area*4)

