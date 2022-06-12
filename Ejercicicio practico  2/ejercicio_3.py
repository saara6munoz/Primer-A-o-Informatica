#Crear un arreglo de dos dimensiones de tamaño 4 y 5, con elementos aleatorios de números enteros del 0 al 100, luego

import numpy as np
A = np.random.randint(0,100,(4,5))
print("El arreglo es:\n",A)

#Mostrar por pantalla la suma de los elementos de cada fila.
print("Mostrar por pantalla la suma de los elementos de cada fila.")
s = np.sum(A, axis=1)
print(s)
print(" ")

#Mostrar por pantalla la suma de los elementos de cada columna.
print("Mostrar por pantalla la suma de los elementos de cada columna.")
suma = np.sum(A, axis=0)
print(suma)
print(" ")

#Mostrar por pantalla la suma de los elementos de la diagonal principal
print("Mostrar por pantalla la suma de los elementos de la diagonal principal")
print("NO SE PUEDE SUMAR ALGO EN DIAGONAL SI EL ARREGLO NO ES CUADRADO")
print(" ")
#Mostrar por pantalla la cantidad de elementos impares.
impar = 0
print("Los numeros impares son:")
a = A[0]
for num in a:
    if num % 2 != 0:
        impar += 1     
b =A[1]
for num in b:
    if num % 2 != 0:
      impar += 1      
c =A[2]
for num in c:
    if num % 2 != 0:
      impar += 1  
d =A[3]
for num in d:
    if num % 2 != 0:
        impar += 1    
print("La cantidad de impares del arreglo son:",impar)
