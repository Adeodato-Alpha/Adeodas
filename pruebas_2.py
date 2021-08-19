"""
Program By Jesús Adeódato López Carranza 
All rights reserve to its creator at https://github.com/Adeodato-Alpha/Adeodas.git
"""
from math import *
import math as mt
from decimal import Decimal, getcontext
#Usaremos el algoritmo de Chudnovsky para el programa
getcontext().prec= 10000
"""
El getcontext nos ayudará a que nos arroje el numero de
decimales que se le ponga como valor, en este caso como queremos los primeros 10000 
le dejamos en claro a la variable que los resultados nos los tendría que arrojar con esa 
cantidad de decimales. 
"""
#uso del modulo Decimal
"""
Decimal(número) es cómo se deja en claro al lenguaje de programación de
que queremos manejar los decimales de manera que por así decirlo, se nos enseño, ya que 
al momento de imprimir ciertos números con decimales, la terminal nos imprime números flotantes de punto binario,
lo cual en ciertos casos se llega a presentar como algo que puede desconcertar a la persona ya que los decimales tienden a arrojar
otro tipo de resultados que se nos enseño a leer desde pequeños, Ej: Cuando se llegan a realizar 
algunas sumas cómo  1.1 + 2.2 = 3.3000000000000003
"""
def calculo():
    numerador = Decimal(0) 
    denominador = Decimal(0) 
    pi = Decimal(0) 
    """
    En esta parte tenemos que dejar en claro que nuestras variables tienen un valor de 0, y como dejamos en claro previamente
    no queremos experimentar problemas con los números flotantes de punto binario por eso es que definimos estas variables con
    Decimal(0), ya que al estar incluidas en el ciclo for estarán agregando valores, por tanto tendrian que empezar en 0. 
    """
    "usamos el algoritmo de Chudnovsky dentro de un ciclo for "
    for i in range(10):
        numerador = ((-1)**i)*(factorial(6*i))*(13591409 + 545140134*i)
        denominador = (factorial(3*i))*(factorial(i)**3)*(640320**(3*i))
        pi = (Decimal(numerador)/Decimal(denominador)) + pi
    #Aqui la ecuación se despeja y crea la variable de valor float con el resultado final
    pi =pi * (Decimal(1)/(Decimal(426880*mt.sqrt(10005))))
    pi = 1/pi
    return pi #Le decimos a la funión que regrese el valor de la función

print(calculo()) #Le pedimos al programa que imprima el valor de retorno de la función 
