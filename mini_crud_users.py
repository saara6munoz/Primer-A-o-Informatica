from csv import list_dialects
import os as clin 
import time as mimir
# DECLARACIÓN DE VARIABLES
op_menu=""
run=""
lista_run=[]
nombre=""
lista_nombres=[]
edad=0
lista_edades=[]
#----------------MENÚ  USUARIOS--------------------
while True:
    op_menu=str(input(''' 
    --------MENÚ-------                  
    1.- Agregar usuario                  
    2.- Listar usuarios                  
    3.- Buscar usuarios por RUN                  
    4.- Salir
    
    Escoja una opción:
    '''))
    if op_menu == '1':
        clin.system("cls")
        run=str(input("Ingrese su RUN: ")).strip()      #No contabiliza los espacios
        while not len(run)>7 or run == '-' :
            print("Error...no puede ser nulo")
            run=str(input("Ingrese su RUN: ")).strip()
        lista_run.append(run)
        
        nombre=str(input("Ingrese su nombre: ")).strip().capitalize()
        while not len(nombre)>0:
            print("Error...no puede ser nulo")
            nombre=str(input("Ingrese su Nombre: ")).strip().capitalize()
        lista_nombres.append(nombre)
        
        edad=int(input("Ingrese su edad: "))
        while not 18 <= edad <= 100:
            print("Pero komo!!11!!!1!1")
            edad=int(input("Ingrese su edad: "))
        lista_edades.append(edad)
        print("Se ingresó el usuario existosamente")
        clin.system("pause")
    if op_menu == '2':
        print("\n--------Lista de Usuarios---------- ")
        for k in range(len(lista_run)):
            print(f'''
           RUN: {lista_run[k]}
           NOMBRE: {lista_nombres[k]}
           EDAD: {lista_edades[k]}
            ''')
        clin.system("pause")
    if op_menu == '3':
        run = str(input("Ingrese su rut: ")).strip().upper()
        if run not in lista_run:
            print("No está registrado")
        else:
            k = lista_run.index(run)
            print(f'''
                {lista_nombres[k]} {lista_edades[k]} años
                ''')
        clin.system("pause")
        print(f''' ''')
    if op_menu == '4':
        respuesta=str(input("¿Está seguro que desea salir de la aplicación? S/N ")).upper()
        if respuesta == 'S':
            mimir.sleep(2)
            break
        else:
            clin.system("pause")
        print(f''' ''')



