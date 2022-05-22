#El import siempre va primero
import os
import time
#variables globales
cantidad_alumnos=0
alumnos_aprobados=0
alumnos_reprobados=0
nota_1=0
nota_2=0
nota_3=0


while True:
    def menu_principal():
        volver= str(input("Desea volver al menu principal? S/N: ")).upper()
        os.system("cls")

        if volver=="N":
            seguro = str(input("¿Esta seguro de salir?: ")).upper()
            if seguro=="S":
                print('''
                Usted marcó que si
                En unos segundos saldra de la aplicacion
                ''')
                time.sleep(5)
                quit()
    

    opcion_menu= str(input('''
    ----------MENU----------.k
    1.- Calcular promedio
    2.- Ver Resultados Estadisticas
    3.- Salir
    ------------------------
    
    Seleccione una opcion: '''))
 
    if opcion_menu=="1":
        os.system("cls")
        cantidad_alumnos= cantidad_alumnos + 1
        cantidad_notas= float(input('''
        ------------Calcular Promedio------------
        Ingrese la cantidad de notas a promediar: '''))

        notas = []
        i = 0
        while i < cantidad_notas:
            nota = float(input(f'''
        Ingrese nota nro {i + 1}: '''))
            if (nota > 70 or nota < 20):
                print('''
        Ingrese una nota válida
                ''')
            else:
                notas.append(nota)
                i = i + 1
        
        acum = 0
        i = 0
        while i < cantidad_notas:
            acum = acum + notas[i]
            i = i + 1
        prom = acum/cantidad_notas
      
        if prom >= 40.0:
            estado= "Aprobado"
            alumnos_aprobados= alumnos_aprobados + 1
            print(f'''
            ------------Calcular Promedio------------
            -Promedio: {prom}
            -Estado:{estado}
            -----------------------------------------
            ''')    
        else:
            estado= "Reprobado"
            alumnos_reprobados= alumnos_reprobados + 1
            print(f'''
            ------------Calcular Promedio------------
            -Nota 1: {nota_1}
            -Nota 2: {nota_2}
            -Nota 3: {nota_3}
            -Promedio: {prom}
            -Estado: {estado}
            -----------------------------------------
            ''')
        menu_principal()
              
    if opcion_menu=="2":
        print(f'''
        ----------Ver Resultados Estadisticas----------
        -Alumnos Atendidos: {cantidad_alumnos}
        -Alumnos Aprobados: {alumnos_aprobados}
        -Alumnos Reprobados: {alumnos_reprobados}
        -----------------------------------------------
        ''')
        menu_principal()

    if opcion_menu=="3":
        seguro= str(input("¿Esta seguro de salir?: ")).upper()
        if seguro=="S":
            print('''
            Usted marco que si
            En unos segundos saldra de la aplicacion
            ''')
            time.sleep(5)
            break