import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext as st
from tkinter import messagebox as mb
from tkinter import StringVar
from bd import BaseDeDatos as bd

class IngresarAlumnos: 
    def __init__(self, parent):
        self.bd = bd()
        self.dni = ttk.Label(parent, text="Dni:")
        self.dni.grid(column=0, row=0, padx=4, pady=4)
        self.nombre = ttk.Label(parent, text="Nombre:")
        self.nombre.grid(column=0, row=1, padx=4, pady=4)
        self.apellido = ttk.Label(parent, text="Apellido:")
        self.apellido.grid(column=0, row=2, padx=4, pady=4)
        self.entryDni = ttk.Entry(parent)
        self.entryDni.grid(column=1, row=0, padx=4, pady=4)
        self.entryNombre = ttk.Entry(parent)
        self.entryNombre.grid(column=1, row=1, padx=4, pady=4)
        self.entryApellido = ttk.Entry(parent)
        self.entryApellido.grid(column=1, row=2, padx=4, pady=4)
        self.button = ttk.Button(parent, text="Ingresar", command=self.bdIngresarAlumnos)
        self.button.grid(column=0, row=3, padx=10, pady=10)

    def bdIngresarAlumnos(self):
        dni = int(self.entryDni.get())
        nombre = self.entryNombre.get()
        apellido = self.entryApellido.get()
        values = (dni, nombre, apellido)
        print("values", values)
        self.bd.ingresarAlumnos(values)
        return
    
class ListarAlumnos: 
    def __init__(self, parent):
        self.titulo = ttk.Label(parent, text="Listado")
        self.titulo.grid(column=0, row=0, padx=4, pady=4)
        self.button = ttk.Button(parent, text="Ingresar", command=self.bdListarAlumnos)
        self.button.grid(column=0, row=2, padx=10, pady=10)
        self.scrollView = st.ScrolledText(parent, width=30, height=15)
        self.scrollView.grid(column=0, row=3, padx=10, pady=10)

    def bdListarAlumnos(self):
        print("listando")
        respuesta=[{"id": 1, "nombre": "Tadeo", "apellido": "Guerstein"}]
        self.scrollView.delete("1.0", tk.END)        
        for fila in respuesta:
            self.scrollView.insert(tk.END, "id: " + str(fila["id"]) + "\nnombre: " + str(fila["nombre"]) + "\napellido: " + str(fila["apellido"]) + "\n\n")
        return
    
class TraerAlumnos: 
    def __init__(self, parent):
        self.bd = bd()
        self.dniLabel = ttk.Label(parent, text="Dni: ")
        self.dniLabel.grid(column=0, row=0, padx=4, pady=4)
        self.dniString = StringVar()
        self.dniEntry = ttk.Entry(parent, textvariable=self.dniString)
        self.dniEntry.grid(column=1, row=0, padx=4, pady=4)
        
        self.nombreLabel = ttk.Label(parent, text="Nombre: ")
        self.nombreLabel.grid(column=0, row=1, padx=4, pady=4)
        self.nombreString = StringVar()
        self.nombreEntry = ttk.Entry(parent, state="readonly", textvariable=self.nombreString)
        self.nombreEntry.grid(column=1, row=1, padx=4, pady=4)
        
        self.apellidoLabel = ttk.Label(parent, text="Apellido: ")
        self.apellidoLabel.grid(column=0, row=2, padx=4, pady=4)
        self.apellidoString = StringVar()
        self.apellidoEntry = ttk.Entry(parent, state="readonly", textvariable=self.apellidoString)
        self.apellidoEntry.grid(column=1, row=2, padx=4, pady=4)
        
        self.button = ttk.Button(parent, text="Ingresar", command=self.bdBuscarAlumno)
        self.button.grid(column=0, row=3, padx=10, pady=10)

    def bdBuscarAlumno(self):
        dni = int(self.dniEntry.get())
        result = self.bd.buscarAlumno(dni)
        print(result)
        print(result[0])
        self.dniString.set(result[0])
        self.nombreString.set(result[1])
        self.apellidoString.set(result[2])
        return
    
