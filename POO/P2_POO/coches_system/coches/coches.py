import conexionBD
from coches import cochesBD
import re



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
    
    def validacion(self, texto, validacion_regex, mensaje):
        opc = True
        entrada = ""
        while opc:
            entrada = input(texto).strip()
            if re.match(validacion_regex, entrada):
                opc = False
            else:
                print(mensaje)
        return entrada

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

    # def agregar(self, marca, color, modelo, velocidad, potencia, asientos):
    #     print("\n\t\t\t...::: AGREGAR COCHE :::... \n")
    # opc = "si"
    # while opc == "si":
    #     marca = self.validacion("Marca: ", r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]{1,20}$", "Ingrese un nombre válido (A-Z, máx 20 caracteres)").upper().strip()
    #     color = self.validacion("Color: ", r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]{1,20}$", "Ingrese un nombre válido (A-Z, máx 20 caracteres)").upper().strip()
    #     modelo = self.validacion("Modelo: ", r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]{1,20}$", "Ingrese un nombre válido (A-Z, máx 20 caracteres)").upper().strip()
    #     velocidad = int(self.validacion("Velocidad: ", r"^\d+(\.\d{1,5})?$", "Ingrese un valor numérico correcto"))
    #     potencia = int(self.validacion("Potencia: ", r"^\d+(\.\d{1,5})?$", "Ingrese un valor numérico correcto"))
    #     asientos = int(self.validacion("Asientos: ", r"^\d+(\.\d{1,5})?$", "Ingrese un valor numérico correcto"))
    
        
        
#         respuesta = cochesBD.insertar(marca, color, modelo, velocidad, potencia, asientos)
#         if respuesta:
#             funciones.accionExitosa()
#         else:
#             funciones.accionNoExitosa()
        
#         opc = ""
#         while opc != "si" and opc != "no":
#             opc = input("¿Deseas agregar otro coche? (si/no) ").lower().strip()
# self.esperarTecla()

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
