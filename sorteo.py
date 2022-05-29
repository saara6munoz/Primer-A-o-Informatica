# -----------------IMPORTACIONES DE LIBRERIAS------------------------------------------
import os
import time
from random import sample

# -----------------lISTAS--------------------------------------------------------------
lista = [i for i in range(1, 43)]
loto = []
cartolaUsuario = []
hits = 0
# -----------------MENU DEL LOTO-------------------------------------------------------
os.system("cls")
print("================================")
print("***   BIENVENIDO AL LOTO  ***")
print("================================\n")
print("\n")
time.sleep(4)  # Tiempo de espera
os.system("cls")  # Limpia la pantalla
print("=========================================")
print("***  SELECCIONE UNA OPCION A JUGAR ***")
print("=========================================\n")
time.sleep(2)
print("[ 1 ] Todos los numeros aleatorios.")
print("[ 2 ] Elige unos cuantos numeros y los demas aleatorios.")
print("[ 3 ] Elige todos los numeros.\n")
# ----------------- OPCION 1 -------------------------------------------------------------
opcion = (input("Ingrese su opcion a jugar: "))
if opcion == "1":
    os.system("cls")
    print("Has seleccionado la  opcion 1 espere porfavor...")
    time.sleep(2)
    os.system("cls")
    print("    *** Juego 1 ***")
    print("""
[1][2][3][4][5][6][7][8][9][10][11]
[12][13][14][15][16][17][18][19][20][21]
[22][23][24][25][26][27][28][29][30][31]
[32][33][34][35][36][37][38][39][40][41]
    """)
    time.sleep(2)
    print("***Generando tus numeros, espere porfavor... ***")
    time.sleep(3)
    os.system("cls")
    print("\n")
    print("*** TUS NUMEROS A JUGAR SERAN ALEATORIOS  ***")
    lista = sample(range(1, 41), 6)
    cartolaUsuario = lista
    print(cartolaUsuario)
    print("Generando numeros ganadores...")
    time.sleep(5)
    print("-----------------------")
    print("Los numeros ganadores son")
    lista = sample(range(1, 41), 6)
    loto = lista
    print(loto)
    print("-----------------------")
    for number in loto:
        if number in cartolaUsuario:
            hits += 1
    print("Le has atinado a ", hits, "numeros")
    if hits == 4:
        print("Has ganado un premio de $10.000")
    elif hits == 5:
        print("Has ganado un premio de $100.000")
    elif hits == 6:
        print("Felicidades tienes el carton ganador, el premio es de 10 millones!!!!")
    else:
        print("============= HAS PERDIDO EL LOTO======================")


# -----------------OPCION 2------------------------------------------

