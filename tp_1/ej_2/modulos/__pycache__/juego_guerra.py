# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 11:36:05 2022

@author: alumno
"""

import random as rd
from module.cola_doble_2 import ColaDoble
from module.carta import Carta

class JuegoGuerra:
    valores = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    palos = ['♠', '♥', '♦', '♣']
    
    def __init__(self):
        self.mazoPrincipal = ColaDoble()
        self.mazoJ1 = ColaDoble()
        self.mazoJ2 = ColaDoble()

    def crearMazo(self):
        lista_cartas=[]
        for palo in self.palos:
            for valor in self.valores:
                carta = Carta(valor, palo)
                lista_cartas.append(carta)
        
        rd.shuffle(lista_cartas)
        for carta in lista_cartas:
            self.mazoPrincipal.agregarFrente(carta)
        return self.mazoPrincipal
    
    
    # def mezclar(self):
    #     rd.shuffle(self.mazoPrincipal)
    #     return self.mazoPrincipal
    
    def repartirCartas(self):  
        for i in range(0,53,2):
            self.mazoJ1.agregarFrente(self.mazoPrincipal[i])
        
        for i in range(1,53,2):
            self.mazoJ2.agregarFrente(self.mazoPrincipal[i])
        

juego1 = JuegoGuerra()

juego1.crearMazo()



            