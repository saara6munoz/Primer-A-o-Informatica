# Crear un arreglo unidimensional con nombre arreglo_1 y de tamaño 10, con elementos aleatorios de números enteros del 0 al 1000
import numpy as np
import os
arreglo_1 = np.random.randint(0, 1000, 10)
os.system("cls")
print("Numeros del arreglo_1 con tamaño 10 y con elementos aleatorios entre el 0 y el 1000")
print(" ")
print(arreglo_1)
print("********************************")

# Contar los elementos pares.
par = 0

for num in arreglo_1:
    if num % 2 == 0:
        par += 1
print("La cantidad de numeros pares dentro del arreglo son en total:", par)
print("********************************")
print(" ")

# Sumas los numeros impares .
suma = 0
print("Los numeros impares son:")
for num in arreglo_1:
    if num % 2 != 0:
        print(num, end=" ")
for x in range(0, len(arreglo_1)):
    if arreglo_1[x] % 2 != 0:
        suma += arreglo_1[x]
print(" ")
print("la suma  de esos numeros es: ", suma)
print("********************************")
print(" ")

# Muesta un mensaje cuando haya un numero primo.
print("Emitir mensaje de cada elemento que sea primo.")
numero = 2
for numero in arreglo_1:
    for n in range(2, int(numero/2)+1):
        if (numero % n) == 0:
            print("No hay ningun numero primo")
            break
    else:
        print("Se ha encontrado un numero primo:", numero)
