import tkinter as tk 
import re
from tkinter import messagebox

def limpiar_campos(): 
    tbNombre.delete(0, tk.END)
    tbApellidos.delete(0, tk.END)
    tbEdad.delete(0, tk.END)
    tbEstatura.delete(0, tk.END)
    tbTelefono.delete(0, tk.END)
    var_genero.set(0)
    
def Valid_Int(val):
    try:
        int(val)
        return True
    except ValueError:
        return False

def Valid_Float(val):
    try:
        float(val)
        return True
    except ValueError:
        return False
  
def Validar_Telefono(val):
    return val.isdigit() and len(val) == 10

def Valid_Text(val):
    return bool(re.match("^[a-zA-Z\s]+$", val))

def guardar_valores():
    nombres = tbNombre.get()
    apellidos = tbApellidos.get()
    edad = tbEdad.get()
    estatura = tbEstatura.get()
    telefono = tbTelefono.get()
    genero = ""
    if var_genero.get() == 1:
        genero = "Hombre"
    elif var_genero.get() == 2: 
        genero = "Mujer" 
    
    if (Valid_Int(edad) and Valid_Float(estatura) and Validar_Telefono(telefono) and Valid_Text(nombres) and Valid_Text(apellidos)):
        datos = (f"Nombre: {nombres}\nApellidos: {apellidos}\nEdad: {edad}\nTeléfono: {telefono}\nEstatura: {estatura}\nGénero: {genero}")
        with open("Datos_Python.txt", "a") as file: 
            file.write(datos + "\n\n")
        messagebox.showinfo("Información", "Datos guardados con éxito:\n\n" + datos)
    else:
        messagebox.showerror("Error", "No se pudo guardar la información\n\nFormato incorrecto")
        limpiar_campos()

ventana = tk.Tk()
ventana.geometry("520x500") 
ventana.title("Formulario Vr.02")

var_genero = tk.IntVar()

lbNombre = tk.Label(ventana, text="Nombre:")
lbNombre.pack()
tbNombre = tk.Entry()
tbNombre.pack()

lbApellidos = tk.Label(ventana, text="Apellidos:")
lbApellidos.pack()
tbApellidos = tk.Entry()
tbApellidos.pack()

lbTelefono = tk.Label(ventana, text="Teléfono:")
lbTelefono.pack()
tbTelefono = tk.Entry()
tbTelefono.pack()

lbEdad = tk.Label(ventana, text="Edad:")
lbEdad.pack()
tbEdad = tk.Entry()
tbEdad.pack()

lbEstatura = tk.Label(ventana, text="Estatura:")
lbEstatura.pack()
tbEstatura = tk.Entry()
tbEstatura.pack()

lbGenero = tk.Label(ventana, text="Género")
lbGenero.pack()

rbHombre = tk.Radiobutton(ventana, text="Hombre", variable=var_genero, value=1)
rbHombre.pack()

rbMujer = tk.Radiobutton(ventana, text="Mujer", variable=var_genero, value=2)
rbMujer.pack()

btnBorrar = tk.Button(ventana, text="Borrar Valores", command=limpiar_campos)
btnBorrar.pack()

btnGuardar = tk.Button(ventana, text="Guardar", command=guardar_valores)
btnGuardar.pack()

ventana.mainloop()
