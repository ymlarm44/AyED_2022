# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 14:46:15 2022

@author: alumno
"""

class Carta:
    """
    clase que modela una carta mediante sus atributos: numero, palo, jerarquia.
    posee metodos para mostrarse y compararse.

    -------
    atributos:        
        numero: str. valor simbolico representativo de la carta.
        
        palo: str. categoriza a la carta con uno de los cuatro grupos existentes.
        
        jerarquia: int. valor numerico que posiciona a la carta en un orden
        jerarquico y le permite compararse.
        

    """
    def __init__(self,num,pal,jer):
        self._numero = num
        self._palo = pal
        self._jerarquia = jer
        
    @property   
    def numero(self):
        return self._numero
   
    @property
    def palo(self):
        return self._palo
    
    @property
    def jerarquia(self):
        return self._jerarquia

    
    def __lt__(self, otro):
        return self.jerarquia < otro.jerarquia
    
    def __gt__(self, otro):
        return self.jerarquia > otro.jerarquia
    
    def __eq__(self, otro):
        return self.jerarquia == otro.jerarquia
    
    def __str__(self):
        cad = str(self.numero) + str(self.palo)
        return cad


