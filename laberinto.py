from _tkinter import *
from tkinter import Button, Entry, Tk, messagebox
from tkinter.ttk import Label
class Laberinto():
    def __init__(self, master): #inicializar clase
        super().__init__(master)
        self.pack()

laberinto=Tk ()
#Titulo
laberinto.title("Laberinto")
#definir un tamaño fijo en booleano
laberinto.resizable(True,True) #(width(ancho),height(alto))
#cambiar icono de la interfaz
#raiz.iconbitmap()
#predeterminar el tamaño
laberinto.geometry("350x150")
#color de fondo
laberinto.config(bg="orange")

#def newlaberinto():
#    messagebox.showinfo(message= "laberinto cargado", title="newlaberinto")
lbl = Label (laberinto, text= "Ingresa el nombre del archivo que contiene el laberinto:")
lbl.place(x=30, y= 10)
inp1 = Entry(laberinto)
inp1.place(x=110, y= 45)

btn1 = Button (laberinto, text= "Aceptar")
#command=newlaberinto
btn1.place(x=60, y= 90)
btn2 = Button (laberinto, text = "Cancelar")
btn2.place(x=220, y=90)

#siempre debe estar al final
laberinto.mainloop() #ejecucion en bucle infinito de la interfaz