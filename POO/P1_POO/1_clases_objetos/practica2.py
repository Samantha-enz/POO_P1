"""
Ejercicio Practico #2 “Modelar y Diagramar en POO”

"""
print("\033c")

#Clase de Coches
class Coches:
    def __init__(self,color, marca, velocidad):

        self.__color=color
        self.__marca=marca
        self.__velocidad=velocidad


    def acelerar(self):
        self.__velocidad += 1
    
    def frenar(self):
        self.__velocidad -= 1
    
    def tocar_claxon(self):
        print("Beep Beep")
        


#Instanciar o crear objetos de la clase Coches
coche1 = Coches("Blanco", "VW",220)
coche2= Coches("Azul","Nissan",180)


coche1.tocar_claxon()

coche2.tocar_claxon()

coche1.acelerar()
coche1.acelerar()
