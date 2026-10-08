#Ejemplo 1 Crear una clase (un molde para crear mas objetos)llamada Coches y apartir de la clase crear objetos o instancias (coche) con caracteristicas similares

class Coches:
    def __init__(self, marca,color,modelo, velocidad, potencia, asientos):
        #La variable que se recibe se asigna al atributo
        #El metodo constructor se utiliza solamente una vez cada que se crea un objeto
        self.__marca=marca
        self.__color=color
        self.__modelo=modelo
        self.__velocidad=velocidad
        self.__potencia=potencia
        self.__asientos=asientos

    def acelerar(self):
        self.__velocidad+=1  

    def frenar(self):
        self.__velocidad -= 1

    def getMarca(self):
        return self.__marca

    def setMarca(self,marca):
        self.__marca=marca

    def getColor(self):
        return self.__color

    def setVelocidad(self,color):
        self.__color=color

    def getVelocidad(self):
        return self.__velocidad

    def setVelocidad(self,velocidad):
        self.__velocidad=velocidad

    def getPotencia(self):
        return self.__potencia

    def setPotencia(self,potencia):
        self.__potencia=potencia

    def getAsientos(self):
        return self.__asientos
    
    def setAsientos(self,asientos):
        self.__asientos=asientos

# Crear los metodos setters y getters .- estos metodos son importantes y necesarios en todos clases para que el programador interactue con los valores de los atributos a traves de estos metodos ... digamos que es la manera mas adecuada y recomendada para solicitar un valor (get) y/o para ingresar o cambiar un valor (set) a un atributo en particular de la clase a traves de un objeto. 
# En teoria se deberia de crear un metodo Getters y Setters por   cada atributo que contenga la clase
# Los metodos get siempre regresan valor es decir el valor de la propiedad a traves del return
# Por otro lado el metodo set siempre recibe parametros para cambiar o modificar el valor del atributo o propiedad en cuestion

