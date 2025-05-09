#Modulos  tipo de importar las clases
from programas.sumas import sumar2
from programas.restas import restar2
from vistas.menu import menu2
from vistas.lineas import lineas2



#Modulos de Python :  
from datetime import datetime
import os 

programa = True

while True:
    os.system("clear")
    print("Hora:", datetime.now().strftime("%H:%M:%S"))



while programa:
    os.system("clear")
    print("Hora:", datetime.now().strftime("%H:%M:%S"))
    print("+-------------------------+")
    lineas2(25)
    menu2()

    res = int(input("|[?]"))

    if res == 1:
        print("Sumar dos numeros")
        sumar2()
        
    elif res == 2:
        print("Resta de dos numeros")
        restar2()

    elif res == 0:
        print("Salir del programa")
        programa = False    


