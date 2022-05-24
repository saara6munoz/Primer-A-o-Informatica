#Debe de validar el correo teniendo un @ pero no lo hice （︶^︶）
respsalir = ""
respsalir2 = ""
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
         rut=int(input("Rut sin puntos ni guion: "))
         nombre=input("Nombre: ")
         direccion=input("Direccion: ")
         correo=input("Correo: ")
         comuna=(input("Comuna:"))
         edad=int(input("Edad:"))
         celular=int(input("Celular: "))
         tipo=input("Tipo = Preferencial – Habitual - Ocasional:")

         if (rut<5000000) or (rut>99999999) and (edad<18) and (len(celular)<9):
             print("-------------------------")
             print("***Ingreso Incorrecto***")
             print("-------------------------")
             break
         else:
            print("-------------------------")
            print("***Ingreso correcto***")
            print("-------------------------")
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
            print("[ 2 ] Consultar datos")
            opcionsalir=input("Eliga la opcion ")
            if opcionsalir=="1" :
                print(Menu())
                break
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
                    break
               
          
    elif opcionmenu== "2":
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
        opcionpedio= input("Ingrese las Opciones que quiera: ")
        if(opcionpedio== "1"):
            monto= c
            print("El monto total es de",monto,"\n")
            opcionpedido2=input("Desea pedir algo mas?")
            if(opcionpedido2=="2"):
                monto= c+ca
                print("El monto total es de",monto,"\n")
        elif(opcionpedio== "2"):
            monto2= ca
            print("El monto total es de",monto2,"\n")
        elif(opcionpedio== "3"):
            monto3= T
            print("El monto total es de",monto3,"\n")
        elif opcionpedio=="4" :
            print(Salir())

    elif opcionmenu=="4":
        print(Salir())
    else: 
        print("\n\n")
        print("ERROR DE OPCION")
print(Menu())
    


