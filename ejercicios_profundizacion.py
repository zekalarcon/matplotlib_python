#!/usr/bin/env python
'''
Matplotlib [Python]
Ejercicios de profundización
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
    # Se desea graficar tres funciones en una misma figura
    # en tres gráficos (axes) distintos. Para el siguiente
    # intervalor de valores de x:
   
    # Realizar tres gráficos que representen
    # y1 = x^2 (X al cuadrado)
    # y2 = x^3 (X al cubo)
    # y3 = x^4 (X a la cuarta)
    # Utilizar comprension de listas para generar
    # y1, y2 e y3 basado en los valores de x

    # Esos tres gráficos deben estar colocados
    # en la diposición de 3 filas y 1 columna:
    # ------
    # graf1
    # ------
    # graf2
    # ------
    # graf3
    # ------
    # Utilizar add_subplot para lograr este efecto
    # de "3 filas" "1 columna" de gráficos

    # Se debe colocar en la leyenda la función que representa
    # cada gráfico

    # Cada gráfico realizarlo con un color distinto
    # a su elección

    x = list(range(-10, 11, 1))
    
    y1 = [i**2 for i in x]
    y2 = [i**3 for i in x]
    y3 = [i**4 for i in x]

    fig, (ax1, ax2, ax3) = plt.subplots(3)
    fig.suptitle('Graficos Verticales')

    ax1.plot(y1, 'tab:blue', label = 'y = x**2')
    ax2.plot(y2, 'tab:orange', label = 'y = x**3')
    ax3.plot(y3, 'tab:green', label = 'y = x**4')
    ax3.set_xlabel('EJE X')
    ax2.set_ylabel('EJE Y')

    for ax in fig.get_axes():
        ax.legend()
        ax.grid(c = 'silver', ls = '--')
        ax.xaxis.set_minor_locator(tck.AutoMinorLocator())
        ax.yaxis.set_minor_locator(tck.AutoMinorLocator())
        ax.set_facecolor('lavenderblush')
        mplcursors.cursor(multiple=True)
        
    plt.show()

def ej2():
    # Scatter Plot
    # Se desea graficar dos funciones en una misma figura
    # en dos gráficos (axes) distintos. Para el siguiente
    # intervalor de valores de x:
    
    # Realizar dos gráficos que representen
    # y1 = sin(x)
    # y2 = cos(x)
    # Utilizar los métodos de Numpy para calcular
    # "y1" y "y2" basado en los valores de x

    # Esos dos gráficos deben estar colocados
    # en la diposición de 1 fila y 2 columnas:
    # ------
    #  graf1 | graf2
    # ------
    # Utilizar add_subplot para lograr este efecto
    # de "1 fila" "2 columnas" de gráficos

    # Se debe colocar en la leyenda la función que representa
    # cada gráfico

    # Cada gráfico realizarlo con un mark distinto
    # a su elección.

    x = np.arange(0, 4*np.pi, 0.1)
    y1 = np.sin(x)
    y2 = np.cos(x)

    fig, (ax1, ax2) = plt.subplots(1,2)
    fig.suptitle('Graficos Horizontales')

    ax1.scatter(x, y1, c = 'orange', label = 'y = sin(x)')
    ax2.scatter(x, y2, c = 'blue', label = 'y = cos(x)')

    for ax in fig.get_axes():
        ax.legend()
        ax.grid(c = 'silver', ls = '--')
        ax.xaxis.set_minor_locator(tck.AutoMinorLocator())
        ax.yaxis.set_minor_locator(tck.AutoMinorLocator())
        ax.set_facecolor('aliceblue')
        mplcursors.cursor(multiple=True)

    plt.show()    


def ej3():
    # Bar Plot
    # Generar un gráfico de barras simple a partir
    # de la siguiente información:

    lenguajes = ['Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp']
    performance = [10, 8, 6, 4, 2, 1]

    # Realizar un gráfico de barras en donde se pueda ver el uso
    # de cada lenguaje, se debe utilizar los labels "lenguajes"
    # como valor del eje X

    # Se debe colocar título al gráfico.
    # Se debe cambiar la grilla y el fondo a su elección.

    fig, ax = plt.subplots()
    fig.suptitle('Uso de Lenguajes', fontsize=16)

    ax.bar(lenguajes, performance,
           color = ['lawngreen', 'mediumturquoise', 'coral', 'orange', 'gold','red'],
           label = 'Uso de Lenguajes')
    ax.grid(c = 'silver', ls = 'dotted')
    ax.set_facecolor('aliceblue')
    ax.set_ylabel('Performance')
    ax.set_xlabel('Lenguajes')
    
    plt.show()

def ej4():
    # Pie Plot
    # Se desea realizar un gráfico de torta con la siguiente
    # información acerca del % de uso de lenguajes en nuevos
    # programadores
    uso_lenguajes = {'Python': 29.9, 'Javascript': 19.1,
                     'Go': 16.2, 'Java': 10.5, 'C++': 10.2,
                     'C#': 8.2, 'C': 5.9
                     }

    # El gráfico debe tener usar como label las keys del diccionario,
    # debe usar como datos los values del diccionario
    # Se desea resaltar (explode) el dato de Python
    # Se desea mostrar en el gráfico los porcentajes de c/u
    # Se debe colocar un título al gráfico
    fig, ax = plt.subplots()
    fig.suptitle('Uso de Lenguajes en nuevos Programadores', fontsize = 12)
    
    ax.pie(uso_lenguajes.values(), 
          colors = ['forestgreen', 'springgreen', 'aqua', 'aquamarine', 'lightsteelblue', 'orange' , 'red'],
          labels = uso_lenguajes.keys(), autopct='%1.1f%%', shadow=True, startangle=90)
    ax.axis('equal')       
    plt.show()


def ej5():
    # Uso de múltiples líneas en un mismo gráfico (axes)
    # En el siguiente ejemplo generaremos una señal senoidal
    # haciendo uso solamente de comprension de listas
    step = 0.1
    sample_size = 100
    signal = [{'X': i*step, 'Y': math.sin(i*step)} for i in range(sample_size)]
    

    # Se generó una lista de diccionarios con dos columnas "X" e "Y"
    # que corresponden a los valores de nuestra señal senoidal.
    # Se pide usar comprensión de listas para generar las dos listas
    # por separado de los valoresde "X" e "Y" para poder utilizar
    # el line plot y observar la señal
    
    signal_x = [signals['X'] for signals in signal]
    signal_y = [signals['Y'] for signals in signal]
    

    # plot(signal_x, signal_y)

    fig, ax = plt.subplots()
    fig.suptitle('Señal Senoidal')

    ax.plot(signal_x, signal_y, c = 'orange', label = 'Senoidal')
    ax.grid(c = 'silver', ls = 'dotted')
    ax.set_facecolor('aliceblue')
    ax.legend()
    plt.show()

    # Ahora que han visto la señal senoidal en su gráfico, se desea
    # que generen otras dos listas de "X" e "Y" pero filtradas por
    # el valor de "Y". Solamente se debe completar la lista
    # con aquellos valores de "Y" cuyo valor absoluto (abs)
    # supere 0.7


    filter_signal = [x for x in signal if abs(x['Y']) > 0.7]
    filter_signal_x = [signal['X'] for signal in filter_signal]
    filter_signal_y = [signal['Y'] for signal in filter_signal]


    # Graficar juntas ambos conjuntos de listas y observar
    # el resultado. Graficar filter como scatter plot

    # plot(signal_x, signal_y)
    # scatter(filter_signal_x, filter_signal_y)

    fig, ax = plt.subplots()
    fig.suptitle('Señales Filtradas')

    ax.plot(signal_x, signal_y, c = 'orange', label = 'Senoidal')
    ax.scatter(filter_signal_x, filter_signal_y, label = 'Filtradas')
    ax.grid(c = 'silver', ls = 'dotted')
    ax.set_facecolor('aliceblue')
    ax.legend()

    plt.show()

    # Pueden ver el concepto y la utilidad de
    # realizar un gráfico encima de otro para filtrar datos?


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
    #ej5()
