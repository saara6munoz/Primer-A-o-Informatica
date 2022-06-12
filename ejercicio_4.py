#Crear un arreglo de dos dimensiones de tamaño 4 y 4 con elementos caracteres. Se pide, contar las vocales.
import numpy as np

print("Crear un arreglo de dos dimensiones de tamaño 4 y 4 con elementos caracteres. Se pide, contar las vocales.")
lista = [["a","u","u"],
         ["e","i","e"],
         ["a","i","e"],
         ["o","u","o"]]
matriz = np.array (lista)
print(matriz)
print("la cantidad de la vocal (a) son: ",sum(map(lambda x : 1 if 'a' in x else 0, matriz)))
print("la cantidad de la vocal (e) son: ",sum(map(lambda x : 1 if 'e' in x else 0, matriz)))
print("la cantidad de la vocal (i) son: ",sum(map(lambda x : 1 if 'i' in x else 0, matriz)))
print("la cantidad de la vocal (o) son: ",sum(map(lambda x : 1 if 'o' in x else 0, matriz)))
print("la cantidad de la vocal (u) son: ",sum(map(lambda x : 1 if 'u' in x else 0, matriz)))