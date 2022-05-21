
import random
from random import sample
lista = [1,2,3,4,5,6,7,8,9,10]
lista2 = [11,12,13,14,15,16,17,18]
lista3 = [19,20,21,22,23,24,25,26]
ganador = []
cartolaUsuario= []
print("\n")
print("    ================================")
print("    ***  Seleccione una opcion ***")
print("    ================================\n")
print(" [ 1 ] Todos los numeros aleatorios.")
print(" [ 2 ] Elige unos cuantos numeros y los demas aleatorios.")
print(" [ 3 ] Elige todos los numeros.\n")

opcion = (input("Ingrese su opcion a jugar: "))

if opcion == "1":
    print("\n")
    print("    *** carton del LOTO ***") 

    print(random.sample(lista, 10))
    print(random.sample(lista2, 8))
    print(random.sample(lista3, 8))
    print("\n")
    print(" *** Tus primeros 6 NUMEROS DE TU CARTOLA SERAN ALEATORIOS***")
    lista = sample(range(1, 27), 6)
    print(lista)


elif opcion == "2":
    print("\n")
   
    lista.extend(lista2)
    lista.extend(lista3)
   
    print("***ELIGE UN MAXIMO DE 5 NUMEROS Y LOS DEMAS ALEATORIOS***")
    x = 1
    while x <= 5:
        num = int(input("Ingrese sus numeros: "))
        continuar = input("Si no quieres ingresar mas numeros escribe //continuar// enter para elegir mas")
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
        
elif opcion=="3":
    lista.extend(lista2)
    lista.extend(lista3)

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
    print('   ***tu numeros son***  \n     ',cartolaUsuario)
    