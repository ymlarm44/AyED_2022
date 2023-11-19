# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 19:46:07 2022

@author: yamil
"""


from modulos.generador_de_datos import crear_archivo_de_datos
from modulos.mezcla_natural import MezclaNatural

def main():
    
    crear_archivo_de_datos('datos.txt')
    MezclaNatural('datos.txt')
    
    
    
if __name__ == "__main__":
    
    main()