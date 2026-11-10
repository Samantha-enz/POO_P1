from coches import cochesBD
from tkinter import *
from tkinter import messagebox

class App():
    def __init__(self,ventana):
        self.ventana= ventana
        self.ventana.title("Gestion de Coches")
        self.ventana.geometry("600x600")
        self.ventana.resizable(0,0)
        self.main()
 
 
    def respuesta_sql(self, respuesta):
        if respuesta:
            messagebox.showinfo(title="...Exitoso...", message="Acción realizada con exito" )
        else:
            messagebox.showerror(title="..Verifica por favor..", message="Esta acción no se pudo realizar con exito")
 ## Vistas de Coches
    def borrarPantallaView(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()   

    def main(self):
        self.borrarPantallaView()
        Label(self.ventana,text ="....:::: M E N Ú  P R I N C I P A L ::::...." ).pack(pady=10)
        Button(self.ventana,text=" 1.- Coches",command=self.menu_accionesView ).pack(pady=5)
        Button(self.ventana,text=" 2.- Salir",command=self.ventana.quit ).pack(pady=5)

    def menu_accionesView(self):
        tipo = "tipo"
        self.borrarPantallaView()
        Label(self.ventana,text=f"....:::Menú de Coches:::.....")
        Button(self.ventana,text="1.- Agregar",command=self.insertarView).pack(pady=5)
        Button(self.ventana,text="2.- Borrar",command=self.eliminarView).pack(pady=5)
        Button(self.ventana,text="3.- Modificar",command=self.modificarView).pack(pady=5)
        Button(self.ventana,text="4.- Mostrar",command=self.consultarView).pack(pady=5)
        Button(self.ventana,text="5.- Regresar",command=self.main).pack(pady=5)
        
    def insertarView(self):
        self.borrarPantallaView()
        Label(self.ventana,text="....Ingresar los datos del coche....").pack(pady=10)
        Label(self.ventana,text="Marca: ").pack(pady=10)
        self.marca=Entry(self.ventana)
        self.marca.focus()
        self.marca.pack(pady=5)

        Label(self.ventana,text="Color:: ").pack(pady=10)
        self.color=Entry(self.ventana)
        self.color.pack(pady=5)

        Label(self.ventana,text="Modelo:").pack(pady=10)
        self.modelo=Entry(self.ventana)
        self.modelo.pack(pady=5)

        Label(self.ventana,text="Velocidad:: ").pack(pady=10)
        self.velocidad=Entry(self.ventana)
        self.velocidad.pack(pady=5)

        Label(self.ventana,text="Potencia: ").pack(pady=10)
        self.potencia=Entry(self.ventana)
        self.potencia.pack(pady=5)
        
        Label(self.ventana,text="Asientos: ").pack(pady=10)
        self.asientos=Entry(self.ventana)
        self.asientos.pack(pady=5)

        Button(self.ventana,text="Guardar",command=self.insertarController).pack(pady=10)
        Button(self.ventana,text="Regresar",command=self.menu_accionesView).pack(pady=10)
    
    def eliminarView(self):
        self.borrarPantallaView()
        Label(self.ventana,text="...Ingresar el ID del coche a Eliminar...").pack(pady=10)
        self.id=Entry(self.ventana)
        self.id.focus()
        self.id.pack(pady=5)
        Button(self.ventana,text="Guardar",command=self.eliminarController).pack(pady=10)
        Button(self.ventana,text="Regresar",command=self.menu_accionesView).pack(pady=10)

    def modificarView(self):
        self.borrarPantallaView()
        Label(self.ventana,text="...Ingresar el ID del coche a Modificar...").pack(pady=10)
        self.id=Entry(self.ventana)
        self.id.focus()
        self.id.pack(pady=5)

        Label(self.ventana,text="Nueva Marca: ").pack(pady=10)
        self.marca=Entry(self.ventana)
        self.marca.pack(pady=5)

        Label(self.ventana,text="Nuevo Color:: ").pack(pady=10)
        self.color=Entry(self.ventana)
        self.color.pack(pady=5)

        Label(self.ventana,text="Nuevo Modelo:").pack(pady=10)
        self.modelo=Entry(self.ventana)
        self.modelo.pack(pady=5)

        Label(self.ventana,text="Nueva Velocidad:: ").pack(pady=10)
        self.velocidad=Entry(self.ventana)
        self.velocidad.pack(pady=5)

        Label(self.ventana,text="Nueva Potencia: ").pack(pady=10)
        self.potencia=Entry(self.ventana)
        self.potencia.pack(pady=5)
        
        Label(self.ventana,text="Nuevos Asientos: ").pack(pady=10)
        self.asientos=Entry(self.ventana)
        self.asientos.pack(pady=5)

        Button(self.ventana,text="Guardar",command=self.modificarController).pack(pady=10)
        Button(self.ventana,text="Regresar",command=self.menu_accionesView).pack(pady=10)
    
    def consultarView(self):
        self.borrarPantallaView()
        Label(self.ventana,text="Consultar Coches").pack(pady=10)
        Label(self.ventana,text=f"{'No':<15}{'ID':<15}{'Marca':<30}{'Color':<15}{'Modelo':<15}{'Velocidad':<15}{'Potencia':<15}{'Asientos':<15}\n{'-'*120}").pack(pady=5)
        filas=""
        resultado_filas = self.consultarController(filas)
        Label(self.ventana, text=resultado_filas).pack(pady=5)
        Button(self.ventana,text="Regresar",command=self.menu_accionesView).pack(pady=10)

## Controladores
    def insertarController(self):
        coche1=cochesBD.CochesBD(self.marca.get(),self.color.get(),self.modelo.get(),self.velocidad.get(),self.potencia.get(),self.asientos.get())
        respuesta=coche1.insertar()
        self.respuesta_sql(respuesta)
        del coche1
    def eliminarController(self):
        id = self.id.get()
        respuesta=cochesBD.CochesBD.eliminar(id)
        self.respuesta_sql(respuesta)
    
    def consultarController(self,filas):
            registros=cochesBD.CochesBD.consultar()
            if len(registros) > 0:
                num_coches=1

                for fila in registros:
                    filas=filas+f"{num_coches:<15}{fila[0]:<15}{fila[1]:<30}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}{fila[5]:<15}{fila[6]:<15}\n"
                    num_coches+=1
            else:
               filas="....:: Por el momento no existen registros :: ...."
            return filas
    def modificarController(self):
        id = self.id.get()               
        coche1=cochesBD.CochesBD(self.marca.get(),self.color.get(),self.modelo.get(),self.velocidad.get(),self.potencia.get(),self.asientos.get())
        respuesta=coche1.actualizar(id)
        self.respuesta_sql(respuesta)
        del coche1



if __name__ == "__main__":
    ventana=Tk()
    app = App(ventana)
    ventana.mainloop()
