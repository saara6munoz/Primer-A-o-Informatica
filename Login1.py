
def Menu():
    print("\n\n\n")
    print("                   |*** SELECCIONE TIPO DE CUENTA ***|\n")
    print("                        [ 1 ] Cuenta Corriente")
    print("                        [ 2 ] Cuenta Vista")
    print("                        [ 3 ] Salir\n\n")
    opcioncuenta =input("Ingrese Opción: ")
    if opcioncuenta == "1":
        os.system("clear")#Limpia la pantalla
        print (CuentaCorriente())
    elif opcioncuenta == "2":
        os.system("clear")#Limpia la pantalla
        print (CuentaVista())
    elif opcioncuenta == "3":
        os.system("clear")#Limpia la pantalla
        print (Salir())
    else:
        os.system("clear")#Limpia la pantalla
        print ("\n\n")
        print ("                             Error de Opción")
        print (Menu())

# SALDOS ---------------------------------------------------------------
totalrut = 0
totalcorriente = 0
totalvista = 0

op1ctarut = ""    #Opciones Cuenta
resp1ctarut = ""  #Respuesta Giro/Deposito/Transferencia
resp2ctarut = ""  #Respuesta Otra Operación
resp3ctarut = ""  #Respuesta Saldo
optranctarut = "" #Opcion de Transferencia


def CuentaCorriente():
    global totalrut, totalcorriente, totalvista
    print ("\n")
    print ("                ..............")
    print ("                | Cuenta Corriente |")
    print ("                ..............\n\n")
    print ("        [ 1 ] Giro              [ 2 ] Deposito\n")
    print ("        [ 3 ] Transferencia     [ 4 ] Saldo\n")
    print ("        [ 5 ] Menu Principal    [ 6 ] Salir\n\n")
    op1ctarut =input("            Ingrese Opcion: ")
# Giro Cuenta Rut ------------------------------------------------------
    if op1ctarut == "1":
        os.system("clear")#Limpia la pantalla
        print ("\n\n")
        print ("                ..............")
        print ("                | Cuenta corriente |\n")
        print ("                |    Giro    |")
        print ("                ..............\n")
        girorut = input("         Ingrese Monto a Girar: ")
        print ("\n")
        print ("         Esta seguro de realizar el Giro por este monto $",girorut)
        print ("\n")
        resp1ctarut =input("                s/n: ")
        if resp1ctarut == "s":
            totalrut = totalrut - girorut
            os.system("clear")#Limpia la pantalla
            print ("\n")
            print ("                ..............")
            print ("                | Cuenta corriente |")
            print ("                ..............\n\n")
            print ("                 Su transacción se ha realizado con exito\n")
            print ("                     ¿Desea realizar otra operación?\n")
            resp2ctarut =input("                s/n: ")
            if resp2ctarut == "s":
                os.system("clear")#Limpia la pantalla
                print (CuentaCorriente())
            elif resp2ctarut == "n":
                os.system("clear")#Limpia la pantalla
                print (Salir())
            else:
                os.system("clear")#Limpia la pantalla
                print ("\n\n")
                print ("                             Error de Opción")
                print (Menu())
        elif resp1ctarut == "n":
            os.system("clear")#Limpia la pantalla
            print (CuentaCorriente())
        else:
            os.system("clear")#Limpia la pantalla
            print ("\n\n")
            print ("                             Error de Opción")
            print (Menu())
# Deposito Cuenta Rut --------------------------------------------------
    elif op1ctarut == "2":
        os.system("clear")#Limpia la pantalla
        print ("\n\n")
        print ("                ..............")
        print ("                | Cuenta corriente |\n")
        print ("                |  Deposito  |")
        print ("                ..............\n")
        deporut = input("         Ingrese Monto a Depositar: ")
        print ("\n")
        print ("         Esta seguro de realizar el Deposito por este monto $",deporut)
        print ("\n")
        resp1ctarut = input("                s/n: ")
        if resp1ctarut == "s":
            totalrut = totalrut + deporut
            os.system("clear")#Limpia la pantalla
            print ("\n")
            print ("                ..............")
            print ("                | Cuenta corriente |")
            print ("                ..............\n\n")
            print ("                 Su transacción se ha realizado con exito\n")
            print ("                     ¿Desea realizar otra operación?\n")
            resp2ctarut =input("                s/n: ")
            if resp2ctarut == "s":
                os.system("clear")#Limpia la pantalla
                print (CuentaCorriente())
            elif resp2ctarut == "n":
                os.system("clear")#Limpia la pantalla
                print (Salir())
            else:
                os.system("clear")#Limpia la pantalla
                print("\n\n")
                print("                             Error de Opción")
                print(Menu())
        elif resp1ctarut == "n":
                os.system("clear")#Limpia la pantalla
                print (CuentaCorriente())
        else:
            os.system("clear")#Limpia la pantalla
            print("\n\n")
            print("                             Error de Opción")
            print(Menu())
