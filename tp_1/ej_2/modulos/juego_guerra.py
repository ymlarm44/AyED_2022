# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 11:36:05 2022

@author: alumno
"""

from modulos.carta import Carta
from modulos.mazo import Mazo
import random as rd

class JuegoGuerra:
    """
    clase que simula el juego guerra de cartas entre dos jugadores con un
    limite de 10.000 turnos.
    recibe como parametro inicial: int. random seed.
    posee los metodos: crearMazo, repartirCartas, iniciar_juego.


    -------
    atributos:
        mazo principal: Mazo(). mazo inicial donde se mezclan las cartas para el juego.
        
        mazo J1: Mazo(). mazo del jugador 1
        
        mazo J2: Mazo(). mazo del jugador 2
    
        turnos jugados: int. cantidad de turnos jugados
        
        ganador: str. el ganador del juego
        
        empate: bool. define si existe empate en el juego (True/False)

    """
    
    valores = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    palos = ['♠', '♥', '♦', '♣']


    
    def __init__(self, random_seed):
        self.mazoPrincipal = Mazo()
        self.mazoJ1 = Mazo()
        self.mazoJ2 = Mazo()
        self.turnos_jugados = 0
        self.ganador = None
        self.empate = True
        self.random_seed = random_seed


    def crearMazo(self):
        """
        crea el mazo principal con cartas y las mezcla.

        Returns
        -------
        None.

        """
        lista_aux = []
        jerarquia = 0
        for valor in self.valores:
            for palo in self.palos:    
                carta = Carta(valor, palo, jerarquia)
                lista_aux.append(carta)
            
            jerarquia += 1
        
        rd.seed(self.random_seed)
        rd.shuffle(lista_aux)
        for carta in (lista_aux):
            self.mazoPrincipal.agregarArriba(carta)
            
            
    def repartirCartas(self):  
        """
        divide el mazo principal en mazoJ1 y mazoJ2 repartiendo cartas
        alternadamente.

        Returns
        -------
        None.

        """
        for i in range(26):
                self.mazoJ1.agregarArriba(self.mazoPrincipal.ultimaCarta())           
                self.mazoJ2.agregarArriba(self.mazoPrincipal.ultimaCarta())



    def iniciar_juego(self):
        """
        llama a los metodos crearMazo() y RepartirCartas() luego inicia 
        el juego con un maximo de 10.000 turnos.

        Returns
        -------
        None.

        """
        self.crearMazo()
        self.repartirCartas()
        
        mesa = []
        while self.turnos_jugados <= 10000:
                        
            try:
                carta_J1 = self.mazoJ1.ultimaCarta()
                carta_J2 = self.mazoJ2.ultimaCarta()
                mesa.append(carta_J1)
                mesa.append(carta_J2)
                print(f'''-----------------------------------------------
turno: {self.turnos_jugados}
jugador 1:
{self.mazoJ1.mostrarCartasBocaAbajo()}
                              
{carta_J1} {carta_J2}
                              
jugador 2:
{self.mazoJ2.mostrarCartasBocaAbajo()}                                                                                                                
                          ''')
                
#---------------------------SI GANA JUGADOR 1----------------------------------                
                if carta_J1 > carta_J2:
                    
                    for i in mesa:
                        self.mazoJ1.agregarAbajo(i)

                
#---------------------------SI GANA JUGADOR 2----------------------------------
                elif carta_J1 < carta_J2:
                
                    for i in mesa:
                        self.mazoJ2.agregarAbajo(i)

                    
#----------------------------SI HAY GUERRA-------------------------------------
                elif carta_J1 == carta_J2:
                    
                    while carta_J1 == carta_J2:
                        copia_carta_J1 = carta_J1
                        copia_carta_J2 = carta_J2
                        m1=self.mazoJ1.mostrarCartasBocaAbajo()
                        m2=self.mazoJ2.mostrarCartasBocaAbajo()
                        
                        for i in range(3):
                            mesa.append(self.mazoJ1.ultimaCarta())
                            mesa.append(self.mazoJ2.ultimaCarta())
                        carta_J1 = self.mazoJ1.ultimaCarta()
                        carta_J2 = self.mazoJ2.ultimaCarta()
                        mesa.append(carta_J1)
                        mesa.append(carta_J2)
                        print(f'''-----------------------------------------------
                    ****GUERRA!!****
turno: {self.turnos_jugados}
jugador 1:
{m1}
                                      
{copia_carta_J1} {copia_carta_J2} -X -X -X -X -X -X {carta_J1} {carta_J2}
                                      
jugador 2:
{m2}                                                                                                                
                                  ''')
                                               
                    if carta_J1 > carta_J2:
                        for i in mesa:
                            self.mazoJ1.agregarAbajo(i)
                    
                    elif carta_J1 < carta_J2:
                        for i in mesa:
                            self.mazoJ2.agregarAbajo(i)
        
            except:


                if self.mazoJ1.cantidadCartas() == 0:
                    self.ganador = 'jugador 2'
                    print('-----------------------------------------------')
                    print("                 ****JUGADOR 2 GANA****")

                    
                if self.mazoJ2.cantidadCartas() == 0:
                    self.ganador = 'jugador 1'
                    print('-----------------------------------------------')
                    print("                 ****JUGADOR 1 GANA****")

                break
                
           
            finally:
                self.turnos_jugados = self.turnos_jugados +1
                mesa.clear()