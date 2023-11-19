# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 19:31:47 2022

@author: yamil
"""

from modulos.Temperaturas_DB import Temperaturas_DB

def main():
    
    base = Temperaturas_DB()
    base.guardar_temperatura(20.1,'25/4/2001')
    base.guardar_temperatura(24.0,'28/4/2001')
    base.guardar_temperatura(20.0, '20/3/2001')
    base.guardar_temperatura(19.2, '04/8/1992')
    base.guardar_temperatura(30.0, '11/9/2001')
    base.guardar_temperatura(40.3, '24/12/2010')
    
    for fecha in base:
        print(fecha)

    print(base.mostrar_cantidad_muestras())
    print(base.devolver_temperatura('25/4/2001'))
    
    print(base.temp_extremos_rango('20/3/2001', '28/4/2001'))
    print(base.max_temp_rango('20/3/2001', '28/4/2012'))
    print(base.min_temp_rango('20/3/2001', '28/4/2001'))
    print(base.mostrar_temperaturas('04/8/1992', '24/12/2010'))
    
    
    
    
if __name__ == "__main__":
    
    main()