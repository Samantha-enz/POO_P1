from estudiantes import estudiante
from tkinter import *
from tkinter import messagebox
class App:
    def __init__(self,ventana):
        self.ventana= ventana
        self.ventana.title("Gestion de Estudiantes")
        self.ventana.geometry("600x600")
        self.ventana.resizable(0,0)
        self.main()
 
 
    def respuesta_sql(self, respuesta):
        if respuesta:
            messagebox.showinfo(title="...Exitoso...", message="Acción realizada con exito" )
        else:
            messagebox.showerror(title="..Verifica por favor..", message="Esta acción no se pudo realizar con exito")
 ## Vistas de estudiantes
    def borrarPantallaView(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()   

    def main(self):
        self.borrarPantallaView()
        Label(self.ventana,text ="....:::: M E N Ú  P R I N C I P A L ::::...." ).pack(pady=10)
        Button(self.ventana,text=" 1.- Estudiates",command=self.menu_accionesView ).pack(pady=5)
        Button(self.ventana,text=" 2.- Salir",command=self.ventana.quit ).pack(pady=5)

    def menu_accionesView(self):
        tipo = "tipo"
        self.borrarPantallaView()
        Label(self.ventana,text=f"....:::Menú de Estudiantes:::.....")
        Button(self.ventana,text="1.- Agregar",command=self.insertarView).pack(pady=5)
        Button(self.ventana,text="2.- Borrar",command=self.eliminarView).pack(pady=5)
        Button(self.ventana,text="3.- Modificar",command=self.modificarView).pack(pady=5)
        Button(self.ventana,text="4.- Mostrar",command=self.consultarView).pack(pady=5)
        Button(self.ventana,text="5.- Regresar",command=self.main).pack(pady=5)
    
    def insertarView(self):
        self.borrarPantallaView()
        Label(self.ventana,text="....Ingresar los datos del estudiante....").pack(pady=10)
        Label(self.ventana,text="Nombre: ").pack(pady=10)
        self.nombre=Entry(self.ventana)
        self.nombre.focus()
        self.nombre.pack(pady=5)

        Label(self.ventana,text="Calificación: ").pack(pady=10)
        self.nota=Entry(self.ventana)
        self.nota.pack(pady=5)

        Button(self.ventana,text="Guardar",command=self.insertarController).pack(pady=10)
        Button(self.ventana,text="Regresar",command=self.menu_accionesView).pack(pady=10)
    
    def eliminarView(self):
        self.borrarPantallaView()
        Label(self.ventana,text="...Ingresar el ID del alumno a Eliminar...").pack(pady=10)
        self.id=Entry(self.ventana)
        self.id.focus()
        self.id.pack(pady=5)
        Button(self.ventana,text="Guardar",command=self.eliminarController).pack(pady=10)
        Button(self.ventana,text="Regresar",command=self.menu_accionesView).pack(pady=10)

    def modificarView(self):
        self.borrarPantallaView()
        Label(self.ventana,text="...Ingresar el ID del Alumno a Modificar...").pack(pady=10)
        self.id=Entry(self.ventana)
        self.id.focus()
        self.id.pack(pady=5)

        Label(self.ventana,text="Nueva Nombre: ").pack(pady=10)
        self.nombre=Entry(self.ventana)
        self.nombre.pack(pady=5)

        Label(self.ventana,text="Nueva Calificación:: ").pack(pady=10)
        self.nota=Entry(self.ventana)
        self.nota.pack(pady=5)

        Button(self.ventana,text="Guardar",command=self.modificarController).pack(pady=10)
        Button(self.ventana,text="Regresar",command=self.menu_accionesView).pack(pady=10)
    
    def consultarView(self):
        self.borrarPantallaView()
        Label(self.ventana,text="Consultar Estudiantes").pack(pady=10)
        Label(self.ventana,text=f"{'No':<15}{'ID':<15}{'Nombre':<30}{'Calificación':<15}\n{'-'*75}").pack(pady=5)
        filas=""
        filas=self.consultarController(filas)
        Label(self.ventana,text=self.consultarController(filas)).pack(pady=5)
        Button(self.ventana,text="Regresar",command=self.menu_accionesView).pack(pady=10)

## Controladores
    def insertarController(self):
        estudiante1=estudiante.Estudiantes(self.nombre.get(),self.nota.get())
        respuesta=estudiante1.insertar()
        self.respuesta_sql(respuesta)
        del estudiante1
    def eliminarController(self):
        id = self.id.get()
        respuesta=estudiante.Estudiantes.eliminar(id)
        self.respuesta_sql(respuesta)
    
    def consultarController(self,filas):
            registros=estudiante.Estudiantes.consultar()
            if len(registros) > 0:
                num_estudiantes=1

                for fila in registros:
                    # filas=filas+(f"{num_estudiantes:<10}\t ID: {fila[0]} \n\t Nombre: {fila[1]}\t Calificación: {fila[2]}")
                    filas=filas+f"{num_estudiantes:<15}{fila[0]:<15}{fila[1]:<30}{fila[2]:<15}\n"
                    num_estudiantes+=1
            else:
               filas="....:: Por el momento no existen registros :: ...."
            return filas
    def modificarController(self):
        id = self.id.get()               
        estudiante1=estudiante.Estudiantes(self.nombre.get(),self.nota.get())
        respuesta=estudiante1.actualizar(id)
        self.respuesta_sql(respuesta)
        del estudiante1


               
    
    
if __name__=="__main__":
    ventana=Tk()
    app = App(ventana)
    ventana.mainloop()
