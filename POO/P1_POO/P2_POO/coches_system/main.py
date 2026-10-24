from coches import cochesBD,coches

'''
Agregar tabla de camiones que sea sin herencia
Utilizar la clase coches para crear un objeto que solicite 


'''
class App():
    def __init__(self):
        self.main()
        
    def menu_acciones(self,tipo):
            print(f"\t\t\t....:::: Menú de {tipo} ::::....")
            opcion=input("\n \t1.- Agregar\n\t2.- Eliminar\n\t3.- Actualizar\n\t4.- Mostrar\n\t5.-Regresar\n\t\tEscribe un opcion: ").strip().lower()
            return opcion

    def borrarPantalla(self):
        print("\033c")

    def respuesta_sql(self,respuesta):
        if respuesta:
            input("\n\t\t\t...¡Acción realizada con éxito !...")
        else:
            input("\n\t\t\t...¡No fue posible realizar esta acción, intentalo mas tarde !...") 

    def esperarTecla(self):
            input("\n\t\t\t...¡Oprima cualquier tecla para continuar!...")

    def main(self):
        opcion=True
        self.borrarPantalla()
        while opcion:
            self.borrarPantalla()
            opcion=input("\t\t\t....:::: M E N Ú  P R I N C I P A L ::::....\n\n \t 1.- Coches \n\t 2.- Salir \n\n\t\t Elige una opción: ").strip().lower()
            match opcion:
                case "1": 
                    self.borrarPantalla()
                    print("\t\t\t__Menú coches__")
                    self.menu_coche()
                    self.esperarTecla()
                case "2": 
                    self.borrarPantalla()
                    print("\t\t\t____Saliendo del sistema____")
                    opcion=False
                case _:
                    input("\t\t\t____Opción invalidad____")
                    self.esperarTecla()
    def menu_coche(self):
            opcion= True    
            while opcion:
                self.borrarPantalla()
                opcion=self.menu_acciones("Coches")

                match opcion:
                    case '1':
                        self.borrarPantalla()
                        print("\t\t\t__Menú agregar__")
                        atri_dict=self.datos_coche("Coche")

                        #Crear objetos
                        coche1=cochesBD.CochesBD(atri_dict['marca'],atri_dict['color'],atri_dict['modelo'],atri_dict['velocidad'],atri_dict['potencia'],atri_dict['asientos'])
                        respuesta=coche1.insertar()
                        self.respuesta_sql(respuesta)
                        del coche1

                    case '2':
                        self.borrarPantalla()
                        #atri_dict=self.datos_coche("Coche")
                        id = input("Ingresa el ID del coche a eliminar: ").strip()
                        registros=cochesBD.CochesBD.consultar()

                        respuesta=cochesBD.CochesBD.eliminar(id)
                        self.respuesta_sql(respuesta)
                        

                    case '3':
                        self.borrarPantalla()
                        id = input("Ingresa el ID del coche a actualizar: ").strip()
                        atri_dict=self.datos_coche("Coche")                    
                        coche1=cochesBD.CochesBD(atri_dict['marca'],atri_dict['color'],atri_dict['modelo'],atri_dict['velocidad'],atri_dict['potencia'],atri_dict['asientos'])
                        respuesta=coche1.actualizar(id)
                        self.respuesta_sql(respuesta)
                        del coche1
                    
                    case "4":
                        self.borrarPantalla()
                        registros=cochesBD.CochesBD.consultar()
                        if len(registros) > 0:
                            num_coches=1
                            for fila in registros:
                                print(f"Coche # {num_coches}\n\t ID: {fila[0]} \n\t Marca: {fila[1]}\n\t Color: {fila[2]}\n\t Modelo: {fila[3]}\n\t Velocidad: {fila[4]}\n\t Potencia: {fila[5]}\n\t Asientos: {fila[6]}")
                                num_coches+=1
                                self.esperarTecla()
                        else:
                            input("\n\t\t ....:: Por el momento no existen registros :: ....")


                    case "5":
                        self.borrarPantalla ()
                        opcion=False

                    


                    case _:
                        input("\n\t\t\t...¡Opción invalida, por favor verifique !...")

    def datos_coche(self,tipo):
        self.borrarPantalla()
        print(f"Ingresar datos del  {tipo}")
        #Atri_dict, es la variable que engloba los atributos en un solo diccionario, para cuando se manden llamar esten juntos, pero se pueda llamar solo el atributo necesitado
        atri_dict={}
        atri_dict ['marca']=input("Marca: ").upper().strip()
        atri_dict ['color']=input("Color: ").upper().strip()
        atri_dict ['modelo']=input("Modelo: ").upper().strip()
        atri_dict ['velocidad']=input("Velocidad: ").strip()
        atri_dict ['potencia']=input("Potencia: ").strip()
        atri_dict ['asientos']=input("Asientos: ").strip()
        return atri_dict




if __name__ == "__main__":
    app = App()
