"""  
 Programación Orinetada a Objetos POO o OOP

CLASES .- es como un molde a traves del cual se puede instanciar un objeto dentro de las clases se definen los atributos (propiedades / caracteristicas) y los métodos (funciones o acciones)

OBJETOS O INSTANCIAS .- son parte de una clase los objetos o instacias pertenecen a una clase, es decir para interacturar con la clase o clases y hacer uso de los atributos y metodos es necesario crear un objeto o objetos.
"""

#Ejemplo 1 Crear una clase (un molde para crear mas objetos)llamada Coches y apartir de la clase crear objetos o instancias (coche) con caracteristicas similares


    #Atributos o propiedades (variables)
    #Caracteristicas del coche
    #valores iniciales es posible declarar al principio de una clase
#Los atributos no pueden ser cambiados o no deben ser cambiados directamente desde el objeto, para eso se utilizan los métodos get y set para obtener y modificar los atributos de la clase.
print("\033c")

class Coches:
    marca = ""
    color = ""
    modelo = ""
    velocidad = 0
    potencia = 0
    asientos = 0

    def acelerar(self):
        self.velocidad+=1
        

    def frenar(self):
        self.velocidad -= 1

#Multiples objetos

coche1 = Coches()
coche2 = Coches()
print(f"El color del coche 1 es:\n {coche1.color}")
#Asignar asi el valor no es correcto y se debe de evitar que los atributos sean publicos
coche1.color = "Rojo y blanco"
print(f"El color del coche 1 es:\n {coche1.color}")
coche2.color = "Blanco y Negro"
print(f"El color del coche 2 es:\n {coche2.color}")
for i in range (1,11):
    coche1.acelerar()
print(f"La velocidad del coche 1 es:\n {coche1.velocidad}")
