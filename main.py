from arbol import Arbol


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
    return recorrido


# * Este es el arbol que estamos representando
"""
                    5
             6             7
         8       9      10   11
      15   13
"""


objArbol = Arbol(5, 
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
                )          



print(busquedaAmplitud(objArbol))