#Crear un arreglo de dos dimensiones de tamaño 10 y 4,  el cual, simula a un bus. 
#Se pide asignar los números de asiento en forma automática
import numpy as np
A =np.array(
[
[1,2,3,4],
[5,6,7,8],
[9,10,11,12],
[13,14,15,16],
[17,18,19,20],
[21,22,23,24],
[25,26,27,28],
[29,30,31,32],
[33,34,35,36],
[37,38,39,40]
])
print("La matriz es la siguiente:")
for fila in A:
    for valor in fila:
        print("\t", valor, end=" ")
    print()
 
A = np.random.randint(1,40)
print("Tu asiento asignado automaticamente es:",A)
