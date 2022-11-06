    
    
    self.ls = []
        strAux = ""
        while (fila != ""):
            print(fila)
            strAux = str(fila)
            self.ls.append(list(strAux))
            fila = archivo.readline()
            
    def buscarInicio(self,lista):
                if (lista[x][y] == 'I'):
                    self.xI= x
                    self.yI= y
                    self.tX=(self.xI, self.yI)
                    print("coordenadas Inicio:", x, y )
                elif (lista[x][y] == 'F'):
                    self.xF= x
                    self.yF= y
                    self.tY=(self.xF, self.yF)
                    print("coordenadas Fin:", x, y )
                else:
                    print("No se encontró el inicio o la meta")
        camino = []
        self.node1 = nodo((self.xI, self.yI), camino, True, False)
        self.node2 = nodo((self.xF, self.yI), camino, False, True)

        self.validarCamino()


    def validarCamino(self):
        self.cola = deque([])
        self.cola.append(self.tX)
        #self.cola.append(self.tY)

        #aux=self.cola.pop()

        self.cola.append(self.node1)
        self.cola.append(self.node2)
        coords=[]
        contador = 10
        #while (len(self.cola) !=0):
        print("a")
        while(contador!=0):
            contador -=1
            print("b")
            aux=self.cola.pop()
            coords.append(aux)
            print(aux[0], aux[1])
            print(len(self.cola))

            if(self.ls[aux[0]][aux[1]] == 'F'):
            #print(self.ls[aux.getCoordenada()[0]-1][aux.getCoordenada()[1]])

            if(self.ls[aux.getCoordenada()[0]][aux.getCoordenada()[1]] == 'F'):
                print("llegó a la meta")
                break

            if (self.ls[aux[0]-1][aux[1]] != '0' and self.validar(coords, aux)):
            # --------------------------

            #print(self.ls[aux.getCoordenada()[0]-1][aux.getCoordenada()[1]])
            if (self.ls[aux.getCoordenada()[0]-1][aux.getCoordenada()[1]] != '0'):
                print("arriba")
                tupla = (aux[0]-1, aux[1])
                coords.append(tupla)
                self.cola.append(tupla)

            elif (self.ls[aux[0]][aux[1]+1] != '0' and self.validar(coords, aux)):
                print("derecha")
                tupla = (aux[0], aux[1]+1)
                coords.append(tupla)
                self.cola.append(tupla)
                if(aux.getIzquierda()):
                    nodoSig = nodo((aux.getCoordenada()[0]-1,aux.getCoordenada()[1]), aux.getCamino(), True, False)
                elif(aux.getDerecha()):
                    nodoSig = nodo((aux.getCoordenada()[0]-1,aux.getCoordenada()[1]), aux.getCamino(), False, True)

            elif (self.ls[aux[0]+1][aux[1]] != '0') and not self.validar(coords, aux):
                if (self.validar (aux.getCamino(), nodoSig)):
                    print("----")
                    for x in range(len (aux.getCamino())):
                        coords.append(aux.getCamino()[x])
                    coords.append(nodoSig.getCoordenada())
                    #coords.append(nodoSig)
                    self.cola.append(nodoSig)

            elif (self.ls[aux.getCoordenada()[0]][aux.getCoordenada()[1]+1] != '0'):
                print("derecha")
                nodoSig = nodo((aux.getCoordenada()[0],aux.getCoordenada()[1]+1), aux.getCamino())
                if (self.validar (aux.getCamino(), nodoSig)):
                    print("----")
                    for x in range(len (aux.getCamino())):
                        coords.append(aux.getCamino()[x])
                    coords.append(nodoSig.getCoordenada())
                    #coords.append(nodoSig)
                    self.cola.append(nodoSig)

            elif (self.ls[aux.getCoordenada()[0]+1][aux.getCoordenada()[1]] != '0'):
                print("abajo")
                tupla = (aux[0]+1, aux[1])
                coords.append(tupla)
                self.cola.append(tupla)

            elif (self.ls[aux[0]][aux[1]-1] != '0' and  self.validar(coords, aux)):
                nodoSig = nodo((aux.getCoordenada()[0]+1,aux.getCoordenada()[1]), aux.getCamino())
                if (self.validar (aux.getCamino(), nodoSig)):
                    print("----")
                    for x in range(len (aux.getCamino())):
                        coords.append(aux.getCamino()[x])
                    coords.append(nodoSig.getCoordenada())
                    #coords.append(nodoSig)
                    self.cola.append(nodoSig)

            elif (self.ls[aux.getCoordenada()[0]][aux.getCoordenada()[1]-1] != '0'):
                print("izquierda")
                tupla = (aux[0], aux[1]-1)
                coords.append(tupla)
                self.cola.append(tupla)

    def validar (self, lsPunto, punto):
        for x in lsPunto:
                nodoSig = nodo((aux.getCoordenada()[0],aux.getCoordenada()[1]-1), aux.getCamino())
                if (self.validar (aux.getCamino(), nodoSig)):
                    print("----")
                    for x in range(len (aux.getCamino())):
                        coords.append(aux.getCamino()[x])
                    coords.append(nodoSig.getCoordenada())
                    #coords.append(nodoSig)
                    self.cola.append(nodoSig)

    def validar (self, caminoRecorrido, punto):
        for x in caminoRecorrido:
            if (x[0] == punto[0] and x[1] == punto[1]):
                return True
        return False
                return False
        return True