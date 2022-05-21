matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

i = 0   #index fila
while i < matriz.__len__():
    j = 0                               #index columna
    while j < matriz[i].__len__():
        print(matriz[i][j], end =" ")
        j = j + 1
    print("\n")
    i = i + 1

print("----------------------- \n")

i = matriz.__len__() - 1   #index fila
while i >= 0:
    j = 0                               #index columna
    while j < matriz[i].__len__():
        print(matriz[i][j], end =" ")
        j = j + 1
    print("\n")
    i = i - 1

print("----------------------- \n")

i = matriz.__len__() - 1   #index fila
while i >= 0:
    j = 0                               #index columna
    while j < matriz[i].__len__():
        print(matriz[i][j], end =" ")
        j = j + 1
    print("\n")
    i = i - 1