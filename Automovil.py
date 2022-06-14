import os as sis
import time as mimir
#---------VARIABLES GLOBALES------------
patente = ""
lista_patente=[]
marca=""
lista_marca=[]
modelo=""
lista_modelo=[]
anio=""
lista_anio=[]
tipo_auto=""
lista_tipo=[]
registros=""
lista_registro=[]

while True:
    sis.system("cls")
    op_menu=str(input(f'''
    1.- Registrar automovil            
    2.- Registro mantenimiento
    3.- Consultar automovil
    4.- Salir
    Ingrese una opción: 
            '''
        ))
    if op_menu == "1":
        sis.system("cls")
        patente=str(input("Ingrese la patente del automovil: ")).strip().upper()
        while len(patente) != 6:
            print("Error debe contener 6 caracteres como minimo")
            patente=str(input("Ingrese la patente del automovil: ")).strip()
        lista_patente.append(patente)
        
        anio=int(input("Ingrese el año del automovil: "))
        while not 1900 < anio <= 2022:
            print("Error el rango de fecha es erroneo")
            anio=int(input("Ingrese el año del automovil: "))
        lista_anio.append(anio)
        
        tipo_auto=str(input("Ingrese el tipo de automovil D/B/E/H: ")).strip()
        while not tipo_auto in ["D", "B", "E", "H", "d", "b", "e", "h"]:
            print("Error el tipo de automovil es erroneo")
            tipo_auto=str(input("Ingrese el tipo de automovil D/B/E/H: "))
        lista_tipo.append(tipo_auto)
        
        marca=str(input("Ingrese la marca del automovil: "))
        while not len(marca) > 0:
            print("Error no puede ser nula la marca")
            marca=str(input("Ingrese la marca del automovil: "))
        lista_marca.append(marca)
        
        modelo=str(input("Ingrese el modelo del automovil: "))
        while not len(modelo) > 0:
            print("Error el modelo no puede ser nulo")
            modelo=str(input("Ingrese el modelo del automovil: "))
        lista_modelo.append(modelo)
        
        confirmo= str(input("¿Desea ingresar un registro? S/N")).upper()
        if confirmo == "S":
            registros=str(input("Ingrese un registro para el automovil: "))
            while not len(registros) > 0:
                print("Error los resgistros no pueden ser nulos")
                registros=str(input("Ingrese un registro para el automovil: "))
            lista_registro.append(registros)
        else:
            lista_registro.append("No existen registros")
        sis.system("cls")
    if op_menu == "2":
        patente=str(input("Ingrese la patente del automovil: ")).strip().upper()
        while  len(patente) != 6:
            print("Error debe contener 6 caracteres como minimo")
            patente=str(input("Ingrese la patente del automovil: "))
        if patente in lista_patente:
            j = lista_patente.index(patente)
            print(f'''
                Patente: {patente}
                Año: {lista_anio[j]}
                Tipo de automovil: {lista_tipo[j]}
                Marca: {lista_marca[j]}
                Modelo {lista_modelo[j]}
                Registros: {lista_registro[j]}
                ''')
            print("------Ingrese un nuevo registro-------")
            fecha=str(input("Ingrese una fecha dd/mm/aaaa: "))
            observaciones=str(input("Ingrese una observación: "))
            obs = f'''
            fecha: {fecha}
            Registros: {observaciones}
            ------------Registros anteriores---------------
            '''+lista_registro[j]
            lista_registro.pop(j)
            lista_registro.insert(j,obs)
        else:
            print("La patente no está registrada")
        sis.system("cls")
    if op_menu == "3":
        sis.system("cls")
        patente=str(input("Ingrese la patente del automovil: ")).strip().upper()
        while len(patente) != 6:
            print("Error debe contener 6 caracteres como minimo")
            patente=str(input("Ingrese la patente del automovil: ")).strip()
        if patente in lista_patente:
            j = lista_patente.index(patente)
            print(f'''
                Patente: {patente}
                Año: {lista_anio[j]}
                Tipo de automovil: {lista_tipo[j]}
                Marca: {lista_marca[j]}
                Modelo {lista_modelo[j]}
                Registro: {lista_registro[j]}
                ''')
        sis.system("pause")        
    if op_menu == "4":
        sis.system("cls")
        seguro = str(input("¿Desea salir de la aplicacion? S/N: ")).upper()
        if seguro == 'S':
            print("Cerrando sesión...")
            mimir.sleep(2)
            break
        sis.system("pause")
        