# Tranferencia Cuenta Rut ----------------------------------------------
    if op1ctarut == "3":
        os.system("clear")#Limpia la pantalla
        print ("\n\n")
        print ("                          .................")
        print ("                          |   Cuenta corriente  |\n")
        print ("                          | Transferencia |")
        print ("                          .................\n")
        tranrut = int(input("         Ingrese Monto a Transferir: "))
        print("\n")
        print("                   ¿A que cuenta desea transferir?\n")
        print("             [ 1 ] Cuenta Corriente     [ 2 ] Cuenta Vista\n")
        optranctarut =input("             Ingrese Opción: ")
        print ("\n")
        print ("         Esta seguro de realizar la Transferencia por este monto $",tranrut)
        print ("\n")
        resp1ctarut =input("                s/n: ")
        if resp1ctarut == "s":
            if optranctarut == "1":
                totalrut = totalrut - tranrut
                totalcorriente = totalcorriente + tranrut
                os.system("clear")#Limpia la pantalla
                print ("\n")
                print ("                ..............")
                print ("                | Cuenta corriente |")
                print ("                ..............\n\n")
                print ("                 Su transacción se ha realizado con exito\n")
                print ("                     ¿Desea realizar otra operación?\n")
                resp2ctarut =input("                s/n: ")
                if resp2ctarut == "s":
                    os.system("clear")#Limpia la pantalla
                    print (CuentaCorriente())
                elif resp2ctarut == "n":
                    os.system("clear")#Limpia la pantalla
                    print (Salir())
            elif optranctarut == "2":
                totalrut = totalrut - tranrut
                totalvista = totalvista + tranrut
                os.system("clear")#Limpia la pantalla
                print("\n")
                print("                ..............")
                print("                | Cuenta corriente |")
                print("                ..............\n\n")
                print("                 Su transacción se ha realizado con exito\n")
                print("                     ¿Desea realizar otra operación?\n")
                resp2ctarut =input("                s/n: ")
                if resp2ctarut == "s":
                    os.system("clear")#Limpia la pantalla
                    print (CuentaCorriente())
                elif resp2ctarut == "n":
                    os.system("clear")#Limpia la pantalla
                    print (Salir())
            else:
                os.system("clear")#Limpia la pantalla
                print ("\n\n")
                print ("                             Error de Opción")
                print (CuentaCorriente()   )
# Saldo Cuenta Rut -----------------------------------------------------
    elif op1ctarut == "4":
        os.system("clear")#Limpia la pantalla
        print ("\n\n")
        print ("            ..............")
        print ("            | Cuenta corriente |\n")
        print ("            |    Saldo   |")
        print ("            ..............\n")
        print ("                       Su Saldo es :",totalrut)
        print ("\n")
        resp3ctarut =input("            [ 1 ] Volver Atras [ 2 ] Salir: ")
        if resp3ctarut == "1":
            os.system("clear")#Limpia la pantalla
            print (CuentaCorriente())
        elif resp3ctarut == "2":
            os.system("clear")#Limpia la pantalla
            print (Salir())
        else:
            os.system("clear")#Limpia la pantalla
            print("\n\n")
            print("                             Error de Opción")
            print(Menu())
    elif op1ctarut == "5":
        os.system("clear")#Limpia la pantalla
        print (Menu())
    elif op1ctarut == "6":
        os.system("clear")#Limpia la pantalla
        print (Salir())
    else:
        os.system("clear")#Limpia la pantalla
        print ("\n\n")
        print ("                             Error de Opción")
        print (Menu())
        

# SALDOS ---------------------------------------------------------------
totalrut = 0
totalcorriente = 0
totalvista = 0


op1ctarut = ""    #Opciones Cuenta
resp1ctarut = ""  #Respuesta Giro/Deposito/Transferencia
resp2ctarut = ""  #Respuesta Otra Operación
resp3ctarut = ""  #Respuesta Saldo
optranctarut = "" #Opcion de Transferencia


