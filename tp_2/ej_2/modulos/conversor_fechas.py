# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 17:01:42 2022

@author: yamil
"""
from datetime import date



def convertirADatetime(fecha):
    """
    funcion que recibe una fecha (str) con el formato 'dd/mm/aaaa' y retorna
    un objeto date(aaaa,mm,dd).

    Parameters
    ----------
    fecha : str
        fecha que se desea convertir. formato: 'dd/mm/aaaa'.

    Returns
    -------
    fecha_date : object
        fecha convertida a date().

    """
    dia,mes,anio = fecha.split('/')
    dia = int(dia)
    mes = int(mes)
    anio = int(anio)
    fecha_date = date(anio,mes,dia)
    return fecha_date



def convertirAString(fecha):
    """
    funcion que recibe un objeto date(aaaa,mm,dd) y retorna
    una fecha (str) con el formato 'dd/mm/aaaa'.

    Parameters
    ----------
    fecha : object
        fecha date() que se desea convertir a string.

    Returns
    -------
    fecha_string : str
        fecha convertida a string. formato: 'dd/mm/aaaa'.

    """
    dia = str(fecha.day)
    mes = str(fecha.month)
    anio = str(fecha.year)
    fecha_string = dia +'/'+ mes +'/'+ anio
    return fecha_string