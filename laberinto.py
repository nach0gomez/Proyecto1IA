from asyncio.windows_events import NULL
import tkinter as tk
from tkinter.ttk import Label
from tkinter import messagebox
from collections import deque
from busquedabidireccional import *


class Laberinto():
   
   
    def __init__(self) -> None:
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


        lbl = tk.Label (laberinto, bg='white' ,text= "Ingresa la ruta del archivo que contiene el laberinto:")
        lbl.place(x = 30, y = 10)
        
        self.inpRuta = tk.Entry(laberinto)
        self.inpRuta.place(x = 110, y = 50)
        

         # * boton para buscar el archivo en la ruta especificada
        btnAceptar = tk.Button (laberinto, text= "Aceptar",command = self.ruta1)
        
        btnAceptar.place(x = 60, y = 90)
        # * boton para cancelar el juego y cerrarlo
        btnCancelar = tk.Button (laberinto, text = "Cancelar", command = laberinto.destroy)
        btnCancelar.place(x = 220, y = 90)
        laberinto.mainloop() # * ejecucion en bucle infinito de la interfaz
        
    
    
    # * metodo que verifica que el archivo exista con una ruta valida, y que no se haya ingresado una ruta nula
    def ruta1(self): 
        if len(self.inpRuta.get()) == 0:
            
            # TODO remover el self.buscarRuta
            self.buscarRuta()
            messagebox.showinfo('Error', 'Ingrese una ruta valida')
            
        else:
            self.buscarRuta() 
            messagebox.showinfo ('Mensaje', 'Ingresado correctamente')
            

        
        
    # * matriz donde guardamos el juego actual
    juego = []
    
    
    # * metodo para leer la matriz desde un archivo de texto
    # * nombramos el objeto de tipo archivo como file_object y guardamos el contenido 
    # * del texto en la variable leer
    # * with es para que cuando no lo utilice mas (el objeto), cierre el intercambio de datos
    def buscarRuta(self):
        """Metodo que nos lee el archivo y lo guarda como matriz"""
    
        ruta=self.inpRuta.get() 
        
        #TODO camiar para que nos solo busque este archivo, cambiar 'lab2' por ruta para leer el txt
        archivo = open('lab2'+".txt")
        leer = archivo.readline()
        
        
        strAux = ""

        # * aqui es donde guardamos el txt en el arreglo juego[] 2D list
        while (leer != ""):
            print(leer)
            strAux = str(leer)
            leer = archivo.readline()
            self.juego.append(list(strAux))
        
        for i in range(len(self.juego)-1):
            self.juego[i].remove('\n')
            
        
        

    
        
if __name__ == '__main__':
    lab = Laberinto()