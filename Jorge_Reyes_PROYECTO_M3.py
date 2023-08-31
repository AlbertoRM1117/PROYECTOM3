import numpy as np
from random import  randint
from matplotlib import pyplot as plt

#Este programa crea una gráfica de la maquina de Galton

#Creamos las variables de tipo array para almacenar las canicas 
#y tambien el tipo de canicas


contenedor  = [1,2,3,4,5,6,7,8,9,10,11,12]
contenedor_lleno = [0,0,0,0,0,0,0,0,0,0,0,0]
canicas = 3000
saltos = 0

def calcular_canicas():
    """ Funcion que ingresa las canicas a el contenedor """
    for i in range(canicas):
        saltos = -1
        for j in range(12):
            saltos = saltos + randint(0, 1)
        contenedor_lleno[saltos] = contenedor_lleno[saltos] + 1
    return contenedor_lleno 

def graficar():
    """ Función imprime en una gráfica los datos de la funcion
    calcular_canicas
    """
    plt.title('Tablero de máquina de Galton')
    plt.xlabel('Contenedor')
    plt.ylabel('Número de Canicas')
    plt.bar(contenedor, calcular_canicas(),width=-1)
    plt.show()

print(calcular_canicas())    
graficar()  