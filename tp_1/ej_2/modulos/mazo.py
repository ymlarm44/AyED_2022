# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 15:41:36 2022

@author: alumno

"""
from modulos.LDE import ListaDobleEnlazada

class Mazo:    
    """
    clase que modela un mazo de cartas como una estructura de cola doble
    a su vez utilizando internamente una estructura de lista doblemente 
    enlazada.
    posee metodos para enseñar su ultimo elemento, agregar elementos por ambos
    extremos del mazo, devolver la cantidad de elementos, mostrarse e iterar.

    Returns
    -------
    None.

    """
    
    
    
    def __init__(self):
        self.mazo = ListaDobleEnlazada()
        

    
    def ultimaCarta(self):
        """
        metodo que devuelve el ultimo elemento en el mazo.

        Returns
        -------
        carta : objeto
            clase que modela una carta con sus atributos; numero, palo, jerarquia.
            posee metodos para mostrarse y compararse.

        """
        nodo = self.mazo.extraer(0)
        carta = nodo.dato
            
        return carta
    
    
       
    def agregarArriba(self, Carta):
        """
        metodo que permite agregar un nuevo elemento en el extremo superior
        del mazo.

        Parameters
        ----------
        Carta : objeto
            clase que modela una carta con sus atributos; numero, palo, jerarquia.
            posee metodos para mostrarse y compararse.

        """
        self.mazo.agregar(Carta)
        
        
        
    def agregarAbajo(self, Carta):
        """
        metodo que permite agregar un nuevo elemento en el extremo inferior
        del mazo.

        Parameters
        ----------
        Carta : objeto
            clase que modela una carta con sus atributos; numero, palo, jerarquia.
            posee metodos para mostrarse y compararse..

        """
        self.mazo.anexar(Carta)
    
    
    
    def cantidadCartas(self):
        """
        metodo que devuelve la cantidad de cartas en el mazo.

        Returns
        -------
        self.mazo.tamanio: int.
            valor entero representativo al total de cartas en mazo.

        """
        return self.mazo.tamanio
    
    
    
    def mostrarCartasBocaAbajo(self):
        """
        metodo que devuelve '-X ' segun la cantidad de elementos en mazo.

        Returns
        -------
        aux : str
            cadena de caracteres que simboliza las cartas en el mazo.

        """
        aux = ""
        for i in range(self.cantidadCartas()):
            aux = aux + '-X '
        return aux
    
    
    
    def __str__(self):
        aux=''
        nodo = self.mazo.cabeza
        for i in range(self.cantidadCartas()):    
            carta=nodo.dato
            aux = aux +' '+ str(carta.numero) + str(carta.palo)
            nodo = nodo.siguiente
        return aux
    
    
    
    def __iter__(self):
        for nodo in self.mazo:
            carta = nodo.dato
            yield carta
    
    
    
    
            