elif opcion == "2":
    os.system("cls")
    print("Has seleccionado la  opcion 2 espere porfavor...")
    time.sleep(2)
    os.system("cls")
    print("             *** JUEGO 1***")
    print("""
    [1][2][3][4][5][6][7][8][9][10][11]
    [12][13][14][15][16][17][18][19][20][21]
    [22][23][24][25][26][27][28][29][30][31]
    [32][33][34][35][36][37][38][39][40][41]
    """)
    time.sleep(2)
    print("*** ELIGE UNA OPCION DE  NUMEROS A JUGAR Y LOS DEMAS ALEATORIOS ***")
    print("""[ 1 ]Numeros [ 2 ]Numeros
[ 3 ]Numeros [ 4 ]Numeros [ 5 ]Numeros""")

    numero = input("Ingresa la cantidad de numeros que deseas ")
    os.system("cls")
    print("***Preparando juego porfavor espere...***")
    time.sleep(4)
    if numero == "1":
        os.system("cls")
        op = int(input("Elige tu numero:  "))
        lista.remove(op)
        lista = sample(range(1, 40), 5)
        num = op
        cartolaUsuario.append(num)
        cartolaUsuario.extend(lista)
        os.system("cls")
        print("Tu numero elegido es el", num, "tu cartola es")
        carton = set(cartolaUsuario)
        print(carton)
        print("\n")
        print("Generando numeros ganadores...")
        time.sleep(4)
        print("-----------------------")
        print("Los numeros ganadores son")
        lista = sample(range(1, 41), 6)
        loto = lista
        print(loto)
        print("-----------------------")
        for number in loto:
            if number in cartolaUsuario:
                hits += 1
            print("Le has atinado a", hits, "numeros\n")
        if hits == 4:
            print("Has ganado un premio de $10.000")
        elif hits == 5:
            print("Has ganado un premio de $100.000")
        elif hits == 6:
            print("Felicidades tienes el carton ganador, el premio es de 10 millones!!!!")
        else:
            print("============= HAS PERDIDO EL LOTO ======================")
      # -----------------------------------------------------------
    elif numero == "2":
        os.system("cls")
        op = int(input("Elige tu primer numero:  "))
        op2 = int(input("Elige tu segundo numero: "))
        lista.remove(op)
        lista.remove(op2)
        lista = sample(range(1, 39), 4)
        num = op
        num2 = op2
        cartolaUsuario.extend(lista)
        cartolaUsuario.append(num)
        cartolaUsuario.append(num2)
        os.system("cls")
        print("Tu numero elegidos son", num, num2, "tu cartola es ")
        carton = set(cartolaUsuario)
        print(carton)
        print("Generando numeros ganadores...")
        time.sleep(4)
        print("-----------------------")
        print("Los numeros ganadores son")
        lista = sample(range(1, 39), 6)
        loto = lista
        print(loto)
        print("-----------------------")
        for number in loto:
            if number in cartolaUsuario:
                hits += 1
            print("Le has atinado a ", hits, "numeros\n")
        if hits == 4:
            print("Has ganado un premio de $10.000")
        elif hits == 5:
            print("Has ganado un premio de $100.000")
        elif hits == 6:
            print("Felicidades tienes el carton ganador, el premio es de 10 millones!!!!")
        else:
            print("============= HAS PERDIDO EL LOTO ======================")
    # -----------------------------------------------------------
    elif numero == "3":
        os.system("cls")
        op = int(input("Elige tu primer numero:  "))
        op2 = int(input("Elige tu segundo numero: "))
        op3 = int(input("Elige tu tercer numero: "))
        lista.remove(op)
        lista.remove(op2)
        lista.remove(op3)
        lista = sample(range(1, 37), 3)
        num = op
        num2 = op2
        num3 = op3
        cartolaUsuario.extend(lista)
        cartolaUsuario.append(num)
        cartolaUsuario.append(num2)
        cartolaUsuario.append(num3)
        os.system("cls")
        print("Tu numero elegidos son", num, num2, num3, "tu cartola es ")
        carton = set(cartolaUsuario)
        print(carton)
        print("Generando numeros ganadores...")
        time.sleep(4)
        print("-----------------------")
        print("Los numeros ganadores son")
        lista = sample(range(1, 41), 6)
        loto = lista
        print(loto)
        print("-----------------------")
        for number in loto:
            if number in cartolaUsuario:
                hits += 1
            print("Le has atinado a ", hits, "numeros\n")
        if hits == 4:
            print("Has ganado un premio de $10.000")
        elif hits == 5:
            print("Has ganado un premio de $100.000")
        elif hits == 6:
            print("Felicidades tienes el carton ganador, el premio es de 10 millones!!!!")
        else:
            print("============= HAS PERDIDO EL LOTO ======================")

    elif numero == "4":
        os.system("cls")
        op = int(input("Elige tu primer numero:  "))
        op2 = int(input("Elige tu segundo numero: "))
        op3 = int(input("Elige tu tercer numero: "))
        op4 = int(input("Elige tu cuarto numero: "))
        lista.remove(op)
        lista.remove(op2)
        lista.remove(op3)
        lista.remove(op4)
        lista = sample(range(1, 36), 2)
        num = op
        num2 = op2
        num3 = op3
        num4 = op4
        cartolaUsuario.extend(lista)
        cartolaUsuario.append(num)
        cartolaUsuario.append(num2)
        cartolaUsuario.append(num3)
        cartolaUsuario.append(num4)
        print("Tu numero elegidos son", num,
              num2, num3, num4, "tu cartola es ")
        carton = set(cartolaUsuario)
        print(carton)
        print("Generando numeros ganadores...")
        time.sleep(4)
        print("-----------------------")
        print("Los numeros ganadores son")
        lista = sample(range(1, 41), 6)
        loto = lista
        print(loto)
        print("-----------------------")
        for number in loto:
            if number in cartolaUsuario:
                hits += 1
            print("Le has atinado a ", hits, "numeros\n")
        if hits == 4:
            print("Has ganado un premio de $10.000")
        elif hits == 5:
            print("Has ganado un premio de $100.000")
        elif hits == 6:
            print("Felicidades tienes el carton ganador, el premio es de 10 millones!!!!")
        else:
            print("============= HAS PERDIDO EL LOTO======================")

    elif numero == "5":
        op = int(input("Elige tu primer numero:  "))
        op2 = int(input("Elige tu segundo numero: "))
        op3 = int(input("Elige tu tercer numero:"))
        op4 = int(input("Elige tu cuarto numero: "))
        op5 = int(input("Elige tu ultimo  numero: "))
        lista.remove(op)
        lista.remove(op2)
        lista.remove(op3)
        lista.remove(op4)
        lista.remove(op5)
        lista = sample(range(1, 35), 1)
        num = op
        num2 = op2
        num3 = op3
        num4 = op4
        num5 = op5
        cartolaUsuario.extend(lista)
        cartolaUsuario.append(num)
        cartolaUsuario.append(num2)
        cartolaUsuario.append(num3)
        cartolaUsuario.append(num4)
        cartolaUsuario.append(num5)
        print("Tu numero elegidos son", num, num2,
              num3, num4, num5, "tu cartola es ")
        carton = set(cartolaUsuario)
        print(carton)
        print("Generando numeros ganadores...")
        time.sleep(4)
        print("-----------------------")
        print("Los numeros ganadores son")
        lista = sample(range(1, 41), 6)
        loto = lista
        print(loto)
        print("-----------------------")
        for number in loto:
            if number in cartolaUsuario:
                hits += 1
            print("Le has atinado a ", hits, "numeros\n")
        if hits == 4:
            print("Has ganado un premio de $10.000")
        elif hits == 5:
            print("Has ganado un premio de $100.000")
        elif hits == 6:
            print("Felicidades tienes el carton ganador, el premio es de 10 millones!!!!")
        else:
            print("============= HAS PERDIDO EL LOTO ======================")

