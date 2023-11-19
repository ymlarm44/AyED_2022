# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 12:27:13 2022

@author: yamil
"""

from modulos.arboles import AVL, Iterador
from modulos.conversor_fechas import convertirADatetime, convertirAString


class Temperaturas_DB:
    
    def __init__(self):
        self.base = AVL()
        
    def __iter__(self):
        return self.base.__iter__()
    
    def guardar_temperatura(self,temperatura,fecha):
        """
        metodo que guarda la medida de temperatura asociada a la fecha.


        Parameters
        ----------
        temperatura : flaot
            temperatura a registrar.
        fecha : string
            fecha asociada a la temperatura. formato: 'dd/mm/aaaa'.

        Returns
        -------
        None.

        """
        fecha = convertirADatetime(fecha)
        self.base[fecha] = temperatura
 
        
    def devolver_temperatura(self,fecha):
        """
        metodo que devuelve la medida de temperatura en la fecha determinada.


        Parameters
        ----------
        fecha : str
            fecha a consultar. formato: 'dd/mm/aaaa'.

        Returns
        -------
        float
            temperatura asociada a la fecha a consultar.

        """
        fecha = convertirADatetime(fecha)
        return self.base[fecha]
     
 
    def borrar_temperatura(self,fecha):
        """
        metodo que recibe una fecha y elimina de la base de datos la medición 
        correspondiente a esa fecha.

        Parameters
        ----------
        fecha : str
            fecha asociada a la medicion a eliminar. formato: 'dd/mm/aaaa'.

        Returns
        -------
        None.

        """
        fecha = convertirADatetime(fecha)
        self.base.eliminar(fecha)
  
    
    def mostrar_cantidad_muestras(self):
        """
        muestra por consola la cantidad de muestras de la base de datos.

        Returns
        -------
        int
            cantidad de mediciones en la base de datos.

        """
        return self.base.tamano
    
    
    def max_temp_rango(self,fecha1, fecha2):
        """
        devuelve la temperatura máxima entre los rangos fecha1 y fecha2 
        inclusive (fecha1 < fecha2).

        Parameters
        ----------
        fecha1 : str
            fecha fijada como minimo de rango. formato: 'dd/mm/aaaa'.
        fecha2 : str
            fecha fijada como maximo de rango. formato: 'dd/mm/aaaa'.

        Returns
        -------
        float
            medicion maxima correspondiente al rango consultado.

        """
        fecha1 = convertirADatetime(fecha1)
        fecha2 = convertirADatetime(fecha2)
        
        max_temp = self.base.obtener(fecha1)
        
        iterador = Iterador(self.base, fecha1)
        for nodo in iterador:
            if nodo.clave <= fecha2:
                if nodo.cargaUtil > max_temp:
                    max_temp = nodo.cargaUtil
        
        return max_temp
        
        
        # aux = []
        # for fecha in self.base:
        #     if fecha >= fecha1 and fecha <= fecha2:
        #         aux.append(self.base[fecha])
        # return max(aux)
    
    
    def min_temp_rango(self,fecha1, fecha2):
        """
        devuelve la temperatura mínima entre los rangos fecha1 y fecha2 
        inclusive (fecha1 < fecha2).


        Parameters
        ----------
        fecha1 : str
            fecha fijada como minimo de rango. formato: 'dd/mm/aaaa'.
        fecha2 : str
            fecha fijada como maximo de rango. formato: 'dd/mm/aaaa'.

        Returns
        -------
        float
            medicion minima correspondiente al rango consultado.

        """
        fecha1 = convertirADatetime(fecha1)
        fecha2 = convertirADatetime(fecha2)
        
        min_temp = self.base.obtener(fecha1)
        
        iterador = Iterador(self.base, fecha1)
        for nodo in iterador:
            if nodo.clave <= fecha2:
                if nodo.cargaUtil < min_temp:
                    min_temp = nodo.cargaUtil
        
        return min_temp
        
    
        # aux = []
        # for fecha in self.base:
        #     if fecha >= fecha1 and fecha <= fecha2:
        #         aux.append(self.base[fecha])
        # return min(aux)

    
    def mostrar_temperaturas(self,fecha1, fecha2):
        """
        muestra por consola un listado de las mediciones de temperatura en 
        el rango recibido por parámetro con el 
        formato “dd/mm/aaaa: temperatura ºC”, ordenado por fechas. 

        Parameters
        ----------
        fecha1 : str
            fecha fijada como minimo de rango. formato: 'dd/mm/aaaa'.
        fecha2 : str
            fecha fijada como maximo de rango. formato: 'dd/mm/aaaa'.

        Returns
        -------
        aux : list
            listado de mediciones en el rango consultado.

        """
        fecha1 = convertirADatetime(fecha1)
        fecha2 = convertirADatetime(fecha2)
        aux = []
        
        iterador = Iterador(self.base, fecha1)
        
        for nodo in iterador:
            if nodo.clave <= fecha2:
                fecha_string = convertirAString(nodo.clave)
                aux.append(fecha_string + ': ' + str(self.base[nodo.clave]) + '°C')
        return aux
        
        # for fecha in self.base:
        #     if fecha >= fecha1 and fecha <= fecha2:
        #         fecha_string = convertirAString(fecha)
        #         aux.append(fecha_string + ': ' + str(self.base[fecha]) + '°C')
                
    
    def temp_extremos_rango(self,fecha1,fecha2):
        """
        devuelve la temperatura mínima y máxima entre los rangos fecha1 y 
        fecha2 inclusive (fecha1 < fecha2).


        Parameters
        ----------
        fecha1 : str
            fecha fijada como minimo de rango. formato: 'dd/mm/aaaa'.
        fecha2 : str
            fecha fijada como maximo de rango. formato: 'dd/mm/aaaa'.

        Returns
        -------
        float
            medicion minima correspondiente al rango consultado.            
        float
            medicion maxima correspondiente al rango consultado.

        """
        # fecha1 = convertirADatetime(fecha1)
        # fecha2 = convertirADatetime(fecha2)
        
        min_temp = self.min_temp_rango(fecha1, fecha2)
        max_temp = self.max_temp_rango(fecha1, fecha2)
        
        return min_temp, max_temp
        
        
        
        # aux = []
        # for fecha in self.base:
        #     if fecha >= fecha1 and fecha <= fecha2:
        #         aux.append(self.base[fecha])
        # return min(aux), max(aux)