class ModificarAlumnos: 
    def __init__(self, parent):
        self.idLabel = ttk.Label(parent, text="Id: ")
        self.idLabel.grid(column=0, row=0, padx=4, pady=4)
        self.idEntry = ttk.Entry(parent)
        self.idEntry.grid(column=1, row=0, padx=4, pady=4)
        
        self.nombreLabel = ttk.Label(parent, text="Nombre: ")
        self.nombreLabel.grid(column=0, row=1, padx=4, pady=4)
        self.nombreEntry = ttk.Entry(parent)
        self.nombreEntry.grid(column=1, row=1, padx=4, pady=4)
        
        self.apellidoLabel = ttk.Label(parent, text="Apellido: ")
        self.apellidoLabel.grid(column=0, row=2, padx=4, pady=4)
        self.apellidoEntry = ttk.Entry(parent)
        self.apellidoEntry.grid(column=1, row=2, padx=4, pady=4)
        
        self.button = ttk.Button(parent, text="Consultar", command=self.bdBuscarAlumno)
        self.button.grid(column=0, row=3, padx=10, pady=10)
        self.button = ttk.Button(parent, text="Modificar", command=self.bdModificarAlumno)
        self.button.grid(column=0, row=4, padx=10, pady=5)

    def bdBuscarAlumno(self):
        print("buscando")
        return
    
    def bdModificarAlumno(self):
        mb.showinfo("Aviso", "Se modificó correctamente")
        return

class BorrarAlumnos: 
    def __init__(self, parent):
        self.idLabel = ttk.Label(parent, text="Id: ")
        self.idLabel.grid(column=0, row=0, padx=4, pady=4)
        self.idEntry = ttk.Entry(parent)
        self.idEntry.grid(column=1, row=0, padx=4, pady=4)
        
        self.button = ttk.Button(parent, text="Ingresar", command=self.bdBorrarAlumno)
        self.button.grid(column=0, row=3, padx=10, pady=10)

    def bdBorrarAlumno(self):
        mb.showinfo("Aviso", "Se eliminó correctamente")
        return


# Preparación app
ventana=tk.Tk()
ventana.title("Aplicación de alumnos")
tabBar = ttk.Notebook(ventana)
tabBar.grid(column=0, row=0, padx=10, pady=10)

# Armado de solapa de ingresar
frameIngresarAlumnos = ttk.Frame(tabBar)
tabBar.add(frameIngresarAlumnos, text="Ingresar alumnos")
ingresarAlumnosFrame = ttk.LabelFrame(frameIngresarAlumnos, text="Alumnos")
ingresarAlumnosFrame.grid(column=0, row=0, padx=5, pady=10)

# Armado de solapa de listado
frameListarAlumnos = ttk.Frame(tabBar)
tabBar.add(frameListarAlumnos, text="Listado de alumnos")
listarAlumnosFrame = ttk.LabelFrame(frameListarAlumnos, text="Listado")
listarAlumnosFrame.grid(column=0, row=0, padx=5, pady=10)

# Armado de solapa de un alumno
frameListarAlumnos = ttk.Frame(tabBar)
tabBar.add(frameListarAlumnos, text="Traer un alumno")
traerAlumnosFrame = ttk.LabelFrame(frameListarAlumnos, text="Alumno")
traerAlumnosFrame.grid(column=0, row=0, padx=5, pady=10)

# Armado de solapa de modificación
frameModificarAlumnos = ttk.Frame(tabBar)
tabBar.add(frameModificarAlumnos, text="Modificación de alumnos")
modificarAlumnosFrame = ttk.LabelFrame(frameModificarAlumnos, text="Modificar")
modificarAlumnosFrame.grid(column=0, row=0, padx=5, pady=10)

# # Armado de solapa de eliminación
frameBorrarAlumnos = ttk.Frame(tabBar)
tabBar.add(frameBorrarAlumnos, text="Borrado de alumnos")
borrarAlumnosFrame = ttk.LabelFrame(frameBorrarAlumnos, text="Borrar")
borrarAlumnosFrame.grid(column=0, row=0, padx=5, pady=10)

# Declaración de las clases de cada solapa
ingresarAlumnos = IngresarAlumnos(ingresarAlumnosFrame)
listarAlumnos = ListarAlumnos(listarAlumnosFrame)
traerAlumnos = TraerAlumnos(traerAlumnosFrame)
modificarAlumnos = ModificarAlumnos(modificarAlumnosFrame)
borrarAlumnos = BorrarAlumnos(borrarAlumnosFrame)

ventana.mainloop()