# -----------------OPCION 3 ------------------------------------------
elif opcion == "3":
    os.system("cls")
    print("Has seleccionado la  opcion 3 espere porfavor...")
    time.sleep(2)
    os.system("cls")
    print("             *** JUEGO 1***")
    print("""
    [1][2][3][4][5][6][7][8][9][10][11]
    [12][13][14][15][16][17][18][19][20][21]
    [22][23][24][25][26][27][28][29][30][31]
    [32][33][34][35][36][37][38][39][40][41]
    """)
    time.sleep(2)
    print("\n")
    print("***ELIGE TODO LOS NUMEROS A JUGAR  ***")
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
    print('***tu numeros son***\n', cartolaUsuario)
    print("Generando numeros ganadores...")
    time.sleep(4)
    print("-----------------------")
    print("Los numeros ganadores son")
    lista = sample(range(1, 41), 6)
    loto = lista
    print(loto)
    print("-----------------------")
    for number in loto:
        if number in cartolaUsuario:
            hits += 1
        print("Le has atinado a ", hits, "numeros")
    print("\n")
    if hits == 4:
        print("Has ganado un premio de $10.000")
    elif hits == 5:
        print("Has ganado un premio de $100.000")
    elif hits == 6:
        print("Felicidades tienes el carton ganador, el premio es de 10 millones!!!!")
    else:
        print("============= HAS PERDIDO EL LOTO ======================")

