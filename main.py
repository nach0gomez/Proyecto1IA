from tkinter import Tk
from arbol import Arbol
#import networkx as nx
#import matplotlib.pyplot as plt 
from laberinto import Laberinto

def busquedaAmplitud(arbol):  
    cola = []
    cola.append(arbol) # * adiciona la raiz a la cola
    recorrido = [] # * lista de recorridos

    while len(cola) > 0:   # * comienza a buscar el recorrido solamente si la cola no esta vacia
        nodo = cola.pop(0);  # * trae el primer valor y lo asigna a nodo
        recorrido.append(nodo.key)  # * le asigna el valor de nodo a la lista de recorridos

         # * agregamos ambos hijos a la cola en caso de que no esten vacios
        if nodo.left != None:
            cola.append(nodo.left)

        if nodo.right != None:
            cola.append(nodo.right)

        if nodo.left1 != None:
            cola.append(nodo.left1)
        
        if nodo.right1 != None:
            cola.append(nodo.right1)

        if nodo.center != None:
            cola.append(nodo.center)
    return recorrido


# * Este es el arbol que estamos representando
"""
                    5
             6             7
         8       9      10   11
      15   13
"""


"""objArbol = Arbol(5, 
                    Arbol(6,
                        Arbol(8,
                        Arbol(15, None, None),
                        Arbol(13, None, None)
                            ),
                        Arbol(9, None, None)
                    ), 
                    Arbol(
                        7, 
                        Arbol(10, None, None),
                        Arbol(11, None, None)
                    )            
                ) """         



#print(busquedaAmplitud(objArbol))

# TODO arbol inicio fin 

objArbol = Arbol (0.0,
                    Arbol(4.0,
                    Arbol(4.3,
                    Arbol(0.3, None, None, None, None, None),
                    Arbol(4.0, None, None, None, None, None), None, None, None),
                    Arbol(0.0, None, None, None, None, None),
                    Arbol(1.3,
                    Arbol(4.3, None, None, None, None, None),
                    Arbol(0.3, None, None, None, None, None),
                    Arbol(1.0, None, None, None, None, None),
                    Arbol(4.0, None, None, None, None, None),
                    None), None, None),
                    Arbol(0.3,
                    Arbol(4.3, None, None, None, None, None),
                    Arbol(0.0, None, None, None, None, None),
                    Arbol(3.0,
                    Arbol(4.0, None, None, None, None, None),
                    Arbol(3.3, None, None, None, None, None),
                    Arbol(0.0, None, None, None, None, None),
                    Arbol(0.3, None, None, None, None, None), None),                    
                    None, None),
             None, None, None)
             
print(busquedaAmplitud(objArbol))

"""
# * Grafica de un grafo completo
G = nx.cycle_graph(10) # * funcion que genera grafo circular de 10 vertices, que no me pete el pc :D
nx.draw_circular(G, with_labels=True, node_size=600, alpha=1.0,
                      node_color='Gainsboro', font_size=14,
                     font_weight='bold') # * Dibujar el grafo G con los atributos especificados
plt.axis("equal") # * redimensionar los ejes a longitudes iguales
plt.show () # * Mostrar el grafo G por pantalla
"""