def CuentaVista():
    global totalrut, totalcorriente, totalvista
    print ("\n")
    print ("                ..............")
    print ("                | Cuenta Vista |")
    print ("                ..............\n\n")
    print ("        [ 1 ] Giro              [ 2 ] Deposito\n")
    print ("        [ 3 ] Transferencia     [ 4 ] Saldo\n")
    print ("        [ 5 ] Menu Principal    [ 6 ] Salir\n\n")
    op1ctarut =input("            Ingrese Opcion: ")
# Giro Cuenta Rut ------------------------------------------------------
    if op1ctarut == "1":
        os.system("clear")#Limpia la pantalla
        print ("\n\n")
        print ("                ..............")
        print ("                | Cuenta Vista |\n")
        print ("                |    Giro    |")
        print ("                ..............\n")
        girorut = input("         Ingrese Monto a Girar: ")
        print ("\n")
        print ("         Esta seguro de realizar el Giro por este monto $",girorut)
        print ("\n")
        resp1ctarut =input("                s/n: ")
        if resp1ctarut == "s":
            totalrut = totalrut - girorut
            os.system("clear")#Limpia la pantalla
            print ("\n")
            print ("                ..............")
            print ("                | Cuenta Vista |")
            print ("                ..............\n\n")
            print ("                 Su transacción se ha realizado con exito\n")
            print ("                     ¿Desea realizar otra operación?\n")
            resp2ctarut = input("                s/n: ")
            if resp2ctarut == "s":
                os.system("clear")#Limpia la pantalla
                print (CuentaVista())
            elif resp2ctarut == "n":
                os.system("clear")#Limpia la pantalla
                print (Salir())
            else:
                os.system("clear")#Limpia la pantalla
                print ("\n\n")
                print ("                             Error de Opción")
                print (Menu())
        elif resp1ctarut == "n":
            os.system("clear")#Limpia la pantalla
            print (CuentaVista())
        else:
            os.system("clear")#Limpia la pantalla
            print ("\n\n")
            print ("                             Error de Opción")
            print (Menu())
# Deposito Cuenta Rut --------------------------------------------------
    elif op1ctarut == "2":
        os.system("clear")#Limpia la pantalla
        print ("\n\n")
        print ("                ..............")
        print ("                | Cuenta Vista |\n")
        print ("                |  Deposito  |")
        print ("                ..............\n")
        deporut = input("         Ingrese Monto a Depositar: ")
        print ("\n")
        print ("         Esta seguro de realizar el Deposito por este monto $",deporut)
        print ("\n")
        resp1ctarut =input("                s/n: ")
        if resp1ctarut == "s":
            totalrut = totalrut + deporut
            os.system("clear")#Limpia la pantalla
            print ("\n")
            print ("                ..............")
            print ("                | Cuenta Vista |")
            print ("                ..............\n\n")
            print ("                 Su transacción se ha realizado con exito\n")
            print ("                     ¿Desea realizar otra operación?\n")
            resp2ctarut =input("                s/n: ")
            if resp2ctarut == "s":
                os.system("clear")#Limpia la pantalla
                print (CuentaVista())
            elif resp2ctarut == "n":
                os.system("clear")#Limpia la pantalla
                print (Salir())
            else:
                os.system("clear")#Limpia la pantalla
                print("\n\n")
                print("                             Error de Opción")
                print(Menu())
        elif resp1ctarut == "n":
                os.system("clear")#Limpia la pantalla
                print (CuentaVista())
        else:
            os.system("clear")#Limpia la pantalla
            print("\n\n")
            print("                             Error de Opción")
            print(Menu())
