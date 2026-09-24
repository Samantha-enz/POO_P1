"""
 Practica # 1 Implementar ejercicio el paradigma estructurado VS OO

 Elaborar un programa que calcule el area de un rectangulo
"""

print("\033c")

#Implementar el paradigma estructurado
def calcular_area_rectangulo(base, altura):
    return base * altura



#Implementar el paradigma Orientado a Objetos (OO)
class Rectangulo: 
    def _init_(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura
    
class Rectangulos:
    def area(self,base, altura):
        area = base * altura
        return area
rectangulo1 = Rectangulos()
print (f"El rectangulo es: {rectangulo1.area(5, 6)}")
