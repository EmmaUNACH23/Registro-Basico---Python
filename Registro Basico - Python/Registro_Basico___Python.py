from multiprocessing import Value
import tkinter as tk 
from tkinter import messagebox

def limpiar_campos(): 
    tbNombre.delete(0,tk.END)
    tbApellidos.delete(0,tk.END)
    tbEdad.delete(0,tk.END)
    tbEstatura.delete(0,tk.END)
    tbTelefono.delete(0,tk.END)
    var_genero.set(0)
    

def guardar_valores():
    nombres= tbNombre.get()
    apellidos = tbApellidos.get()
    edad = tbEdad.get()
    estatura = tbEstatura.get()
    telefono = tbTelefono.get()
    genero = ""
    if var_genero.get()==1:
        genero = "Hombre"
    elif var_genero.get ()==2: 
        genero = "Mujer" 
    datos= "Nombre : " +nombres + "\nApellidos :" + apellidos + "\nEdad:" + edad + "\nTelefono:" + telefono + "\nEstatura:"  + estatura
    
    with open ("Datos_Python.txt","a") as file : 
       file.write(datos + "\n\n")
       messagebox.showinfo ("informacion" + "guardada\n\n", datos)
    
        


ventana =  tk.Tk()
ventana.geometry ("520x500") 
ventana.title("Formulario Vr.01")

var_genero = tk.IntVar()



lbNombre = tk.Label(ventana, text = "Nombre :")
lbNombre.pack()
tbNombre = tk.Entry()
tbNombre.pack()

lbApellidos = tk.Label(ventana, text = "Apellidos :")
lbApellidos.pack()
tbApellidos = tk.Entry()
tbApellidos.pack()

lbTelefono = tk.Label(ventana, text = "Telefono :")
lbTelefono.pack()
tbTelefono = tk.Entry()
tbTelefono.pack()

lbEdad = tk.Label(ventana, text = "Edad :")
lbEdad.pack()
tbEdad = tk.Entry()
tbEdad.pack()

lbEstatura = tk.Label(ventana, text = "Estatura :")
lbEstatura.pack()
tbEstatura = tk.Entry()
tbEstatura.pack()

lbGenero = tk.Label(ventana, text = "Genero")
lbGenero.pack()

rbHombre = tk.Radiobutton(ventana, text = "Hombre",variable=var_genero,value=1)
rbHombre.pack()

rbMujer = tk.Radiobutton(ventana, text = "Mujer",variable=var_genero,value=2)
rbMujer.pack()

btnBorrar = tk.Button (ventana,text ="Borrar Valores",command=limpiar_campos)
btnBorrar.pack()
btnGuardar = tk.Button (ventana,text ="Guardar",command=guardar_valores)
btnGuardar.pack()

ventana.mainloop()
