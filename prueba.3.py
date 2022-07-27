import numpy as np
import time 
import os as sis
compra=0
total=0
precio=0
ingresados=0
tipo_a=0
tipo_b=0
tipo_c=0
tipo_d=0
precio_tipo_a=0
precio_tipo_b=0
precio_tipo_c=0
precio_tipo_d=0
rut_array = np.empty(40, dtype='object')
fila=np.empty(40,dtype='object')
a = np.empty(10, dtype="object")
b = np.empty(10, dtype="object")
c = np.empty(10, dtype="object")
l=np.empty(27,dtype='object')
d = np.empty(10, dtype="object")
total_ganancias=0
num_asiento=np.empty(40,dtype='object')
for k in range(0,10):
    a[k] = "[ ]"
for k in range(0,10):
    b[k] = "[ ]"
for k in range(0,10):
    c[k] = "[ ]"
for k in range(0,10):
    d[k] = "[ ]"
for k in range(0,20):
    l[k]=(f'{[k+1]}')
for j in range(0,total):
    rut_array[j]=''

#solo mostrar rut

while True:
    sis.system('cls')
    op_menu=str(input('''
    ================================= Bienvenido a Casa Feliz =================================
    1. Comprar departamento
    2. Mostrar departamentos disponibles
    3. Ver listado de compradores 
    4. Mostrar ganancias totales
    5. Salir
    Escoja una opción:  '''))
    if op_menu == '1':
        print("----------- Comprar Departamento ----------")
        ingresados=int(input("Ingrese la cantidad de departamenos que desea comprar: "))
        while ingresados<=0 or ingresados>40:
            ingresados=int(input('\tIngrese cantidad valida:'))
        total+=ingresados
        for k in range (0, ingresados):
            sis.system('cls')
            print ('\t\t    A  B   C  D ')
            for k in range(0,10):
                print (f'''\t\t{l[k]}{a[k]}{b[k]}{c[k]}{d[k]}''')
            rut=str(input("Ingrese su run sin puntos ni digito verificador: "))
            while not len(rut) > 7:
                print("Error el formato de run es incorrecto")
                rut=int(input("Ingrese su run sin puntos ni digito verificador: "))
            num_dep = int(input("Ingrese el número de departamento que desea comprar: "))
            while num_dep<=0 or num_dep>=11:
                print("Error ingrese un numero válido")
                num_dep = int(input("Ingrese el número de departamento que desea comprar: "))
            letra_dep=str(input("Ingrese la letra del departamento: ")).upper()
            while letra_dep not in ['A', 'B', 'C', 'D']:
                print("Ingrese una letra válida...")
                letra_dep=str(input("Ingrese la letra del departamento: ")).upper()
            num_asiento[k]=num_asiento
            fila[k]=letra_dep
        for i in range (0, 40):
            if i==num_dep-1:
                if letra_dep=='A':
                    if a[i]=='X ':
                        print ('Este departamento ya ha sido comprada')
                        num_dep=int(input('seleccione otro número de casa que desee comprar: '))
                        while num_dep<=0 or num_dep>=28:
                            num_dep=int(input('\tseleccione numero valido:'))
                            letra_dep=str(input(f'\tVuelva a seleccionar letra para la casa: ')).upper()
                        while letra_dep not in ['A', 'B', 'C', 'D']:
                            letra_dep=str(input('Seleccione letra válida: ')).upper()
                    else:
                            sis.system('cls')
                            print('Compra realizada exitosamente!')
                            time.sleep(1)
                if letra_dep=='B':
                    if b[i]=='X ':
                        print ('Este departamento ya ha sido comprada')
                        num_dep=int(input('seleccione otro número de casa que desee comprar: '))
                        while num_dep<=0 or num_dep>=28:
                            num_dep=int(input('seleccione número válido: '))
                            letra_dep=str(input(f'\tVuelva a seleccionar letra para la casa: ')).upper()
                        while letra_dep not in ['A', 'B', 'C', 'D']:
                            letra_dep=str(input('Seleccione letra válida: ')).upper()
                    else:
                            sis.system('cls')
                            print('Compra realizada exitosamente!')
                            time.sleep(1)
                if letra_dep=='C':
                    if b[i]=='X ':
                        print ('Este departamento ya ha sido comprada')
                        num_dep=int(input('seleccione otro número de casa que desee comprar: '))
                        while num_dep<=0 or num_dep>=28:
                            num_dep=int(input('seleccione número válido: '))
                            letra_dep=str(input(f'\tVuelva a seleccionar letra para la casa: ')).upper()
                        while letra_dep not in ['A', 'B', 'C', 'D']:
                                letra_dep=str(input('Seleccione letra válida: ')).upper()
                    else:
                            sis.system('cls')
                            print('Compra realizada exitosamente!')
                            time.sleep(1)
                if letra_dep=='D':
                    if b[i]=='X ':
                        print ('Este departamento ya ha sido comprada')
                        num_dep=int(input(f'\tseleccione otro numero de asiento para el pasaje: '))
                        while num_dep<=0 or num_dep>=28:
                            num_dep=int(input('\tseleccione numero valido:'))
                            letra_dep=str(input(f'\tVuelva a seleccionar letra para la casa: ')).upper()
                        while letra_dep not in ['A', 'B', 'C', 'D']:
                                letra_dep=str(input('Seleccione letra válida: ')).upper()
                    else:
                            sis.system('cls')
                            print('Compra realizada exitosamente!')
                            time.sleep(1)
        for k in range(0,40):
            if k == num_dep - 1:
                if letra_dep=='A':
                    if a[k]=='[ ]':
                        a[k]=' X '
                if letra_dep=='B':
                    if b[k]=='[ ]':
                        b[k]=' X '
                if letra_dep=='C':
                    if c[k]=='[ ]':
                        c[k]=' X '
                if letra_dep=='D':
                    if d[k]=='[ ]':
                        d[k]=' X '
        if letra_dep == 'A':
            precio=3800
            precio_tipo_a+=precio
            tipo_compra='A'
            tipo_a += 1
        if letra_dep == 'B':
            precio = 3000
            precio_tipo_b+=precio
            tipo_compra='B'
            tipo_b += 1
        if letra_dep == 'C':
            precio = 2800
            precio_tipo_c+=precio
            tipo_compra='C'
            tipo_c += 1
        if letra_dep == 'D':
            precio = 3500
            precio_tipo_d+=precio
            tipo_compra='D'
            tipo_d += 1
        rut_array[k]=rut 
        total_ganancias+=precio
        compra+=1    
    elif op_menu == '2':
        sis.system("cls")
        print('''\t
        [ ]=DISPONIBLE
        X=RESERVADO
        ''')
        print("----------- Mostar Departamentos Disponibles ----------")
        print ('\t\t    A  B   C  D ')
        for k in range(0,10):
            print (f'''\t\t{l[k]}{a[k]}{b[k]}{c[k]}{d[k]}''')
        sis.system ('pause')
    elif op_menu == '3':
        print("----------- Ver Listado de Compradores ----------")
        print ('Rut')
        for j in range(0,total):
            print(f'Comprador {j+1}:\t{rut_array[j]}')
            rut_array.sort()
        sis.system('pause')
        
    elif op_menu == '4':
        sis.system("cls")
        print("         ----------- Mostar Ganancias Totales ----------")
        print(f'''
        Tipo de departamento                 Cantidad\t\tTotal
        Tipo A $3.800 UF                       {tipo_a}\t\t{precio_tipo_a}
        Tipo B $3000 UF                        {tipo_b}\t\t{precio_tipo_b}
        Tipo C $2.800                          {tipo_c}\t\t{precio_tipo_c}
        Tipo D $3.500 UF                       {tipo_d}\t\t{precio_tipo_d}
        TOTAL                                  {total}\t\t{total_ganancias}
        ''')
        sis.system('pause')
    elif op_menu == '5':
        print("----------- Salir ----------")
        break
        
