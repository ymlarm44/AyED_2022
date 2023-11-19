# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 14:22:10 2022

@author: alumno
"""

#cola de prioridad implementada con un monticulo de maximos
class ColaPrioridad_maxheap:
    """
    Clase que modela una cola de prioridad que internamente utiliza un monticulo binario de maximos.
    posee metodos de un monticulo binario ademas de un metodo propio 'decrementarClave'


    """
    def __init__(self):
        self.listaMonticulo = [0]
        self.tamanoActual = 0
        
   
    def infiltArriba(self,i):
        """
        metodo que ordena un elemento del monticulo inflitrando hacia arriba.
        es decir comparandose con sus nodos antecesores.

        Parameters
        ----------
        i : clave, en este caso int
            clave del elemento a infiltrar.

        Returns
        -------
        None.

        """
        while i // 2 > 0:
            if self.listaMonticulo[i] > self.listaMonticulo[i // 2]:
                tmp = self.listaMonticulo[i // 2]
                self.listaMonticulo[i // 2] = self.listaMonticulo[i]
                self.listaMonticulo[i] = tmp
            i = i // 2
    
    def insertar(self,k):
        """
        metodo que agrega un nuevo elemento al monticulo

        Parameters
        ----------
        k : clave, en este caso int
            clave con la cual se ingresa el nuevo elemento.

        Returns
        -------
        None.

        """
        self.listaMonticulo.append(k)
        self.tamanoActual = self.tamanoActual + 1
        self.infiltArriba(self.tamanoActual)
        
    def infiltAbajo(self,i):
        """
        metodo que ordena un elemento del monticulo inflitrando hacia abajo.
        es decir comparandose con sus nodos predecesores.

        Parameters
        ----------
        i : clave, en este caso int
            clave del elemento a infiltrar.

        Returns
        -------
        None.

        """
        while (i * 2) <= self.tamanoActual:
            hm = self.hijoMax(i)
            if self.listaMonticulo[i] < self.listaMonticulo[hm]:
                tmp = self.listaMonticulo[i]
                self.listaMonticulo[i] = self.listaMonticulo[hm]
                self.listaMonticulo[hm] = tmp
            i = hm
    
    def hijoMax(self,i):
        """
        metodo que busca el hijo maximo de un elemento

        Parameters
        ----------
        i : clave, en este caso int
            clave del elemento a buscar su hijo maximo.

        Returns
        -------
        int
            clave del hijo maximo.

        """
        if i * 2 + 1 > self.tamanoActual:
            return i * 2
        else:
            if self.listaMonticulo[i*2] > self.listaMonticulo[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1
    
    # extrae el elemento maximo o raiz del monticulo
    def eliminarMax(self):
        """
        metodo que elimina el elemento con maxima clave del monticulo que es a su vez la raiz.
        devuelve dicho elemento

        Returns
        -------
        valorSacado : elemento maximo del monticulo (raiz)

        """
        valorSacado = self.listaMonticulo[1][1]
        self.listaMonticulo[1] = self.listaMonticulo[self.tamanoActual]
        self.tamanoActual = self.tamanoActual - 1
        self.listaMonticulo.pop()
        self.infiltAbajo(1)
        return valorSacado       
            
    def construirMonticulo(self,unaLista):
        """
        metodo que permite construir el monticulo mediante una lista por comprension.

        Parameters
        ----------
        unaLista : []
            lista con los elementos que conformaran el monticulo.

        Returns
        -------
        None.

        """
        i = len(unaLista) // 2
        self.tamanoActual = len(unaLista)
        self.listaMonticulo = [0] + unaLista[:]
        while (i > 0):
            self.infiltAbajo(i)
            i = i - 1
    
    def __iter__(self):
        """
        metodo magico que permite iterar sobre el monticulo.

        Yields
        ------
        i : elemento del monticulo

        """
        for i in self.listaMonticulo:
            yield i
    
    # elimina la tupla con la clave a buscar y la agrega nuevamente con la distancia actualizada
    def decrementarClave(self, vertice, nuevaDistancia):
        """
        metodo propio de la cola de prioridad que recibe una nueva distancia para
        un vertice y la modifica del conjunto en la cola.

        Parameters
        ----------
        vertice : vertice
            vertice al cual se le modificara su dato hermanado distancia.
        nuevaDistancia : int
            valor entero a modificar.

        Returns
        -------
        None.

        """
        for i in range(1,self.tamanoActual):
            if self.listaMonticulo[i][1].id == vertice.id:
                self.listaMonticulo[i] = self.listaMonticulo[self.tamanoActual]
                self.tamanoActual = self.tamanoActual - 1
                self.listaMonticulo.pop()
                self.infiltAbajo(1)
                self.insertar((nuevaDistancia, vertice))
                
    def estaVacia(self):
        """
        comprueba que el monticulo se encuentre vacio

        Returns
        -------
        bool
            devuelve true o false si el monticulo esta vacio.

        """
        return self.tamanoActual == 0


class ColaPrioridad_minheap:
    """
    Clase que modela una cola de prioridad que internamente utiliza un monticulo binario de minimos.
    posee metodos de un monticulo binario ademas de un metodo propio 'decrementarClave'


    """
    def __init__(self):
        self.listaMonticulo = [0]
        self.tamanoActual = 0
        
   
    def infiltArriba(self,i):
        """
        metodo que ordena un elemento del monticulo inflitrando hacia arriba.
        es decir comparandose con sus nodos antecesores.

        Parameters
        ----------
        i : clave, en este caso int
            clave del elemento a infiltrar.

        Returns
        -------
        None.

        """
        while i // 2 > 0:
            if self.listaMonticulo[i] < self.listaMonticulo[i // 2]:
                tmp = self.listaMonticulo[i // 2]
                self.listaMonticulo[i // 2] = self.listaMonticulo[i]
                self.listaMonticulo[i] = tmp
            i = i // 2
    
    def insertar(self,k):
        """
        metodo que agrega un nuevo elemento al monticulo

        Parameters
        ----------
        k : clave, en este caso int
            clave con la cual se ingresa el nuevo elemento.

        Returns
        -------
        None.

        """
        self.listaMonticulo.append(k)
        self.tamanoActual = self.tamanoActual + 1
        self.infiltArriba(self.tamanoActual)
        
    def infiltAbajo(self,i):
        """
        metodo que ordena un elemento del monticulo inflitrando hacia abajo.
        es decir comparandose con sus nodos predecesores.

        Parameters
        ----------
        i : clave, en este caso int
            clave del elemento a infiltrar.

        Returns
        -------
        None.

        """
        while (i * 2) <= self.tamanoActual:
            hm = self.hijoMin(i)
            if self.listaMonticulo[i] > self.listaMonticulo[hm]:
                tmp = self.listaMonticulo[i]
                self.listaMonticulo[i] = self.listaMonticulo[hm]
                self.listaMonticulo[hm] = tmp
            i = hm
    
    def hijoMin(self,i):
        """
        metodo que busca el hijo minimo de un elemento

        Parameters
        ----------
        i : clave, en este caso int
            clave del elemento a buscar su hijo minimo.

        Returns
        -------
        int
            clave del hijo minimo.

        """
        if i * 2 + 1 > self.tamanoActual:
            return i * 2
        else:
            if self.listaMonticulo[i*2] < self.listaMonticulo[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1
    
    # extrae el elemento minimo o raiz del monticulo
    def eliminarMin(self):
        """
        metodo que elimina el elemento con minima clave del monticulo que es a su vez la raiz.
        devuelve dicho elemento

        Returns
        -------
        valorSacado : elemento minimo del monticulo (raiz)

        """
        valorSacado = self.listaMonticulo[1][1]
        self.listaMonticulo[1] = self.listaMonticulo[self.tamanoActual]
        self.tamanoActual = self.tamanoActual - 1
        self.listaMonticulo.pop()
        self.infiltAbajo(1)
        return valorSacado       
            
    def construirMonticulo(self,unaLista):
        """
        metodo que permite construir el monticulo mediante una lista por comprension.

        Parameters
        ----------
        unaLista : []
            lista con los elementos que conformaran el monticulo.

        Returns
        -------
        None.

        """
        i = len(unaLista) // 2
        self.tamanoActual = len(unaLista)
        self.listaMonticulo = [0] + unaLista[:]
        while (i > 0):
            self.infiltAbajo(i)
            i = i - 1
    
    def __iter__(self):
        """
        metodo magico que permite iterar sobre el monticulo.

        Yields
        ------
        i : elemento del monticulo

        """
        for i in self.listaMonticulo:
            yield i
    
    # elimina la tupla con la clave a buscar y la agrega nuevamente con la distancia actualizada
    def decrementarClave(self, vertice, nuevaDistancia):
        """
        metodo propio de la cola de prioridad que recibe una nueva distancia para
        un vertice y la modifica del conjunto en la cola.

        Parameters
        ----------
        vertice : vertice
            vertice al cual se le modificara su dato hermanado distancia.
        nuevaDistancia : int
            valor entero a modificar.

        Returns
        -------
        None.

        """
        for i in range(1,self.tamanoActual):
            if self.listaMonticulo[i][1].id == vertice.id:
                self.listaMonticulo[i] = self.listaMonticulo[self.tamanoActual]
                self.tamanoActual = self.tamanoActual - 1
                self.listaMonticulo.pop()
                self.infiltAbajo(1)
                self.insertar((nuevaDistancia, vertice))
            
    def estaVacia(self):
        """
        comprueba que el monticulo se encuentre vacio

        Returns
        -------
        bool
            devuelve true o false si el monticulo esta vacio.

        """
        return self.tamanoActual == 0


class Vertice:
    """
    Clase que modela un vertice de un grafo.
    posee atributos: 
        id:
            clave del vertice
        conctadoA:
            conexiones a sus vertices vecinos
        dist:
            la distancia del vertice al inicio
        predecesor:
            referencia a su vertice predecesor


    """
    def __init__(self,clave):
        self.id = clave
        self.conectadoA = {}
        self.dist = 0 #se agrega atributo para utilizar dijkstra
        self.predecesor = None
        
    def asignarPredecesor(self, vertice):
        """
        metodo que permite asignar o modificar el atributo predecesor

        Parameters
        ----------
        vertice : objeto vertice
            vertice que se desea asignar como predecesor.

        Returns
        -------
        None.

        """
        self.predecesor = vertice

    def agregarVecino(self,vecino,ponderacion=0):
        """
        metodo que permite agregar un vecino y su ponderacion

        Parameters
        ----------
        vecino : objeto vertice
            vertice que se desea asignar como vecino.
        ponderacion : int
            la distancia del vertice a su vecino. The default is 0.

        Returns
        -------
        None.

        """
        self.conectadoA[vecino] = ponderacion

    def __str__(self):
        """
        metodo magico que permite visualizar el vertice

        Returns
        -------
        str
            str con la clave del vertice y sus conexiones.

        """
        return str(self.id) + ' conectadoA: ' + str([x.id for x in self.conectadoA])

    def obtenerConexiones(self):
        """
        metodo que devuelve las claves de los vertices vecinos.

        """
        return self.conectadoA.keys()

    def obtenerId(self):
        """
        metodo que devuelve la clave del vertice.


        """
        return self.id

    def obtenerPonderacion(self,vecino):
        """
        metodo que devuelve la ponderacion o distancia del vertice a un vecino.

        Parameters
        ----------
        vecino : objeto vertice
            vecino al cual se desea saber la distancia.

        """
        return self.conectadoA[vecino]
    
    #metodo para modificar atributo distancia
    def asignarDistancia(self, valor):
        """
        metodo que modifica el atributo distancia

        Parameters
        ----------
        valor : int
            valor nuevo que se desea modificar.

        Returns
        -------
        None.

        """
        self.dist = valor
    
    #metodo para obtener atributo distancia
    def obtenerDistancia(self):
        """
        metodo que devuelve el valor del atributo distancia.

        Returns
        -------
        int
            valor distancia.

        """
        return self.dist
        
    def __lt__(self, otro):
        return True
    

class Grafo:
    """
    clase que modela un grafo. utiliza un diccionario para almacenar sus vertices
    posee atributos:
        listaVertices:
            listado con los vertices del grafo
        numVertices: 
            la cantidad de vertices en el grafo.  
    
    """
    def __init__(self):
        self.listaVertices = {}
        self.numVertices = 0    
    
    def __getitem__(self,clave):
        """
        metodo magico que permite obtener un vertice mediante su clave

        Parameters
        ----------
        clave : cualquier tipo, en este caso str
            clave con la cual se accedera al vertice.

        Returns
        -------
        objeto vertice
            vertice correspondiente a la clave ingresada.

        """
        return self.obtenerVertice(clave)

    def agregarVertice(self,clave):
        """
        metodo que permite agregar un nuevo vertice al grafo

        Parameters
        ----------
        clave : str
            clave con la que se agregara el nuevo vertice.

        Returns
        -------
        nuevoVertice : objeto vertice
            el vertice que se desea agregar.

        """
        self.numVertices = self.numVertices + 1
        nuevoVertice = Vertice(clave)
        self.listaVertices[clave] = nuevoVertice
        return nuevoVertice

    def obtenerVertice(self,n):
        """
        metodo que devuelve el vertice correspondiente a la clave ingresada.

        Parameters
        ----------
        n : str
            clave correspondiente al vertice solicitado.

        Returns
        -------
        objeto vertice
            vertice que se solicita.

        """
        if n in self.listaVertices:
            return self.listaVertices[n]
        else:
            return None

    def __contains__(self,n):
        """
        metodo magico que permie comprobar si un elemento es parte de un conjunto o no.

        Parameters
        ----------
        n : str
            clave de un vertice.

        Returns
        -------
        bool
            devuelve true o false si este vertice se encuentra en la lista.

        """
        return n in self.listaVertices

    def agregarArista(self,de,a,costo=0):
        """
        metodo que permite agregar una arista entre dos vertices.
        si los vertices a conectar no se encuentran en el grafo los crea.

        Parameters
        ----------
        de : str
            clave del vertice 'origen'.
        a : str
            clave del vertice 'destino'.
        costo : int, optional
            el costo que tendra ligado la arista. The default is 0.

        Returns
        -------
        None.

        """
        if de not in self.listaVertices:
            nv = self.agregarVertice(de)
        if a not in self.listaVertices:
            nv = self.agregarVertice(a)
        self.listaVertices[de].agregarVecino(self.listaVertices[a], costo)

    def obtenerVertices(self):
        """
        metodo que devuelve las claves correspondientes a los vertices almacenados en el grafo.

        """
        return self.listaVertices.keys()

    def __iter__(self):
        """
        metodo magico que permite iterar sobre el grafo vertice a vertice

        Returns
        -------
        objeto vertice
            vertice del grafo.

        """
        return iter(self.listaVertices.values())