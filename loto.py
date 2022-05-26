#-----------------IMPORTACIONES DE LIBRERIAS------------------------------------------
import time
import random
from random import sample
import os

#-----------------lISTAS------------------------------------------
lista = [1,2,3,4,5,6,7,8,9,10]
lista2 =[11,12,13,14,15,16,17,18,19,20]
lista3 =[21,22,23,24,25,26,27,28,29,30]
lista4 =[31,32,33,34,35,36,37,38,39,40,41]
"""ganador = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]"""
loto = []
cartolaUsuario= []

 #-----------------MENU DEL LOTO------------------------------------------
os.system("cls")    
print("================================")
print("***   BIENVENIDO AL LOTO  ***")
print("================================\n")
print("\n")    
time.sleep(2)   
os.system("cls")    
print("================================")
print("***  Seleccione una opcion ***")
print("================================\n")
time.sleep(2)   
print("[ 1 ] Todos los numeros aleatorios.")
print("[ 2 ] Elige unos cuantos numeros y los demas aleatorios.")
print("[ 3 ] Elige todos los numeros.\n")

#-----------------OPCION 1 ------------------------------------------
opcion = (input("Ingrese su opcion a jugar: "))
if opcion == "1":
    os.system("cls")
    print("Has seleccionado la  opcion 1 espere porfavor...")
    time.sleep(2)
    os.system("cls")
    print("*** carton del LOTO ***") 


    print(random.sample(lista, 10))
    print(random.sample(lista2, 10))
    print(random.sample(lista3, 10))
    print(random.sample(lista4, 11))
    print("\n")
    print("*** Tus primeros 6 NUMEROS DE TU CARTOLA SERAN ALEATORIOS ***")
    lista = sample(range(1, 41), 6)
    cartolaUsuario = lista 
    print(cartolaUsuario)
    print("----")
    
    
    print("----")
    lista = sample(range(1, 41), 6)
    loto = lista
    print(loto)
   
    
    if cartolaUsuario==loto:
        print("HAS GANADO EL LOTO!!!")
    else:
        print("HAS PERDIDO EL LOTO:(")
    """
    time.sleep(3)
    print("Acontinuacion se elegira al GANADOR!!!!")
    time.sleep(4)
    """
#-----------------OPCION 2------------------------------------------

elif opcion == "2":
    os.system("cls")
    print("Has seleccionado la  opcion 2 espere porfavor...")
    time.sleep(2)
    os.system("cls")
    print("\n")
    lista.extend(lista2)
    lista.extend(lista3)
    lista.extend(lista4)
    print("***ELIGE UN MAXIMO DE 5 NUMEROS Y LOS DEMAS ALEATORIOS***")
    x = 1
    while x <= 5:
        num = int(input("Ingrese sus numeros: "))
        continuar = input("Si no quieres ingresar mas numeros escribe //continuar// enter para elegir mas: ")
        if num not in cartolaUsuario:
            cartolaUsuario.append(num)
            x += 1
            lista.remove(num)
            if continuar=="continuar":
                print("\n")
                print('   ***tu numeros son***  \n     ',cartolaUsuario)
                print("Los demas numeros de tu cartola son ")    
                print(random.sample(lista,20))
            
        else:
            print("El número está repetido, inténtelo con otro...")
    print("\n")
    print('   ***tu numeros son***  \n     ',cartolaUsuario)
    print("Los demas numeros de tu cartola son ")    
    print(random.sample(lista,20))   
#-----------------OPCION 3 ------------------------------------------        
elif opcion=="3":
    os.system("cls")
    print("Has seleccionado la  opcion 3 espere porfavor...")
    time.sleep(2)
    os.system("cls")
    lista.extend(lista2)
    lista.extend(lista3)
    lista.extend(lista4)

    print("***ELIGE TODO LOS NUMEROS ***")
    x = 1
    while x <= 6:
        num = int(input("Ingrese sus numeros: "))
        if num not in cartolaUsuario:
            cartolaUsuario.append(num)
            x += 1
            lista.remove(num)
        else:
            print("El número está repetido, inténtelo con otro...")
    print("\n")
    print('   ***tu numeros son***  \n ',cartolaUsuario)


