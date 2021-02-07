#!/usr/bin/env python
'''
Matplotlib [Python]
Ejercicios de profundización
---------------------------
Autor: Inove Coding School
Version: 1.2

Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "Ezequiel Alarcon"
__email__ = "zekalarcon@gmail.com"
__version__ = "1.2"


'''
NOTA PARA TODOS LOS EJERCICIOS

Para la resolución de todos los problemas utilizará
el dataset "ventas.csv".

Desde ahora los de datos los generará c/u
con Numpy o comprensión de listas o ambos, queda
a su elección en cada caso. Si quiere usar Numpy
para todo, puede abrir el archivo directamente con Numpy
y trabajar sin pasar por listas o diccionarios.

TIP: Para abrir el archivo CSV con Numpy y que el header no
     quede mezclado con los datos utilizar:
     data = np.genfromtxt('ventas.csv', delimiter=',')
     # Borro la fila 0 del header, los nombres de las columnas
     data = data[1:,:]

NO están permitidos los bucles en la realización de estos ejercicios.

Descripción del dataset "ventas.csv"
- Este dataset contiene el importe facturado por un local
  en la venta de sus productos dividido en 4 categorías
- Se contabiliza lo vendido por categória al cerrar el día,
  el dataset está ordenado por mes y día
- El dataset contiene 3 meses (genéricos) de 30 días c/u

