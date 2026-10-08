#Clase Principal 
print("\033c")

class Coches:
    def __init__(self, marca,color,modelo, velocidad, potencia, asientos):
        #La variable que se recibe se asigna al atributo
        #El metodo constructor se utiliza solamente una vez cada que se crea un objeto
        self._marca=marca
        self._color=color
        self._modelo=modelo
        self._velocidad=velocidad
        self._potencia=potencia       
        self._asientos=asientos

    def acelerar(self):
        self._velocidad+=1  

    def frenar(self):
        self._velocidad -= 1

    def getMarca(self):
        return self._marca

    def setMarca(self,marca):
        self._marca=marca

    def getColor(self):
        return self._color

    def setColor(self,color):
        self._color=color

    def getVelocidad(self):
        return self._velocidad

    def setVelocidad(self,velocidad):
        self._velocidad=velocidad

    def getPotencia(self):
        return self._potencia

    def setPotencia(self,potencia):
        self._potencia=potencia

    def getAsientos(self):
        return self._asientos
    
    def setAsientos(self,asientos):
        self._asientos=asientos

class Camiones(Coches):
    def __init__(self,marca,color,modelo,velocidad,potencia,asientos,eje,capacidadCarga):
        super().__init__(marca,color,modelo,velocidad,potencia,asientos)
        self.__eje= eje
        self.__capacidadCarga= capacidadCarga
    
    def cargar(self,tipo_carga):
        print(f"Tipo de carga es {tipo_carga} ")

    def acelerar(self):
        self._velocidad += 1
        print("Estoy acelerando como un camion")

    def frenar (self):
        self._velocidad -= 1
        print("Freno como camion")

    def getEje(self):
        return self.__eje

    def setEje(self,eje):
        self.__eje=eje

    def getCapacidadCarga(self):
        return self.__capacidadCarga

    def setCapacidadCarga(self,capacidadCarga):
        self.__capacidadCarga=capacidadCarga

class Camionetas(Coches):

    def __init__(self,marca,color,modelo,velocidad,potencia,asientos,traccion,cerrada):
        super().__init__(marca,color,modelo,velocidad,potencia,asientos)
        self.__traccion= traccion
        self.__cerrada= cerrada
    
    def transportar(self,num_pasajeros):
        print(f"El número de pasajeros de la camioneta es: {num_pasajeros}")

    def acelerar(self):
        self._velocidad += 1
        print("Estoy acelerando como una camioneta")

    def frenar (self):
        self._velocidad -= 1
        print("Freno como camioneta")
    
    def getTraccion(self):
        return self.__traccion
    
    def setTraccion(self,traccion):
        self.__taccion=traccion

    def getCerrada(self):
        return self.__cerrada

    def setCerrada(self,cerrada):
        self.__cerrada = cerrada

# class CamionesCarga(Camiones):
#     def __init__(self,marca,color,modelo,velocidad,potencia,asientos,eje,capacidadCarga,tipoCarga):
#         super().__init__(marca,color,modelo,velocidad,potencia,asientos,eje,capacidadCarga)
#         self.__tipoCarga= tipoCarga

#     def getTipoCarga(self):
#         return self.__tipoCarga

#     def setTipoCarga(self,tipoCarga):
#         self.__tipoCarga=tipoCarga

# print(CamionesCarga.mro()) 

    