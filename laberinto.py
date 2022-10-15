
# * cambio a la manera de importacion, ya que me generaba incosistencias al
# * momento de llamar los metodos de tkinter
import tkinter as tk
from tkinter.ttk import Label


class Laberinto():
    def __init__(self, master): #inicializar clase
        super().__init__(master)
        self.pack()

laberinto=tk.Tk()
#Titulo
laberinto.title("Laberinto")
#definir un tamaño fijo en booleano
laberinto.resizable(True,True) #(width(ancho),height(alto))
#cambiar icono de la interfaz
#raiz.iconbitmap()


appAncho = 350
appAlto = 150

# * determinamos, basados en el tamano de la pantalla,
# * para centrar la interfaz

screen_width = laberinto.winfo_screenwidth()
screen_height = laberinto.winfo_screenheight()
x = (screen_width / 2) - (appAncho / 2)
y = (screen_height / 2) - (appAlto / 2)

# * predeterminar el tamaño
laberinto.geometry(f'{appAncho}x{appAlto}+{int(x)}+{int(y)}')

#laberinto.geometry("350x150")

#color de fondo
laberinto.config(bg="orange")

# C:/Python33/README.txt
#def newlaberinto():
#    messagebox.showinfo(message= "laberinto cargado", title="newlaberinto")
lbl = tk.Label (laberinto, bg='orange' ,text= "Ingresa la ruta del archivo que contiene el laberinto:")
lbl.place(x = 30, y = 10)
lbl1 = tk.Label(laberinto, bg='orange', text= "Ej:C:/Python33/matriz.txt")
lbl1.place(x = 30, y = 40)
inpRuta = tk.Entry(laberinto)
inpRuta.place(x = 170, y = 40)


# * metodo para leer la matriz desde un archivo de texto
# * nombramos el objeto de tipo archivo como file_object y guardamos el contenido 
# * del texto en la variable leer
# * with es para que cuando no lo utilice mas (el objeto), cierre el intercambio de datos

def buscarRuta():
    ruta=inpRuta.get()
    with open(ruta) as file_object:
     leer = file_object.readlines()
    print(leer)
    
# * boton para buscar el archivo en la ruta especificada
btnAceptar = tk.Button (laberinto, text= "Aceptar", command=buscarRuta)
#command=newlaberinto
btnAceptar.place(x = 60, y = 90)

# * boton para cancelar el juego y cerrarlo
btnCancelar = tk.Button (laberinto, text = "Cancelar", command=laberinto.destroy)
btnCancelar.place(x = 220, y = 90)





#siempre debe estar al final
laberinto.mainloop() #ejecucion en bucle infinito de la interfaz

