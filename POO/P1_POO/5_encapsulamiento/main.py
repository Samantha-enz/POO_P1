#Programa principal desde la que se manda llamar los objetos de la clase de coches
print("\033c")

from coches import Coches,Camiones,Camionetas
coche1 = Coches( "VW","Blanco","2022", 220,150, 5)
coche2 = Coches("Nissan","Azul","2019",180, 150, 6)

for i in range (1,101):
    coche1.acelerar()

print(coche1.getVelocidad())

coche1.setVelocidad(400)
print(coche1.getVelocidad())






