"""   
  Herencia.-  la herencia es el hecho de que una clase puede permitir el uso o implementacion o compartir de los atributos y metodos. Es decir cuando una clase hereda a otra se dice que es una super clase, clase padre o principal que es la que hereda los atributos y metodos a la o las clases llamadas sub clases o clases hijas o secundaias
""" 
print("\033c")

from coches import Coches,Camiones,Camionetas
coche1 = Coches( "VW","Blanco","2022", 220,150, 5)
coche2 = Coches("Nissan","Azul","2019",180, 150, 6)
camion1 = Camiones("Dina","Negro","2020",180,300,12,8,2500)
camion2 = Camiones("Star","Azul","2019",150,200,14,6,2000)
camioneta1=Camionetas("Renault","Amarillo","2025",240,250,8,"delantera",True)
camioneta2=Camionetas("Nissan","Blanco","2020",180,150,6,"trasera",False)

# for i in range (1,101):
#     coche1.acelerar()

# print(coche1.getVelocidad())

# coche1.setVelocidad(400)
# print(coche1.getVelocidad())
