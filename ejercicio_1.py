#Crear dos arreglos de dos dimensiones de tamaño 3 x 3, con elementos de tipo numérico entero
import numpy as np
A =np.array(
    [[1,2,3],
    [5,6,7]]
    )
B = np.array(
    [[4,3,2,],
    [8,7,6,]]
    )

#Muestre la matriz resultante de la multiplicación de la matriz 1 y matriz 2.

print("Matriz A:\n",A,"\n")
print("Matriz B:\n",B,"\n")
print("Matriz resultante de la multiplicación de la matriz 1 y matriz 2.")
result = [[0,0,0,0],
         [0,0,0,0]]
for i in range(len(A)):
   for j in range(len(B[0])):
       for k in range(len(A)):
           result[i][j] += B[i][k] * B[k][j]
for r in result:
   print(r)