# Tranferencia Cuenta Rut ----------------------------------------------
    if op1ctarut == "3":
        os.system("clear")#Limpia la pantalla
        print ("\n\n")
        print ("                          .................")
        print ("                          |   Cuenta vista   |\n")
        print ("                          | Transferencia |")
        print ("                          .................\n")
        tranrut = int(input("         Ingrese Monto a Transferir: "))
        print("\n")
        print("                   ¿A que cuenta desea transferir?\n")
        print("             [ 1 ] Cuenta Corriente     [ 2 ] Cuenta Vista\n")
        optranctarut =input("             Ingrese Opción: ")
        print ("\n")
        print ("         Esta seguro de realizar la Transferencia por este monto $",tranrut)
        print ("\n")
        resp1ctarut =input("                s/n: ")
        if resp1ctarut == "s":
            if optranctarut == "1":
                totalrut = totalrut - tranrut
                totalcorriente = totalcorriente + tranrut
                os.system("clear")#Limpia la pantalla
                print ("\n")
                print ("                ..............")
                print ("                | Cuenta Rut |")
                print ("                ..............\n\n")
                print ("                 Su transacción se ha realizado con exito\n")
                print ("                     ¿Desea realizar otra operación?\n")
                resp2ctarut =input("                s/n: ")
                if resp2ctarut == "s":
                    os.system("clear")#Limpia la pantalla
                    print (CuentaVista())
                elif resp2ctarut == "n":
                    os.system("clear")#Limpia la pantalla
                    print (Salir())
            elif optranctarut == "2":
                totalrut = totalrut - tranrut
                totalvista = totalvista + tranrut
                os.system("clear")#Limpia la pantalla
                print("\n")
                print("                ..............")
                print("                | Cuenta Rut |")
                print("                ..............\n\n")
                print("                 Su transacción se ha realizado con exito\n")
                print("                     ¿Desea realizar otra operación?\n")
                resp2ctarut =input("                s/n: ")
                if resp2ctarut == "s":
                    os.system("clear")#Limpia la pantalla
                    print (CuentaVista())
                elif resp2ctarut == "n":
                    os.system("clear")#Limpia la pantalla
                    print (Salir())
            else:
                os.system("clear")#Limpia la pantalla
                print ("\n\n")
                print ("                             Error de Opción")
                print (CuentaVista()   )
# Saldo Cuenta Rut -----------------------------------------------------
    elif op1ctarut == "4":
        os.system("clear")#Limpia la pantalla
        print ("\n\n")
        print ("            ..............")
        print ("            | Cuenta Vista |\n")
        print ("            |    Saldo   |")
        print ("            ..............\n")
        print ("                       Su Saldo es :",totalrut)
        print ("\n")
        resp3ctarut =input("            [ 1 ] Volver Atras [ 2 ] Salir: ")
        if resp3ctarut == "1":
            os.system("clear")#Limpia la pantalla
            print (CuentaVista())
        elif resp3ctarut == "2":
            os.system("clear")#Limpia la pantalla
            print (Salir())
        else:
            os.system("clear")#Limpia la pantalla
            print("\n\n")
            print("                             Error de Opción")
            print(Menu())
    elif op1ctarut == "5":
        os.system("clear")#Limpia la pantalla
        print (Menu())
    elif op1ctarut == "6":
        os.system("clear")#Limpia la pantalla
        print (Salir())
    else:
        os.system("clear")#Limpia la pantalla
        print ("\n\n")
        print ("                             Error de Opción")
        print (Menu())
        
respsalir = ""
respsalir2 = ""
def Salir():
    print ("\n\n\n")
    respsalir = input("                Si desea Salir seleccione opcion (s/n): \n")
    if respsalir == "s":
        print ("                   Está seguro que desea salir (s/n)?")
        respsalir2 = input()
        if respsalir2 == "s":
            os.system("clear")#Limpia la pantalla
            print("\n\n\n")
            print("                         Su Sesión ha finalizado\n")
            print("                     Gracias por Operar Con Nosotros\n")
            print("                         CAJERO AUTOMATICO Falabella\n\n")
            time.sleep(5)
            os.system("clear")#Limpia la pantalla
            print (Login())
        elif respsalir2 == "n":
            os.system("clear")#Limpia la pantalla
            print (Menu())
        else:
            os.system("clear")#Limpia la pantalla
            print ("\n\n")
            print ("                             Error de Opción")
            print (Menu())
    elif respsalir == "n":
        os.system("clear")#Limpia la pantalla
        print (Menu())
    else:
        os.system("clear")#Limpia la pantalla
        print ("\n\n")
        print ("                             Error de Opción")
        print (Menu())        




# LOGIN USUARIO
import os
import time


def Login():
    sesion = 3
    print (time.ctime())
    print ("\n\n\n")
    print ("                         Bienvenido - Welcome\n")
    print ("                      ==========================")
    print ("                       CAJERO AUTOMATICO Falabella")
    print ("                      ==========================\n\n")
    print ("                  Ingrese su Rut sin puntos ni guión\n\n\n")
    while (sesion > 0):
        rut = input("Rut: ")
        clave =input("Clave: ")
        if (len(rut)<9) or (len(rut)>12) and (len(clave)<4) or (len(clave)>8):
            print ("                        --------------------------")
            print ("                        |*** Ingreso Incorrecto ***|")
            print ("                        --------------------------\n")  
        else:
            print ("                        --------------------------")
            print ("                        |*** Ingreso Correcto ***|")
            print ("                        --------------------------\n")
            print(Menu())  
print (Login())

        
        