'''

import csv
from csv import DictReader
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.axes
import mplcursors 




def ej1():
    print('Comenzamos a divertirnos!')

    '''
    Para comenzar a calentar en el uso del dataset se lo solicita
    que grafique la evolución de la facturación de la categoría alimentos
    para el primer mes (mes 1) de facturación.
    Realice un line plot con los datos de facturación de alimentos del mes 1
    Deberá poder observar la evolución de ventas(y) vs días(x)

    TIP:
    1) Para aquellos que utilicen listas siempre primero deberan
    emprezar filtrando el dataset en una lista de diccionarios que
    posee solo las filas y columnas que a están buscando.
    En este caso todas las filas cuyo mes = 1 y solo la columan
    de día(x) y de alimentos(y).
    Una vez que tiene esa lista de dccionarios reducida a la información
    de interés, debe volver a utilizar comprensión de listas para separar
    los datos de los días(x) y de los alimentos(y)

    2) Para aquellos que utilicen Numpy, si transformaron su CSV en Numpy
    les debería haber quedado una matriz de 6 columnas y de 90 filas
    (recordar sacar la primera fila que es el header)
    mes | dia | alimentos | bazar | limpieza | electrodomesticos
    Luego si quisieramos acceder a solo la columna de los dias (col=1)
    podemos utilizar slicing de Numpy:
    dias = dataset[:, 1]
    ¿Cómo puedo obtener las filas solo del primer mes?
    Aplicando mask de Numpy:
    mes_1 --> col = 0
    filas_mes_1 = dataset[:, 0] == 1
    Obtengo solos los datos del mes uno
    mes_1 = dataset[filas_mes_1, :]

    x --> dias
    Obtengo solo los dias del mes1 de alimentos
    x = dataset[filas_mes_1, 1]
    o tambien puede usar
    x = mes_1[:, 1]

    y --> alimentos
    Obtengo solo los alimentos del mes1 de alimentos
    y = dataset[filas_mes_1, 2]
    o tambien puede usar
    y = mes_1[:, 2]

    '''

  
    with open('ventas.csv', 'r') as f:
        reader = DictReader(f)
        lista_filtrada = [x for x in reader if x['Mes'] == '1']
        alimentos_mes_1 = [x['Alimentos'] for x in lista_filtrada]
        dias_mes_1 = [x['Dia'] for x in lista_filtrada]
        
        fig, ax = plt.subplots()
        fig.suptitle('Facturacion Alimentos Mes 1')

        ax.plot(dias_mes_1, alimentos_mes_1, c = 'orange')
        ax.grid(c = 'silver', ls = '--')
        ax.set_facecolor('honeydew')
        ax.set_xlabel('DIAS')
        ax.set_ylabel('FACTURACION')

        plt.show()


def ej2():
    print('Comenzamos a ponernos serios!')

    '''
    Queremos visualizar como ver la tendencia de venta de los alimentos
    a lo largo de todo el año.
    Para eso queremos utilizar el método "np.diff" para obtener la diferencia
    día a día de lo vendido.

    Se debe poder primero discriminar las ventas por la categoría Alimentos,
    1) en el caso de usar listas se debe generar una lista de solo
       ventas de aliementos de todo el año.
    2) En el caso de usar numpy no hace falta generar una lista/array aparte,
       pero si le resulta comodo puede hacerlo.

    Luego que tienen discriminadas las ventas por alimento aplicar el método
    np.diff
    tendencia = np.diff(mis ventas de alimentos)

    Graficar el valor obtenido con un Line Plot

    NOTA: Importante!, en este caso no disponen facilmente del eje "X" de diff,
    para simplificar el caso solamente graficar la variable "tendencia"
    plot(tendencia)

    '''

    with open('ventas.csv', 'r') as f:
        reader = DictReader(f)
        alimentos_año = [int(x['Alimentos']) for x in reader]
        tendencia = np.diff(alimentos_año)
        
        fig, ax = plt.subplots()
        fig.suptitle('Diferencias Facturacion Alimentos')

        ax.plot(tendencia, c = 'orange')
        ax.grid(c = 'silver', ls = '--')
        ax.set_facecolor('honeydew')
        ax.set_xlabel('DIAS')
        ax.set_ylabel('DIFERENCIA')
        mplcursors.cursor(multiple=True)

        plt.show()
        
        

def ej3():
    print("Buscando la tendencia")

    '''
    Si observa el dataset, los electrodomésticos no siempre
    tienen facturación al finalizar el día.
    Deseamos que generen una nueva lista/array/columna
    en la cual coloquen un "1" si ese día se vendió electrodomésticos
    o un "0" sino se vendio nada (facturación = 0).
    Luego graficar utilizando Line Plot esta nueva lista/array/columna
    para visualizar la tendencia de cuantos días consecutivos hay
    ventas de electrodomésticos.

    '''


    with open('ventas.csv', 'r') as f:
        reader = DictReader(f)
        electrodomesticos_año = [int(x['Electrodomesticos']) for x in reader]
        electros_filtrados = [1 if x != 0 else 0 for x in electrodomesticos_año  ]
        
        fig, ax = plt.subplots()
        fig.suptitle('Electrodomestico Tendencia Ventas')

        ax.plot(electros_filtrados, c = 'orange')
        ax.grid(c = 'silver', ls = '--')
        ax.set_facecolor('honeydew')
        ax.set_xlabel('DIAS')
        ax.set_ylabel('VENTAS')
        mplcursors.cursor(multiple=True)

        plt.show()

def ej4():
    print("Exprimiendo los datos")

    '''
    Obtener la facturación total (la suma total en los 3 meses)
    de cada categória por separado. Nos debe quedar el total
    facturado en alimentos, en bazar, en limpieza y en
    electrodomesticos por separado (son 4 valores)

    TIP:
    1) para los que usan listas, para poder obtener estos
    valores primero deberan generar una lista de cada categoría,
    para luego poder aplicar operaciones como sum.
    2) Para los que usan numpy pueden usar directamente np.sum
    y especificando el axis=0 estarán haciendo la suma total de la columna

    Con la información obtenida realizar un Pie Plot
    para visualizar que categoría facturó más en lo que va
    del año
    '''


    with open('ventas.csv', 'r') as f:
        reader = DictReader(f)
        categorias_año = [[int(x['Alimentos']), int(x['Bazar']), int(x['Limpieza']),int(x['Electrodomesticos'])] for x in reader]
        
        sum_alimentos = sum([x[0] for x in categorias_año])
        sum_bazar = sum([x[1] for x in categorias_año])
        sum_limpieza = sum([x[2] for x in categorias_año])
        sum_electrodomesticos = sum([x[3] for x in categorias_año])

        cantidades = [sum_alimentos, sum_bazar, sum_limpieza, sum_electrodomesticos]
        labels = ['Alimentos', 'Bazar', 'Limpieza', 'Electrodomesticos']
        explode = (0,0,0,0.1)
        
        fig, ax = plt.subplots()
        fig.suptitle('Facturacion Anual Productos')

        ax.pie(cantidades, explode = explode,
          colors = ['orange', 'red', 'dodgerblue', 'forestgreen'],
          labels = labels, autopct='%1.1f%%', shadow=True, startangle=90)
        ax.axis('equal') 

        plt.show()
           

def ej5():
    print("Ahora sí! buena suerte :)")

    '''
    Ahora que ya hemos jugado un poco con nuestro dataset,
    queremos realizar 3 gráficos de columnas en una misma figura
    Cada gráfico de columnas deben tener 4 columnas que representan
    el total vendido de cada categoría al final del mes.
    Para poder hacer este ejercicio deben obtener primero
    total facturado por categoria por mes (deben filtrar por mes)
    Es parecido a lo realizado en el ejercicio anterior pero en vez
    de todo el año es la suma total por mes por categoría.

    Siendo que son 4 categorías y 3 meses, deben obtener al final
    12 valores, con esos 12 valores construir 3 listas/arrays
    para poder mostrar los 3 gráficos de columnas

    BONUS Track: Si están cancheros y aún quedan energías para practicar,
    les proponemos que en vez de realizar 3 gráficos de columnas separados
    realicen uno solo y agrupen la información utilizando gráfico de barras
    apilados o agrupados (a su elección)
    '''

    
    with open('ventas.csv', 'r') as f:
        reader = DictReader(f)
        lista_filtrada = [x if x['Mes'] == '1' else x if x['Mes'] == '2' else x for x in reader]
        
        categorias_mes_1 = [[int(x['Alimentos']), int(x['Bazar']), int(x['Limpieza']),int(x['Electrodomesticos'])] for x in lista_filtrada if x['Mes'] == '1']
        categorias_mes_2 = [[int(x['Alimentos']), int(x['Bazar']), int(x['Limpieza']),int(x['Electrodomesticos'])] for x in lista_filtrada if x['Mes'] == '2']
        categorias_mes_3 = [[int(x['Alimentos']), int(x['Bazar']), int(x['Limpieza']),int(x['Electrodomesticos'])] for x in lista_filtrada if x['Mes'] == '3']

         # Mes 1 Sumas

        alimentos_mes_1 = sum([x[0] for x in categorias_mes_1])
        bazar_mes_1 = sum([x[1] for x in categorias_mes_1])
        limpieza_mes_1 = sum([x[2] for x in categorias_mes_1])
        electro_mes_1 = sum([x[3] for x in categorias_mes_1])

        mes1 = [alimentos_mes_1,bazar_mes_1,limpieza_mes_1,electro_mes_1]

        # Mes 2 Sumas

        alimentos_mes_2 = sum([x[0] for x in categorias_mes_2])
        bazar_mes_2 = sum([x[1] for x in categorias_mes_2])
        limpieza_mes_2 = sum([x[2] for x in categorias_mes_2])
        electro_mes_2 = sum([x[3] for x in categorias_mes_2])

        mes2 = [alimentos_mes_2,bazar_mes_2,limpieza_mes_2,electro_mes_2]

        # Mes 3 Sumas

        alimentos_mes_3 = sum([x[0] for x in categorias_mes_3])
        bazar_mes_3 = sum([x[1] for x in categorias_mes_3])
        limpieza_mes_3 = sum([x[2] for x in categorias_mes_3])
        electro_mes_3 = sum([x[3] for x in categorias_mes_3])

        mes3 = [alimentos_mes_3, bazar_mes_3, limpieza_mes_3, electro_mes_3]


        # Grafico Separados


        productos = ['Alimentos', 'Bazar', 'Limpieza', 'Electros']

        fig, (ax1, ax2, ax3) = plt.subplots(1,3)
        fig.suptitle('Ventas Productos Mensuales')

        ax1.bar(productos,mes1, color = 'orange')
        ax2.bar(productos,mes2, color = 'royalblue')
        ax3.bar(productos,mes3, color = 'lightseagreen')
        ax1.set_xlabel('MES 1')
        ax2.set_xlabel('MES 2')
        ax3.set_xlabel('MES 3')
        ax1.set_ylabel('CANTIDAD')

        for ax in fig.get_axes():
            ax.grid(c = 'silver', ls = 'dotted')
            ax.set_facecolor('aliceblue')
            
        plt.show()


        # Grafico todo en uno


        alimentos = [mes1[0], mes2[0], mes3[0]]
        bazar = [mes1[1], mes2[1], mes3[1]]
        limpieza = [mes1[2], mes2[2], mes3[2]]
        electros = [mes1[3], mes2[3], mes3[3]]

        width = 0.2

        x1 = np.arange(len(alimentos))
        x2 = [x + width for x in x1]
        x3 = [x + width for x in x2]
        x4 = [x + width for x in x3]

        fig, ax = plt.subplots()
        fig.suptitle('Ventas Productos Mensuales')

        ax.bar(x1, alimentos, width=width, edgecolor='honeydew', label='Alimentos')
        ax.bar(x2, bazar, width=width, edgecolor='honeydew', label='Bazar')
        ax.bar(x3, limpieza, width=width, edgecolor='honeydew', label='Limpieza')
        ax.bar(x4, electros, width=width, edgecolor='honeydew', label='electros')
        ax.grid(c = 'silver', ls = 'dotted')
        ax.set_facecolor('honeydew')
        ax.set_ylabel('CANTIDAD')
        ax.legend()
        
        plt.xticks([x + 0.3 for x in range(len(alimentos))], ['Mes 1', 'Mes 2', 'Mes 3'])

        plt.show()



if __name__ == '__main__':
    print("Ejercicios de práctica")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
    #ej5()
