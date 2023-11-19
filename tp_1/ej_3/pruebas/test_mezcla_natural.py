# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 20:07:24 2022

@author: yamil
"""

from modulos.generador_de_datos import crear_archivo_de_datos
from modulos.mezcla_natural import MezclaNatural
import unittest
from pathlib import Path


class TestMezclaNatural(unittest.TestCase):

    def setUp(self):
        crear_archivo_de_datos('datos.txt')
        self.file_size = Path(r'datos.txt').stat().st_size
        
        MezclaNatural('datos.txt')
        self.file_out_size = Path(r'datos.txt').stat().st_size
        
    
    def test_arch_igual_tamanio(self):
        self.assertEqual(self.file_size, self.file_out_size)
        
    
    def test_arch_ordenado(self):
        F = open('datos.txt','r')
        linea = F.readline()
        linea_anterior = linea
        
        while linea != '':
        
            self.assertTrue(linea >= linea_anterior)
            
            linea_anterior = linea          
            linea = F.readline()
                
        

if __name__=='__main__':
    
    unittest.main()