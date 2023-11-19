# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 20:12:56 2022

@author: rodro
"""

class Nodo:
    """
    clase que modela un nodo que almacena un dato.
    posee referencias a su anterior y posterior ademas de metodos
    para modificar o devolver tanto su dato como las referencias.
    
    ----------
    atributos:
        dato: cualquier tipo. dato que contiene el nodo.
        
        siguiente: referencia a su nodo posterior.
        
        anterior: referencia a su nodo anterior.

    """
    
    
    
    def __init__(self,datoInicial):
        self.dato = datoInicial
        self.siguiente = None
        self.anterior = None
        
    def __str__(self):
        return str(self.dato)
    
    def __repr__(self):
        return str(self)
    
    @property
    def dato(self):
        return self._dato
    
    @dato.setter
    def dato(self, valor):
        self._dato = valor

    @property    
    def siguiente(self):
        return self._siguiente
    
    @siguiente.setter
    def siguiente(self, valor):
        self._siguiente = valor
    
    @property
    def anterior(self):
        return self._anterior
    
    @anterior.setter
    def anterior(self, valor):
        self._anterior = valor
        
"""+-++-+-+-+-+-+-++-+--+-+-+-++-"""        

class ListaDobleEnlazada:
    """
    clase que modela una lista de nodos doblemente enlazada.
    posee metodos que permiten copiar la lista, agregar y eliminar
    elementos en cualquier posicion de la lista, invertir la lista, iterar
    sobre la lista, ordenarla de menor a mayor, concatenar listas.

    ----------
    atributos:
        cabeza: el nodo que encabeza la lista (el primero).
        
        cola: el ultimo nodo de la lista.
        
        tamanio: cantidad de elementos en la lista.

    """
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self._tamanio = 0
    
    @property
    def cabeza(self):
        return self._cabeza
    
    @cabeza.setter
    def cabeza(self, valor):
        self._cabeza = valor
    
    @property
    def cola(self):
        return self._cola
    
    @cola.setter
    def cola(self, valor):
        self._cola = valor
    
    @property
    def tamanio(self):     
         return  self._tamanio

        

    def estaVacia(self): 
        """
        chequea que no existan elementos en la lista.

        Returns
        -------
        True/False

        """
        return self.cabeza == None   
 
    

    def agregar(self, item):
        """
        metodo que agrega un nuevo nodo a la lista por el extremo
        izquiero y desplaza el resto de nodos hacia la derecha.

        Parameters
        ----------
        item : TYPE
            dato que posee el nuevo nodo a agregar.


        """
        temp = Nodo(item)
        if self.cabeza == None:  
            self.cabeza = temp
            self.cola = temp
            self.cabeza.siguiente = None
        else:  
            temp.siguiente = self.cabeza
            self.cabeza.anterior = temp  
            self.cabeza = temp
        self._tamanio += 1 
        
        
                
    def anexar(self, item): 
        """
        metodo que anexa un nuevo nodo al final de la lista.

        Parameters
        ----------
        item : TYPE
            dato que posee el nuevo nodo a agregar.

        """
        temp = Nodo(item)
        if self.cabeza == None:  
            self.cabeza = temp
           
        else:
            apuntador = self.cabeza  
            while apuntador.siguiente != None:  
                apuntador = apuntador.siguiente
            apuntador.siguiente = temp
            temp.anterior = apuntador
            self.cola = temp
        self._tamanio += 1 



    def insertar(self, posicion, item):
        """
        metodo que agrega un nuevo nodo a la lista en una 
        posicion indicada.

        Parameters
        ----------
        posicion : int.
            posicion de la lista donde se desea agregar el nodo.
            
        item : TYPE
            dato que posee el nuevo nodo a agregar.

        Raises
        ------
        IndexError
            la posicion ingresada no es valida.

        """
        nuevoNodo = Nodo(item)
        if  0 > posicion or posicion > self._tamanio:
            raise IndexError
        
        if posicion == 0:
            self.agregar(item)
        
        
        else:
            temp = self.cabeza
            for nodo in range(posicion-1):  
                temp = temp.siguiente 
            nuevoNodo.anterior = temp     
            nuevoNodo.siguiente = temp.siguiente
            if temp.siguiente != None:
                temp.siguiente.anterior = nuevoNodo
            temp.siguiente = nuevoNodo
            self._tamanio += 1



    def extraer(self, posicion=-1):
        """
        metodo que elimina un nodo en una posicion indicada.

        Parameters
        ----------
        posicion : int., optional
            posicion de la lista donde se desea eliminar 
            el nodo.. The default is -1.

        Raises
        ------
        IndexError
            la posicion ingresada no es valida.

        Returns
        -------
        num : objeto
            objeto que se elimina de la lista.

        """
        
        num = None
            
        if  -1 > posicion or posicion >= self._tamanio:
            raise IndexError
        
        if self.tamanio == 1:
            num = self.cabeza
            self.cabeza = None
            self.cola = None
        
        elif posicion == self._tamanio-1 or posicion == -1:
            num = self.cola
            aux = self.cola.anterior
            self.cola.anterior = None
            self.cola = aux
        
        elif posicion == 0:
            num = self.cabeza
            aux = self.cabeza.siguiente
            self.cabeza.siguiente = None
            self.cabeza =  aux
            
            
        else:
            temp = self.cabeza
            for nodo in range(posicion):  
                temp = temp.siguiente
            num = temp
            temp.anterior.siguiente = temp.siguiente
            if temp.siguiente != None:
                temp.siguiente.anterior = temp.anterior
               
        self._tamanio -=1
        return num
    
    
    
    def copiar(self):
        """
        metodo que crea una copia de la lista. 

        Returns
        -------
        copia : ListaDobleEnlazada
            copia de la lista.

        """
        copia = ListaDobleEnlazada()
        temp = self.cabeza
        for nodo in range(self.tamanio):
            copia.anexar(temp.dato)
            temp = temp.siguiente
        return copia
        
    
    
    def invertir(self):
        """
        metodo que invierte el orden de la lista.

        Returns
        -------
        None.

        """
        p = self.cabeza
        self.cola = self.cabeza
        q = p.siguiente
        p.siguiente = None
        p.anterior = q
             
        while q is not None:
            q.anterior = q.siguiente
            q.siguiente = p
            p = q
            q = p.anterior
            self.cabeza = p
             
             
            
    
    
    def concatenar(self, ListaDobleEnlazada):
        """
        metodo que concatena dos listas manteniendo su orden.

        Parameters
        ----------
        ListaDobleEnlazada : ListaDobleEnlazada
            lista que se desea concatenar.

        """
        if self.cabeza == None:
            return ListaDobleEnlazada
        elif ListaDobleEnlazada.cabeza == None:
            return self
        else:
            self.cola.siguiente = ListaDobleEnlazada.cabeza
            ListaDobleEnlazada.cabeza.anterior = self.cola
            self.cola = ListaDobleEnlazada.cola
            self._tamanio = self._tamanio + ListaDobleEnlazada._tamanio
            return self



    def ordenar(self):
        """
        metodo que ordena los elementos de la lista de menor a mayor.

        Returns
        -------
        None.

        """       
        fin = None
        while self.cabeza != fin:
            actual = self.cabeza
            aux = self.cabeza
            
            while aux.siguiente != fin:
                cambia = aux.siguiente
                if aux.dato > cambia.dato:
                    aux.siguiente = cambia.siguiente
                    cambia.siguiente = aux
                    if aux != self.cabeza:
                        actual.siguiente = cambia
                    else:
                        self.cabeza = cambia
                    aux = aux
                    aux = cambia
                    cambia = aux
                actual = aux
                aux = aux.siguiente
            fin=aux
                
                               
    def buscar(self,item):
        """
        metodo que busca un elemento determinado en la lista.

        Parameters
        ----------
        item : TYPE
            dato que se desea buscar en la lista.

        Returns
        -------
        encontrado : bool.
            devuelve True/False dependiendo del resultado de la busqueda.

        """
        actual = self.cabeza
        encontrado = False
        while actual != None and not encontrado:
            if actual.obtenerDato() == item:
                encontrado = True
            else:
                actual = actual.obtenerSiguiente()

        return encontrado


        
    def __str__ (self):
        """
        metodo que devuelve por consola los 
        elementos de la lista como una lista de python.

        -------
         
        """
        
        return str([nodo for nodo in self])
                
                
    def __iter__(self):
         nodo = self.cabeza
         while nodo :
             yield nodo
             nodo = nodo.siguiente
             
