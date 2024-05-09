import math

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
print(acumulador)
print(acumulador*4)