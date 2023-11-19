# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 14:32:51 2022

@author: alumno
"""

from modulos.estructuras import ColaPrioridad_maxheap, ColaPrioridad_minheap
 
#se modifica dijkstra para que su cola de prioridad funcione internamente con
#un monticulo de maximos

def dijkstra_modificado(unGrafo,inicio):
    """
    Algoritmo que procesa un grafo para obtener el maximo cuello de botella

    Parameters
    ----------
    unGrafo : Grafo
        Grafo al cual se le aplicara el algoritmo dijkstra.
    inicio : Vertice
        Vertice inicial del grafo donde comienza dijkstra.


    """
    cp = ColaPrioridad_maxheap()
    inicio.asignarDistancia(999999999) #se asigna distancia 'infinito' al vertice inicio del grafo
    cp.construirMonticulo([(v.obtenerDistancia(),v) for v in unGrafo])

    while not cp.estaVacia():
        verticeActual = cp.eliminarMax()
        
        
        for verticeSiguiente in verticeActual.obtenerConexiones():
            distancia_actual_a_siguiente = verticeActual.obtenerPonderacion(verticeSiguiente) #obtiene la distancia o peso del vertice actual al siguiente
            peso_vertice_actual = verticeActual.obtenerDistancia() #obtiene distancia o peso del vertice actual
            if distancia_actual_a_siguiente < peso_vertice_actual: #evalua para quedarse con el minimo cuello de botella
                nuevaDistancia = distancia_actual_a_siguiente
            else:
                nuevaDistancia = peso_vertice_actual
            
                        
            if nuevaDistancia > verticeSiguiente.obtenerDistancia():  #evalua para modificar distancia o peso y llegar al maximo cuello de botella
                verticeSiguiente.asignarDistancia(nuevaDistancia)
                verticeSiguiente.asignarPredecesor(verticeActual)
                cp.decrementarClave(verticeSiguiente,nuevaDistancia)


                
def dijkstra(unGrafo,inicio):
    """
    Algoritmo que procesa un grafo para obtener el costo minimo.

    Parameters
    ----------
    unGrafo : Grafo
        Grafo al cual se le aplicara el algoritmo dijkstra.
    inicio : Vertice
        Vertice inicial del grafo donde comienza dijkstra.


    """
    cp = ColaPrioridad_minheap()
        
    for vertice in unGrafo:                     # se inicializan los vertices con d = 'infinito'
        vertice.asignarDistancia(999999)
        
    inicio.asignarDistancia(0)  #vertice inicio con d = 0
    cp.construirMonticulo([(v.obtenerDistancia(),v) for v in unGrafo])
    
    #sigue como dijkstra comun
    while not cp.estaVacia():
        verticeActual = cp.eliminarMin()
        
        for verticeSiguiente in verticeActual.obtenerConexiones():    
            nuevaDistancia = verticeActual.obtenerDistancia() + verticeActual.obtenerPonderacion(verticeSiguiente)
            
            if nuevaDistancia < verticeSiguiente.obtenerDistancia():
                verticeSiguiente.asignarDistancia(nuevaDistancia)
                verticeSiguiente.asignarPredecesor(verticeActual)
                cp.decrementarClave(verticeSiguiente,nuevaDistancia)
                
                
                
                
                
                
                
                