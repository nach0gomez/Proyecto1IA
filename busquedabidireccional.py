
class Nodo:
    def __init__(self, valor, vecinos=[]):
        self.valor = valor
        self.vecinos = vecinos
        self.visitados_derecha = False  # * Si el nodo fue encontrado por amplitud empezando desde el raiz
        self.visitados_izquierda = False  # * Si el nodo fue encontrado por amplitud empezando desde el destino
        self.padre_derecha = None  # * usado para recuperar el camino final desde la raiz hasta el punto de encuentro
        self.padre_izquierda = None  # * usado para recuperar el camino final desde el punto de encuentro hasta el destino




from collections import deque

def busquedaBidireccional(s, t):
    def extraerCamino(nodo):
        """Retorna el camino cuando ambas busquedas por profunidad se han encontrado"""
        nodo_copia = nodo
        camino = []

        while nodo:
            camino.append(nodo.valor)
            print(nodo.padre_derecha)
            nodo = nodo.padre_derecha
        
        # * del elimina un objeto y reverse invierte el orden de una lista   
        camino.reverse()
        del camino[-1]  # * dado que el nodo de encuentro aparece dos veces
        #  * index -1 se refiere al ultimo de la lista
            
        while nodo_copia:
            camino.append(nodo_copia.valor)
            print(nodo_copia.padre_izquierda)
            nodo_copia = nodo_copia.padre_izquierda
        return camino
        
    q = deque([])
    q.append(s)
    q.append(t)
    s.visitados_derecha = True
    t.visitados_izquierda = True

    
    while len(q) > 0:
        n = q.pop()
            
        if n.visitados_izquierda and n.visitados_derecha:  # * si el nodo es visitado por ambas busquedas por profundidad
            return extraerCamino(n)
            
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
print(busquedaBidireccional(n0, n4))