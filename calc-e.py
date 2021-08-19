"""
Program By Jesús Adeódato López Carranza 
All rights reserve to its creator at https://github.com/Adeodato-Alpha/Adeodas.git
"""
from math import *
import math as mt
from decimal import Decimal, getcontext
getcontext().prec= 10000
"""
El getcontext nos ayudará a que nos arroje el numero de
decimales que se le ponga como valor, en este caso como queremos los primeros 10000 
le dejamos en claro a la variable que los resultados nos los tendría que arrojar con esa 
cantidad de decimales. 
"""
#Para la creación de este programa se usó el algoritmo de la sumatoria de Taylor 
"""
Decimal(número) es cómo se deja en claro al lenguaje de programación de
que queremos manejar los decimales de manera que por así decirlo, se nos enseño, ya que 
al momento de imprimir ciertos números con decimales, la terminal nos imprime números flotantes de punto binario,
lo cual en ciertos casos se llega a presentar como algo que puede desconcertar a la persona ya que los decimales tienden a arrojar
otro tipo de resultados que se nos enseño a leer desde pequeños, Ej: Cuando se llegan a realizar 
algunas sumas cómo  1.1 + 2.2 = 3.3000000000000003
"""
def cal_e():
    ne = Decimal(0)
    s = Decimal(0)
    #ejecutamos la sumatoria de Taylor
    for i in range(100):
        s = Decimal(1)/(mt.factorial(i))
        ne = ne + s
    return ne 

print(cal_e())
