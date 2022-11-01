class nodo:
    def __init__(self, coordenada, camino, izquierda, derecha):
        self.coordenada = coordenada 
        self.camino = camino
        self.izquierda = izquierda
        self.derecha = derecha

    def getCoordenada(self):
        return self.coordenada
    
    def getCamino(self):
        return self.camino

    def getIzquierda(self):
        return self.izquierda

    def getDerecha(self):
        return self.derecha

    def setIzquierda(self, izq):
        self.izquierda = izq

    def setDerecha(self, der):
        self.derecha = der
