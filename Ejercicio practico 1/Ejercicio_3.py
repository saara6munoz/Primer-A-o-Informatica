import numpy as np
import os
os.system("cls")
A = np.random.randint(0, 300, 10)
B = np.random.randint(0, 300, 10)
print("Arreglo A")
print(A)
print("**********************************************************************************")
print("  ")
print("Arreglo B")
print(B)
print("**********************************************************************************")
print("  ")

#Mostrar por pantalla la suma de los elementos de cada arreglo.
print("Muestra la suma de los elementos del arreglo A")
suma = sum(A)
print("La suma total de los numeros es:", suma)
print("**********************************************************************************")
print("  ")
print("Muestra la suma de los elementos del arreglo B")
suma2 = sum(B)
print("La suma total de los numeros es:", suma2)
print("**********************************************************************************")
print("  ")

#Mostrar por pantalla la suma de lo s elementos de ambos arreglo.
print("Muestra la suma de ambos arreglos")
suma3 = sum(A)+sum(B)
print("La suma todal  de ambos arreglos es:",suma3)
print("**********************************************************************************")
print("  ")
 
#Mostrar por pantalla la tabla de multiplicar de los elementos impares del arreglo B.
print("Muestra la tabla de multiplicar con elementos impares del arreglo B")
for a in B:
    if a % 2 != 0:
      print(a, end = " ")
print(" ")
print("**********************************************************************************")
print(" ")
for a in B:
    if a % 2 != 0:
        for j in range(1,11):
                    print(str(a)+" * "+str(j)+" = "+str(a*j))
     
   
 
