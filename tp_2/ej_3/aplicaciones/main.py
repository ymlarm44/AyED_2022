# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 17:16:10 2022

@author: yamil
"""

from modulos.algoritmos import dijkstra, dijkstra_modificado
from modulos.estructuras import Grafo
import csv

def main():

    '-----------------------------------------------------------------------------'
    # SELECCION DE DESTINO
    
    destinos = ['Rufino', 'Laboulage', 'VillaMercedes', 'SanLuisCap', 'Rosario', 'MarcosJuarez', 'VillaMaria', 'CiudadCordoba', 'S.delEstero', 'Rosario', 'Rafaela', 'SanMiguelTucuman', 'Salta', 'MinaClavero', 'Frias', 'Simoca', 'BellaVista', 'Mendoza', 'VillaStaRosa', 'LaRioja', 'S.F.ValleCatamarca', 'RosarioFrontera', 'Gral.Guemes', 'RioCuarto', 'SanSalvadorJujuy']
    destinos.sort()
    print(destinos)
    
    
    destino_seleccionado = input('ingrese un destino de la lista: ')
    while destino_seleccionado not in destinos:
        print()
        destino_seleccionado = input('El destino ingresado no se encuentra, porfavor ingresar uno de los destinos validos: ')
    
    '-----------------------------------------------------------------------------'
    # OBTENCION DE MAXIMO CUELLO DE BOTELLA
    
    grafo_a = Grafo()
    
    with open('rutas.txt','r') as rutas:
        datos = csv.reader(rutas)
        for linea in datos:
            grafo_a.agregarArista(linea[0], linea[1], int(linea[2]))
    
    
    dijkstra_modificado(grafo_a, grafo_a['CiudadBs.As.'])
    
    w_max = grafo_a[destino_seleccionado].obtenerDistancia()
    
    
    '-----------------------------------------------------------------------------'
    # OBTENCION DE CAMINO CON MENOR COSTO
    
    grafo_b = Grafo()
    
    with open('rutas.txt','r') as rutas:
        datos = csv.reader(rutas)
        for linea in datos:
            if int(linea[2]) >= w_max:
                grafo_b.agregarArista(linea[0], linea[1], int(linea[3]))
    
    dijkstra(grafo_b, grafo_b['CiudadBs.As.'])
    
    precio_min = grafo_b[destino_seleccionado].obtenerDistancia()
    
    vertice_actual = grafo_b[destino_seleccionado]
    camino = [vertice_actual.id]    
    while vertice_actual.predecesor != None:
        camino.append(vertice_actual.predecesor.id)
        vertice_actual = vertice_actual.predecesor
    
    camino.reverse()
    ruta = ''
    for i in range(len(camino)):
        if i == len(camino)-1:
            ruta += str(camino[i])
            break
        ruta += str(camino[i]) + ' -> '
        
    '-----------------------------------------------------------------------------'
    # INFORME DE RESULTADOS
    
    print(f'''
          destino seleccionado: {destino_seleccionado}
          peso max: {w_max} kg
          precio: ${precio_min}.000
          ruta: {ruta}
          ''')


if __name__ == "__main__":
    
    main()