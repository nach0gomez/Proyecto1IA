
class Nodo:
    def __init__(self, valor, vecinos=[]):
        self.valor = valor  
        self.vecinos = vecinos
        self.visitados_derecha = False  # * Si el nodo fue encontrado por amplitud empezando desde el raiz
        self.visitados_izquierda = False  # * Si el nodo fue encontrado por amplitud empezando desde el destino
        self.padre_derecha = None  # * usado para recuperar el camino final desde la raiz hasta el punto de encuentro
        self.padre_izquierda = None  # * usado para recuperar el camino final desde el punto de encuentro hasta el destino
    
    def __str__(self):
        return f'el valor del nodo es {self.valor}'
    
    def __repr__(self):
        return f'el valor del nodo es {self.valor}'




from collections import deque

# * incio y final son los nodos que usaremos en la busqueda, el inicio y el final   
def busquedaBidireccional(inicio, final):
    
    
    
    def extraerCamino(nodo):
        """Retorna el camino cuando ambas busquedas por profundidad se han encontrado"""
        
        # * Copiamos el nodo en otra variable para poder modificarla mientras comparamos
        nodo_copia = nodo
        camino = []

        while nodo:
            camino.append(nodo.valor)
            nodo = nodo.padre_derecha
        
        # * del elimina un objeto y reverse invierte el orden de una lista   
        camino.reverse()
        del camino[-1]  # * dado que el nodo de encuentro aparece dos veces
        #  * index -1 se refiere al ultimo de la lista
            
            
        # * copiamos cada uno de los valores de cada nodo al camino
        while nodo_copia:
            camino.append(nodo_copia.valor)
            nodo_copia = nodo_copia.padre_izquierda
        return camino
    
    
    
    # * cola que usaremos para almacenar e iterar los nodos que vamos verificando    
    q = deque([])
    
    # * añadimos el inicio y el final, y les ponemos como visitado = true, ya que ya los verificamos
    q.append(inicio)
    q.append(final)
    inicio.visitados_derecha = True
    final.visitados_izquierda = True

    
    # * mientras que en la cola de la busqueda todavia tengamos elementos, seguimos buscando
    while len(q) > 0:
        n = q.pop()
        print(q)
        if n.visitados_izquierda and n.visitados_derecha:  # * si el nodo es visitado por ambas busquedas por profundidad
            # * retornamos el camino desde ahi hasta la meta 
            return extraerCamino(n)
            
        # * iteramos en todos los vecinos de manera que se buscan si alguno de ellos ha sido visitado previamente
        # * comparamos de manera que si no hay hijo izquierdo, lo ponemos como visitado y lo juntamos a la cola, y agregamos 
        # * los nodos de los vecinos a la cola q donde seguimos verificando
        for nodo in n.vecinos:
            if n.visitados_izquierda == True and not nodo.visitados_izquierda:
                nodo.padre_izquierda = n
                nodo.visitados_izquierda = True
                q.append(nodo)
            if n.visitados_derecha == True and not nodo.visitados_derecha:
                nodo.padre_derecha = n
                nodo.visitados_derecha = True
                q.append(nodo)

    # * En caso de no encontrarlo
    return False




"""
lab2

XXXF   1  2  3   4
0X00   5  6  7   8
XXXX   9  10 11  12
XXXI   13 14 15  16

"""

n0 = Nodo(0)
n1 = Nodo(1)
n2 = Nodo(2)
n3 = Nodo(3)
n4 = Nodo(4)
n5 = Nodo(5)
n6 = Nodo(6)
n7 = Nodo(7)
n8 = Nodo(8)
n9 = Nodo(9)
n10 = Nodo(10)
n11 = Nodo(11)
n12 = Nodo(12)
n13 = Nodo(13)
n14 = Nodo(14)
n15 = Nodo(15)
n16 = Nodo(16)



n16.vecinos = [n15,n12]
n15.vecinos = [n16, n14, n11]
n14.vecinos = [n15, n13, n10]
n13.vecinos = [n14, n9]
n9.vecinos = [n13]
n10.vecinos = [n14, n6]
n6.vecinos = [n10, n2]
n2.vecinos = [n6, n1, n3]
n1.vecinos = [n2]
n3.vecinos = [n2, n4]





'''
n0 = Nodo(0)
n1 = Nodo(1)
n2 = Nodo(2)
n3 = Nodo(3)
n4 = Nodo(4)
n5 = Nodo(5)
n6 = Nodo(6)
n7 = Nodo(7)
n0.vecinos = [n1, n5] 
n1.vecinos = [n0, n2, n6]
n2.vecinos = [n1]
n3.vecinos = [n4, n6]
n4.vecinos = [n3]
n5.vecinos = [n0, n6]
n6.vecinos = [n1, n3, n5, n7]
n7.vecinos = [n6]

'''

#print(busquedaBidireccional(n16, n4))