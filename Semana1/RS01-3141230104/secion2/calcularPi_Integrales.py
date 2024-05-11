import math

divisiones=10000
cuarto_area=0.0
acumulador = 0
for i in range (divisiones):
    acumulador += 1
    base_triangulo = float(acumulador)/float(divisiones)
    altura = math.sqrt(1-base_triangulo*base_triangulo)
    base=1/float(divisiones)
    cuarto_area+=base*altura
print("El cuarto del area es: ",cuarto_area)
print("Pi es igual a: ", cuarto_area*4)
