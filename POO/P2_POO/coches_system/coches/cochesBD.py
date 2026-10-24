from conexionBD import conexion,cursor

class CochesBD:
    def __init__(self,marca,color, modelo,velocidad,potencia,asientos):
        self._marca=marca
        self._color=color
        self._modelo=modelo
        self._velocidad=velocidad
        self._potencia=potencia
        self._asientos=asientos
    def insertar(self):
        try:
            cursor.execute("insert into coches values (NULL, %s, %s , %s, %s, %s, %s)",(self._marca,self._color,self._modelo,self._velocidad,self._potencia,self._asientos))
            conexion.commit()
            return True
        
        except:
            return False
    @staticmethod
    def consultar():
        try:
            cursor.execute("select * from coches")
            registros = cursor.fetchall()
            
            return registros
        except:
            return []
    @staticmethod
    def eliminar (id):
        try:
            cursor.execute("delete from coches where id=%s",(id,))
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar coche: {e}")
            return False
    def actualizar(self,id):
            try: 
                if conexion.is_connected():
                    cursor.execute("update coches set marca=%s,color=%s, modelo=%s,velocidad=%s,potencia=%s,asientos=%s where id=%s",(self._marca,self._color,self._modelo,self._velocidad,self._potencia,self._asientos,id))
                    conexion.commit()
                    return True
                else:
                    return False
            except Exception as e:
                print(f"Error al actualizar coche: {e}")
                return False
    @property
    def marca(self):
        return self._marca
    @marca.setter
    def marca(self,marca):
        self._marca=marca
    @property
    def color(self):
        return self._color
    @color.setter
    def color(self,color):
        self._color=color
    @property
    def velocidad(self):
        return self._velocidad
    
    @velocidad.setter
    def velocidad(self,velocidad):
        self._velocidad=velocidad
    @property
    def potencia(self):
        return self._potencia
    @potencia.setter
    def potencia(self,potencia):
        self._potencia=potencia
    @property
    def asientos(self):
        return self._asientos
    @asientos.setter
    def asientos(self,asientos):
        self._asientos=asientos

#Se pone en otro paquete
# class CamionesBD(CochesBD):
#     def __init__(self,marca,color, modelo,velocidad,potencia,asientos):
#         super().__init__(marca,color, modelo,velocidad,potencia,asientos)
#         self.__eje= eje
#         self.__capacidadCarga= capacidadCarga

#     def insertar(self):
#         try:
#             cursor.execute("insert into camiones values (NULL, %s, %s , %s, %s, %s, %s)",(self._marca,self._color,self._modelo,self._velocidad,self._potencia,self._asientos,self.__eje,self.__capacidadCarga))
#             conexion.commit()
#             return True
        
#         except:
#             return False

#     def consultar(self):
#         try:
#             cursor.execute("select * from camiones")
#             registros = cursor.fetchall()
            
#             return registros
#         except:
#             return []
#     def eliminar (self,id):
#         try:
#             cursor.execute("delete from camiones where id=%s",(id,))
#             conexion.commit()
#             return True
#         except Exception as e:
#             print(f"Error al eliminar camion: {e}")
#             return False
#     def actualizar(self,id):
#             try: 
#                 if conexion.is_connected():
#                     cursor.execute("update camiones set marca=%s,color=%s, modelo=%s,velocidad=%s,potencia=%s,asientos=%s where id=%s",(self._marca,self._color,self._modelo,self._velocidad,self._potencia,self._asientos,self.__eje,self.__capacidadCarga,id))
#                     conexion.commit()
#                     return True
#                 else:
#                     return False
#             except Exception as e:
#                 print(f"Error al actualizar camion: {e}")
#                 return False