def dividir(F):
    """
    Divide el fichero F en ficheros F1 y F2 copiando sublistas 
    naturales ordenadas de F alternativamente en F1 y F2.

    Parameters
    ----------
    F : .txt
        archivo que contiene numeros separados por tabulaciones.
    

    Returns
    -------
    None.

    """
    
    F = open(F, 'r')
    f1 = open('F1.txt', 'w')
    f2 = open('F2.txt', 'w')
    
    
    bandera = True   # controla que las sublistas naturalmente ordenadas
                     # de f se escriban alternadamente en f1 y f2
                     # se inicializa en true escribe primero en f1
    
    linea = F.readline()
    linea_anterior = linea
    
   
    while linea != '':         # mientras no se alcance el final de F
    
        if linea >= linea_anterior:            
            if bandera == True:         # chequea donde se escribe la sublista
                f1.write(linea)                
            elif bandera == False:
                f2.write(linea)
                 
        else:                           # si linea es menor a su siguiente
            if bandera == True:         # escribe el pricipio de la siguiente
                f2.write(linea)         # sublista en el otro archivo
                bandera = False         # bandera cambia su estado
            elif bandera == False:
                f1.write(linea)
                bandera = True
                
        linea_anterior = linea          # actualiza variables auxiliares             
        linea = F.readline()
    
    F.close()
    f1.close()
    f2.close()



    
def mezclar(f1 ,f2):
    """
    Mezcla las sublistas ordenadas de F1 y F2 para producir el fichero F.
    

    Parameters
    ----------
    f1 : .txt
        archivo que contiene numeros separados por tabulaciones.

    f2 : .txt
        archivo que contiene numeros separados por tabulaciones.


    Returns
    -------
    numSublistas : int
        Cantidad de sublistas.

    """
    f1 = open(f1, 'r')
    f2 = open(f2, 'r')
    F = open('datos.txt', 'w')
    numSublistas = 1
    
    linea_f1 = f1.readline()
    linea_anterior_f1 = linea_f1
    
    linea_f2 = f2.readline()
    linea_anterior_f2 = linea_f2
    
    # mientras no se alcance el final de f1 y f2
    while linea_f1 != '' and linea_f2 != '':
        
        # mientras no se alcance el final de las dos sublistas en f1 y f2
        while linea_f1 >= linea_anterior_f1 and linea_f2 >= linea_anterior_f2:
            
            # compara elementos de ambas sublistas para escribir f
            if linea_f1 < linea_f2:
                F.write(linea_f1)
                linea_anterior_f1 = linea_f1
                linea_f1 = f1.readline()
            else:
                F.write(linea_f2)
                linea_anterior_f2 = linea_f2
                linea_f2 = f2.readline()
        
        # si se alcanza el final de la sublista en f1
        if linea_f1 < linea_anterior_f1:
            
            # escribe el resto de la sublista de f2 en f
            while linea_f2 >= linea_anterior_f2:
                F.write(linea_f2)
                linea_anterior_f2 = linea_f2
                linea_f2 = f2.readline()
            linea_anterior_f1 = linea_f1
            linea_anterior_f2 = linea_f2
        
        # si se alcanza el final de la sublista en f2
        elif linea_f2 < linea_anterior_f2:
            
            # escribe el resto de la sublista de f1 en f
            while linea_f1 >= linea_anterior_f1:
                F.write(linea_f1)
                linea_anterior_f1 = linea_f1
                linea_f1 = f1.readline()
            linea_anterior_f1 = linea_f1
            linea_anterior_f2 = linea_f2
        
        numSublistas += 1
    
    # si se alcanza el final de f1
    if linea_f1 == '':
        
        # escribe el resto de f2 en f
        while linea_f2 != '':
            if linea_f2 < linea_anterior_f2:
                numSublistas += 1
            F.write(linea_f2)
            linea_anterior_f2 = linea_f2
            linea_f2 = f2.readline()
    
    # si se alcanza el final de f2
    elif linea_f2 == '':
        
        # escribe el resto de f1 en f
        while linea_f1 != '':
            if linea_f1 < linea_anterior_f1:
                numSublistas += 1
            F.write(linea_f1)
            linea_anterior_f1 = linea_f1
            linea_f1 = f1.readline()
            
    f1.close()
    f2.close()
    F.close()
    return numSublistas


        
def MezclaNatural(F):
    """
    Usa la ordenacion por mezclas natural para ordenar el fichero F.

    Parameters
    ----------
    F : .txt
        archivo que contiene numeros separados por tabulaciones.

    Returns
    -------
    None.

    """
    numSublistas = 0
    
    # llama a dividir y mezclar hasta que f quede ordenado
    while numSublistas != 1:
        dividir(F)
        numSublistas = mezclar('F1.txt','F2.txt')
    from os import remove
    
    # elimina los archivos auxiliares f1 y f2
    remove('F1.txt')
    remove('F2.txt')