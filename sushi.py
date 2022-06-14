#Debe de validar el correo teniendo un @ pero no lo hice （︶^︶）
from genericpath import exists
import os as sis
respsalir = ""
respsalir2 = ""
#rut = 0
def Salir():
    print ("\n\n\n")
    respsalir = input("                Si desea Salir seleccione opcion (s/n): \n")
    if respsalir == "s":
        print ("                   Está seguro que desea salir (s/n)?")
        respsalir2 = input()
        if respsalir2 == "s":
           
            print("\n\n\n")
            print("                         Su Sesión ha finalizado\n")
            print("                    Gracias por preferir Sushi – Nikkey\n")
                         
             
def Menu ():
    print("\n\n\n")
    print("===Bienvenido al Menu de la app===")
    print("***Seleccione la opcion que desea***\n")
    print("[ 1 ]  Registrar cliente ")
    print("[ 2 ]  Consultar datos Cliente(Si no hay datos saldra ERROR) ") 
    print("[ 3 ]  Registro de pedido")  
    print("[ 4 ]  Salir") 

    opcionmenu= input("Ingrese la Opcion: ")
    if opcionmenu == "1":
        sesion=3
        print("\n\n\n")
        print("                                      ===========================")
        print("                                      BIENVENIDO A  Sushi-Nikkey ")
        print("                                      ===========================")

        print("Acontinuacion ingrese los datos solicitados \n\n\n")
        while (sesion >0):
            try:
                rut=int(input("Rut sin puntos ni guion: "))
                while  5000000 < rut <= 99999999:
                    print("Error el formato de rut especificado no coincide")
                    rut=int(input("Rut sin puntos ni guion: "))
                break
            except:
                print("El rut ingresado no coincide con el formato")
                
         
        nombre=input("Nombre: ")
        direccion=input("Direccion: ")
        correo=input("Correo: ")
        while not correo in ["@"]:
            print("Error el correo ingresado debe contener @")
            correo=input("Correo: ")
        comuna=(input("Comuna:"))
        edad=int(input("Edad:"))
        while not edad >= 18:
            print("Error debe ser mayor de edad")
            edad=int(input("Edad:"))
        celular=int(input("Celular: "))
        tipo=input("Tipo = Preferencial – Habitual - Ocasional:")
        print("-------------------------")
        print("***Ingreso correcto***")
        print("-------------------------")
        print("\n\n\n")
        print("===Bienvenido a la consulta de datos ===")
        print("***Los datos ingresados del usuario son..")
        print("\n\n")
        print("Rut: ",rut)
        print("Nombre: ", nombre)
        print("Dirección: ", direccion)
        print("Comuna: ", comuna)
        print("Correo: ", correo)
        print("Edad: ", edad)
        print("Celular:  ", celular)
        print("Tipo: ", tipo)
        print("\n")
        print("[ 1 ] Menu")
        print("[ 2 ] Consultar datos")
        opcionsalir=input("Eliga la opcion ")
        if opcionsalir=="1" :
            print(Menu())
            sis.system("pause")
        elif opcionsalir== "2":
            print("\n\n\n")
            print("===Bienvenido a la consulta de datos ===")
            print("***Los datos ingresados del usuario son..")
            print("\n\n")
            print("Rut ",rut)
            print("Nombre ", nombre)
            print("Direccion ", direccion)
            print("Comuna ", comuna)
            print("Correo ", correo)
            print("Edad", edad)
            print("Celular ", celular)
            print("Tipo", tipo)
            print("\n")

            print("[ 1 ] Menu")
            opcionsalir=input("Volver al menu principal: ")
            if opcionsalir=="1" :
                print(Menu())
                sis.system("pause")
               
          
    elif opcionmenu== "2":

        while True:
            try:
                rut=int(input("Rut sin puntos ni guion: "))
                while  5000000 < rut <= 99999999:
                    print("Error el formato de rut especificado no coincide")
                    rut=int(input("Rut sin puntos ni guion: "))
                break
            except:
                print("El rut ingresado no coincide con el formato")

        print("\n\n\n")
        print("===Bienvenido a la consulta de datos ===")
        print("***Los datos ingresados del usuario son..")
        print("\n\n")
        print("Rut ",rut)
        print("Nombre ", nombre)
        print("Direccion ", direccion)
        print("Comuna ", comuna)
        print("Correo ", correo)
        print("Edad", edad)
        print("Celular ", celular)
        print("Tipo", tipo)
        print("\n")

        print("[ 1 ] Menu")
        opcionsalir=input("Eliga la opcion ")
        if opcionsalir=="1" :
           print(Menu())
        
            
  
    elif opcionmenu== "3":
        c=5100
        ca=6200
        T=5800
        print("\n\n\n")
        print("===Registro de Pedido===")
        print("***Seleccione la opcion que desea***\n")
        print("\n\n\n")
        print("[ 1 ]  California $5.100 ")
        print("[ 2 ]  Crab ahumado $6.200 ") 
        print("[ 3 ]  Tempura Tuna Nikkei $5.800")  
        print("[ 4 ]  Salir") 
        opcionpedio= int(input("Ingrese las Opciones que quiera: "))
        if(opcionpedio== 1):
            monto= c
            print("El monto total es de",monto,"\n")
            opcionpedido2=str(input("Desea pedir algo mas S/N: ?")).strip().upper()
            if(opcionpedido2=="S"):
                opcionpedio = int(input("Ingrese las Opciones que quiera: "))
                if(opcionpedio==2):
                    monto=c+ca
                    print(f"Su monto actual es de: {monto} ")
                    opcionpedido2=str(input("Desea pedir algo mas S/N: ?")).strip().upper()
                    if(opcionpedido2=="S"):
                        monto=c+ca+T
                        print(f"Su monto total es: {monto}")
                        Salir()
                elif(opcionpedio==3):
                    monto=c+T
                    print(f"Su monto actual es de: {monto} ")
                    opcionpedido2=str(input("Desea pedir algo mas S/N: ?")).strip().upper()
                    if(opcionpedido2=="S"):
                        monto=c+ca+T
                        print(f"Su monto total es: {monto}")
                        Salir()
        elif(opcionpedio== 2):
            monto2= ca
            print("El monto total es de",monto2,"\n")
            opcionpedido2=str(input("Desea pedir algo mas S/N?")).strip().upper()
            if(opcionpedido2=="S"):
                opcionpedio = int(input("Ingrese las Opciones que quiera: "))
                if(opcionpedio==1):
                    monto2=ca+c
                    print(f"Su monto total actual es: {monto2} ")
                    opcionpedido2=str(input("Desea pedir algo mas S/N?")).strip().upper()
                    if(opcionpedido2=="S"):
                        monto2=ca+c+T
                        print(f"Su monto total es: {monto2}")
                        Salir()
            elif(opcionpedio==3):
                monto2=ca+T
                print(f"Su monto total actual es: {monto2} ")
                opcionpedido2=str(input("Desea pedir algo mas S/N?")).strip().upper()
                if(opcionpedido2=="S"):
                    monto2=ca+c+T
                    print(f"Su monto total es: {monto2}")
                    Salir()
                else:
                    Salir()
        elif(opcionpedio== 3):
            monto3= T
            print("El monto total es de",monto3,"\n")
            opcionpedido2=str(input("Desea pedir algo mas S/N?")).strip().upper()
            if(opcionpedido2=="S"):
                opcionpedio = int(input("Ingrese las Opciones que quiera: "))
                if(opcionpedio==1):
                    monto3=T+c
                    print(f"Su actual monto es: {monto3}")
                    opcionpedido2=str(input("Desea pedir algo mas S/N?")).strip().upper()
                    if(opcionpedido2=="S"):
                        monto3=T+c+ca
                        print(f"Su total es: {monto3} ")
                        Salir()
                elif(opcionpedio==2):
                    monto3=T+ca
                    print(f"Su actual monto es: {monto3}")
                    opcionpedido2=str(input("Desea pedir algo mas S/N?")).strip().upper()
                    if(opcionpedido2=="S"):
                        monto3=T+c+ca
                        print(f"Su total es: {monto3} ")
                        Salir()
                    else:
                        Salir()
        elif opcionpedio=="4" :
            print(Salir())

    elif opcionmenu=="4":
        print(Salir())
    else: 
        print("\n\n")
        print("ERROR DE OPCION")
print(Menu())