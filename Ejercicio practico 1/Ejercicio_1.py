#Crear un arreglo unidimensional con nombre arregloA y de tamaño 100, con elementos aleatorios de números enteros del 0 al 500
import numpy as np
import os
arregloA =np.random.randint(0,500,100)
os.system("cls")
print("Los siguientes numeros son del arreglo de tamaño 100 entre el 0 al 500 aleatorios")
print(" ")
a = print(arregloA, end="," "\n")
print("**********************************************************************************")

#Mostrar por pantalla sólo los valores que se encuentren en los índices pares del arreglo.
print("Indices pares del arreglo son: ")
for num in arregloA:
    if num % 2 == 0:
      print(num, end = " ")
print(" ")
print("**********************************************************************************")
print(" ")

#Mostrar el elemento mayor del arreglo.
print("El numero mayor del arreglo es:")
a = max(arregloA)
print(a)
print("**********************************************************************************")
print("  ")

#Mostrar el índice (posición) del elemento mayor.
print("Mostrar el indice(posicion) del  elemento mayor")
max_value = a
for idx, num in enumerate(arregloA):
    if (max_value is a or num > max_value):
        max_value = num
        max_idx = idx
print('El numero mayor es: ', max_value, "la posicion de ese numero es: ", max_idx)
print("**********************************************************************************")
print("  ")

#Mostrar el elemento menor del arreglo.
print("El numero menor del arreglo es:")
a = min(arregloA)
print(a)
print("**********************************************************************************")
print("  ")

print("Generar la copia de arreglo A y multiplicar por 3 cada elemento. Mostrar resultado.")
arregloB = arregloA
print(arregloB*3, end=" ")
print("  ")
print("**********************************************************************************")
print("  ")

#Mostrar la suma de los elementos del segundo arreglo.
print("Muestra la suma de los elementos del segundo arreglo")
suma = sum(arregloB)
print("La suma total de los numeros es:", suma)
print("  ")
print("**********************************************************************************")
print("  ")

#Calcular el promedio de los elementos del segundo arreglo.
print("Muestra el promedio de los elementos del segundo arreglo")
arregloB = sum(arregloB)/len(arregloB) 
print(arregloB)