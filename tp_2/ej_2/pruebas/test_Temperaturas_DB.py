# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 10:13:38 2022

@author: yamil
"""

from modulos.Temperaturas_DB import Temperaturas_DB
from modulos.conversor_fechas import convertirADatetime
import unittest


class TestTemperaturasDB(unittest.TestCase):

    def setUp(self):
        self.base = Temperaturas_DB()

        self.base.guardar_temperatura(20.1,'25/4/2001')
        self.base.guardar_temperatura(7.3,'28/8/2019')
        self.base.guardar_temperatura(8.0, '24/6/1987')
        self.base.guardar_temperatura(10.2, '19/6/1999')
        self.base.guardar_temperatura(25.0, '22/8/1995')
        self.base.guardar_temperatura(25.0, '09/11/1989')
        self.base.guardar_temperatura(40.3, '24/12/2012')
        
    
    # chequeo que las mediciones se hayan cargado correctamente a la base de datos
    def test_temperaturas_correctamente_cargadas(self):
        fecha_anterior = convertirADatetime('24/6/1987')
        for fecha in self.base:
            self.assertTrue(fecha_anterior <= fecha)
            fecha_anterior = fecha
        
    
    # chequeo que la temperatura consultada corresponda a la fecha ingresada como parametro
    def test_devolver_temperatura(self):
        temperatura_consultada = self.base.devolver_temperatura('25/4/2001')
        self.assertEqual(temperatura_consultada, 20.1)
        
    
    # chequeo que el valor maximo devuelto por el metodo a testear corresponda al maximo en el rango de fechas consultado
    def test_max_temp_rango(self):
        temp_max_consulta = self.base.max_temp_rango('24/6/1987', '24/12/2012')
        self.assertEqual(temp_max_consulta, 40.3)
        
    
    # chequeo que el valor minimo devuelto por el metodo a testear corresponda al minimo en el rango de fechas consultado
    def test_min_temp_rango(self):
        temp_min_consulta = self.base.min_temp_rango('22/8/1995', '28/8/2019')
        self.assertEqual(temp_min_consulta, 7.3)
        
    
    # chequeo que los extremos devueltos por el metodo a testear correspondan a los extremos en el rango de fechas consultado
    def test_temp_extremos_rango(self):
        temp_min_consulta, temp_max_consulta = self.base.temp_extremos_rango('22/8/1995', '24/12/2012')
        self.assertEqual(temp_min_consulta, 10.2)
        self.assertEqual(temp_max_consulta, 40.3)
        
    
    # chequeo que la medicion eliminada no se encuentre en la base de datos           
    def test_borrar_temperatura(self):
        self.base.borrar_temperatura('24/12/2012')
        fecha_medicion_eliminada = convertirADatetime('24/12/2012')
        for fecha in self.base:
            self.assertFalse(fecha == fecha_medicion_eliminada)
            
    
    # chequeo que la lista que retorna el metodo a testear contenga las mediciones en el formato adecuado
    def test_mostrar_temperaturas(self):
        lista_temperaturas = self.base.mostrar_temperaturas('24/6/1987', '28/8/2019')
        self.assertTrue(lista_temperaturas[0] == '24/6/1987: 8.0°C')
        
    
    # chequeo que el valor retornado por el metodo a testear corresponda con la cantidad de mediciones en la base de datos
    def test_mostrar_cantidad_muestras(self):
        cantidad_muestras = self.base.mostrar_cantidad_muestras()
        self.assertEqual(cantidad_muestras, 7)
        
    
        

if __name__=='__main__':
    
    unittest.main()