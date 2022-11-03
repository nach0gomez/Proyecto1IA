from asyncio.windows_events import NULL
import tkinter as tk
from tkinter.ttk import Label
from tkinter import messagebox
from collections import deque
from busquedabidireccional import *


class Laberinto():
    def __init__(self): #inicializar clase
        self.mostrar()

    # * determinamos, basados en el tamano de la pantalla,
    # * para centrar la interfaz
    def mostrar (self):
        laberinto=tk.Tk()
        #Titulo
        laberinto.title("Laberinto")
        #definir un tamaño fijo en booleano
        laberinto.resizable(True,True) #(width(ancho),height(alto))
        #cambiar icono de la interfaz
        #raiz.iconbitmap()
        laberintoAncho = 350
        laberintoAlto = 150  
        screen_width = laberinto.winfo_screenwidth()
        screen_height = laberinto.winfo_screenheight()
        x = (screen_width / 2) - (laberintoAncho / 2)
        y = (screen_height / 2) - (laberintoAlto / 2)

        # * predeterminar el tamaño
        laberinto.geometry(f'{laberintoAncho}x{laberintoAlto}+{int(x)}+{int(y)}')

        #laberinto.geometry("350x150")

        #color de fondo
        laberinto.config(bg="sky blue")

        # C:/Python33/README.txt
        #def newlaberinto():
        #    messagebox.showinfo(message= "laberinto cargado", title="newlaberinto")
        lbl = tk.Label (laberinto, bg='white' ,text= "Ingresa la ruta del archivo que contiene el laberinto:")
        lbl.place(x = 30, y = 10)
        #lbl1 = tk.Label(laberinto, bg='orange', text= "Nombre del archivo: ")
        #lbl1.place(x = 30, y = 40)
        self.inpRuta = tk.Entry(laberinto)
        self.inpRuta.place(x = 110, y = 50)

         # * boton para buscar el archivo en la ruta especificada
        btnAceptar = tk.Button (laberinto, text= "Aceptar",command= self.ruta1)
        #command=newlaberinto
        btnAceptar.place(x = 60, y = 90)
        # * boton para cancelar el juego y cerrarlo
        btnCancelar = tk.Button (laberinto, text = "Cancelar", command=laberinto.destroy)
        btnCancelar.place(x = 220, y = 90)
        #siempre debe estar al final
        laberinto.mainloop() #ejecucion en bucle infinito de la interfaz

    def buscarRuta(self):
        ruta=self.inpRuta.get() 
        archivo = open(ruta+".txt")
        fila = archivo.readline()
        self.ls = []
        strAux = ""
        while (fila != ""):
            strAux = str(fila)
            self.ls.append(list(strAux))
            fila = archivo.readline()
        
    
    def ruta1(self): 
        if len(self.inpRuta.get()) == 0:
            messagebox.showinfo('Error', 'Ingrese una ruta valida') 
        else:
            self.buscarRuta() 
            messagebox.showinfo ('Mensaje', 'Ingresado correctamente')

        
# * metodo para leer la matriz desde un archivo de texto
# * nombramos el objeto de tipo archivo como file_object y guardamos el contenido 
# * del texto en la variable leer
# * with es para que cuando no lo utilice mas (el objeto), cierre el intercambio de datos
def validarArchivo(self): 
    ruta=self.inpRuta.get()
    try:
        with open(ruta) as file_object:
            leer = file_object.read()
            print(leer)
        messagebox.showinfo('Información', 'Archivo encontrado')
        
    except:
        messagebox.showerror('Error', 'No se encontró un archivo valido')
    finally:
        self.inpRuta.delete(0,'end')

if __name__ == '__main__':
    lab = Laberinto()