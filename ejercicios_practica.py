#!/usr/bin/env python
'''
Matplotlib [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Ezequiel Alarcon"
__email__ = "zekalarcon@gmail.com"
__version__ = "1.1"

import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.axes
import matplotlib.gridspec as gridspec
import mplcursors  # [Opcional cursores]
import matplotlib.ticker as tck


def ej1():
    # Line Plot
    # Se desea graficar los valores de X e Y en un gráfico de línea

    # Función que se desea graficar:
    # y1 = x**2

    x = list(range(-10, 11, 1))
    # Estamos aprovechando el concepto de comprension de listas
    # para generar los valores que toma "Y" por cada valor de "X"
    y = [i**2 for i in x]

    # Crear una "figura" y crear un "ax" con add_subplot
    # Graficar el "line plot" de "Y" en función de "X"
    # Colocar la leyenda y el label con el nombre de la función
    # Darle color a la línea a su elección

    
    fig, ax = plt.subplots()
    fig.suptitle('"Y" en función de "X"')

    ax.plot( x, y, c='orange', marker = '^', ms = 10, label = 'y = x**2')
    ax.set_xlabel('X Label')  
    ax.set_ylabel('Y Label')
    ax.legend()
    ax.grid(c = 'silver', ls='--') 
    ax.set_facecolor('lavenderblush')

    plt.show()



def ej2():
    # Line Plot
    # Se desea graficar varias funciones en un mismmo gráfico (axe)

    # Las funciones que se desean implementar y graficar son:
    # y1 = x**2
    # y2 = x**3

    # Su implementación es la siguiente:
    x = list(np.linspace(-4, 4, 20))
    # Estamos aprovechando el concepto de comprension de listas
    # para generar los valores que toma "Y" por cada valor de "X"
    y1 = [i**2 for i in x]
    y2 = [i**3 for i in x]

    # Realizar un gráfico que representen las dos funciones
    # Para ello se debe llamar dos veces a "plot" con el mismo "ax"

    # Se debe colocar en la leyenda la función que representa
    # cada función

    # Cada función dibujarla con un color distinto
    # a su elección

    fig, ax = plt.subplots()
    fig.suptitle('Dos funciones en el mismo grafico') 

    ax.plot( x, y1, c = 'slateblue', marker ='.', ms = 10, label = 'y1 = x**2')
    ax.plot( x, y2, c = 'orange', marker ='.', ms = 10, label = 'y2 = x**3')
    ax.set_xlabel('EJE X = list(np.linspace(-4, 4, 20))')  
    ax.set_ylabel('EJE Y')
    ax.xaxis.set_minor_locator(tck.AutoMinorLocator())
    ax.yaxis.set_minor_locator(tck.AutoMinorLocator())
    ax.legend()
    ax.grid(c = 'silver', ls = '--') 
    ax.set_facecolor('lavenderblush')

    plt.show()


def ej3():
    # Scatter Plot
    # Se desea graficar la función tanh para el siguiente
    # intervalor de valores de "X"
    x = np.arange(-np.pi, np.pi, 0.1)

    # Función a implementar
    # y = tanh(x) --> tangente hiperbólica

    # Implementacion
    y = np.tanh(x)

    # Graficar la función utilizando "scatter"

    # Se debe colocar en la leyenda la función que representa
    # cada gráfico

    # Elegir un marker a elección

    fig, ax = plt.subplots()
    fig.suptitle('Tangente hiperbolica de X')

    ax.scatter( x, y, c = 'slateblue', marker = '.', label = 'y1 = x**2')
    ax.set_xlabel('EJE X = np.arange(-np.pi, np.pi, 0.1)')  
    ax.set_ylabel('EJE Y = np.tanh(x)')
    ax.xaxis.set_minor_locator(tck.AutoMinorLocator())
    ax.yaxis.set_minor_locator(tck.AutoMinorLocator())
    ax.set_facecolor('lavenderblush')
    ax.grid(c = 'silver', ls= '--')
    ax.legend()

    plt.show()

def ej4():
    # Figura con múltiples gráficos
    # Line Plot
    # Se desea graficar cuatro funciones en una misma figura
    # en cuatros gráficos (axes) distintos. Para el siguiente
    # intervalor de valores de "X":
    x = np.linspace(-10, 10, 40)

    # Realizar tres gráficos que representen
    # y1 = x^2 (X al cuadrado)
    # y2 = x^3 (X al cubo)
    # y3 = x^4 (X a la cuarta)
    # y4 = raiz_cuadrada(X)

    # Implementación:
    y1 = x**2
    y2 = x**3
    y3 = x**4
    y4 = np.sqrt(x)

    # Esos tres gráficos deben estar colocados
    # en la diposición de 3 filas y 1 columna:
    # ------
    #  graf1 | graf2
    # ------
    #  graf3 | graf4
    # Utilizar add_subplot para lograr este efecto
    # de "2 filas" "2 columna" de gráficos

    # Se debe colocar en la leyenda la función que representa
    # cada gráfico

    # Cada gráfico realizarlo con un color distinto
    # a su elección

    # Colocar una grilla a elección

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
    fig.suptitle('Multiples Graficos', fontsize=16)

    ax1.plot(x, y1, 'tab:blue', label = 'y1 = x**2')
    ax2.plot(x, y2, 'tab:orange', label = 'y2 = x**3')
    ax3.plot(x, y3, 'tab:green', label = 'y3 = x**4')
    ax4.plot(x, y4, 'tab:red', label = 'y4 = np.sqrt(x)')

    for ax in fig.get_axes():
        ax.legend()
        ax.grid(c = 'silver', ls= '--')
        ax.xaxis.set_minor_locator(tck.AutoMinorLocator())
        ax.yaxis.set_minor_locator(tck.AutoMinorLocator())
        ax.set_facecolor('lavenderblush')
        mplcursors.cursor(multiple=True)  

    plt.show()


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
    
