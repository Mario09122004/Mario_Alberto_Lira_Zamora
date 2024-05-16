class FiguraGeometricas():

    ubicacion_x = 0
    ubicacion_y = 0

    def __init__(self):
        None

    def get_area(self):
        return 999999999.9
    
    def modificar_x(self,x):
        self.ubicacion_x = x

    def modificar_y(self,y):
        self.ubicacion_y = y

class Rectangulo(FiguraGeometricas):

    alto = 0.0
    base = 0.0
    
    #esta funciones estan divididas dentro de la propia clase para que furule se tiene que llamar 
    #para buena practica es mejor usar la llamada self
    def __init__(self,alto,base): #variables de clase
        self.alto = float(alto) #llama a contenido dentro de la clase
        self.base = float(base)

    def __str__(self):
        return "Es un rectangulo, con area: " + str(self.get_area())
    
    def get_area(self):  #variables de clase
        return self.alto * self.base
    
class Circulo(FiguraGeometricas):
    None #tarea

class Triangulo(FiguraGeometricas):
    None #tarea

#iaqui esta nuestro codigo
import turtle

prueba = Rectangulo(2,2)
print(str(prueba.get_area()))

#el termino self es un metodo para que me llame a si mismo 
#metodo get y self son necesarios para evitar modificaciones a distincion entre

#Tarea
#Terminar circulo y triangulo
#Realizar proyecto semanal 1
#Dibujar figura c/ turtle (opcional)