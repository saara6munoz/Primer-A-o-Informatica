import os
from xmlrpc.client import boolean

vprecio1=1990
vprecio2=2590
vprecio3=2890
vprecio4=5990

resultado1=vprecio1+1990
resultado2=vprecio2+2590
resultado3=vprecio3+2890
resultado4=vprecio4+5990


def ftotalizacion(pitaliano, phamburguesamericana, pcarnepollo, pgigantem):
	totalizacion=pitaliano+phamburguesamericana+pcarnepollo+pgigantem
	print("Totalización: ")
	print("=================================")
	print("Total De Combos: ",totalizacion)
	print("Total De Combos De Hamburguesa Americana: ",phamburguesamericana)
	print("Total De Combos De Italiano: ",pitaliano)
	print("Total De Combos De Mixto Carne Y Pollo: ",pcarnepollo)
	print("Total De Combos De Gigante Mixto: ",pgigantem)
	print("=================================")
	input("Pulse [ENTER] Para Continuar")

def fcombo_italiano():
	combos=int(input("Ingrese Cantidad De Combos Italiano: "))
	if combos>0:
		correofeka=(input("¿Desea Recibir Promociones? "))
		if correofeka=="SI":
			correo=(input("Ingrese Correo Del Cliente:"))
			input("Combo Ingresado Exitosamente..! Pulse [ENTER]")
			return combos
		if correofeka=="NO":
			input("Combo Ingresado Exitosamente..! Pulse [ENTER]")
			return combos
	else:
		print("El Número Ingresado Es Inválido")


def fcombo_hamburguesa():
	combos=int(input("Ingrese Cantidad De Hamburguesas Americanas: "))
	if combos>0:
		correofeka=(input("¿Desea Recibir Promociones? "))
		if correofeka=="SI":
			correo=(input("Ingrese Correo Del Cliente:"))
			input("Combo Ingresado Exitosamente..! Pulse [ENTER]")
			return combos
		if correofeka=="NO":
			input("Combo Ingresado Exitosamente..! Pulse [ENTER]")
			return combos
	else:
		print("El Número Ingresado Es Inválido")


def fcombo_mixto():
	combos=int(input("Ingrese Cantidad De Combo Mixtos: "))
	while combos <= 0:
		print("error el combo no puede ser 0")
		combos=int(input("Ingrese Cantidad De Combo Mixtos: "))
	correofeka=str(input("¿Desea Recibir Promociones? ")).strip().upper()
	if correofeka=="SI":
		correo=(input("Ingrese Correo Del Cliente:"))
		input("Combo Ingresado Exitosamente..! Pulse [ENTER]")
		return combos
	if correofeka=="NO":
		input("Combo Ingresado Exitosamente..! Pulse [ENTER]")
		return combos
	else:
		print("El Número Ingresado Es Inválido")

def fcombo_gigantem():
	combos=int(input("Ingrese Cantidad De Combos Gigantes Mixtos: "))
	if combos>0:
		correofeka=(input("¿Desea Recibir Promociones? "))
		if correofeka=="SI":
			correo=(input("Ingrese Correo Del Cliente:"))
			input("Combo Ingresado Exitosamente..! Pulse [ENTER]")
			return combos
		if correofeka=="NO":
			input("Combo Ingresado Exitosamente..! Pulse [ENTER]")
			return combos
	else:
		print("El Número Ingresado Es Inválido")


vcombo_italiano=0
vcombo_hamburguesa=0
vcombo_mixto=0
vcombo_gigantem=0
vcontinuar=True
while vcontinuar:
	os.system('cls')
	print("********* MENU *********")
	print("=========================")
	print("[1]-> Combo Italiano")
	print("[2]-> Combo Hamburguesa Americana")
	print("[3]-> Combo Mixto Carne Pollo")
	print("[4]-> Combo Gigante Mixto")
	print("[5]-> Totaización Y Cierres De Caja")
	print("[6]-> Combo Ganador")
	print("[7]-> Salir Del Sistema")
	print("=========================")
	opcion=int(input("Elija su opción:"))
	if opcion==1:
		vcombo_italiano+=fcombo_italiano()
	if opcion==2:
		vcombo_hamburguesa+=fcombo_hamburguesa()
	if opcion==3:
		vcombo_mixto+=fcombo_mixto()
	if opcion==4:
		vcombo_gigantem+=fcombo_gigantem()
	if opcion==5:
		vtotalizacion=int(vcombo_hamburguesa+vcombo_italiano+vcombo_mixto+vcombo_gigantem)
		porctItaliano = (vcombo_italiano*100)/vtotalizacion
		porctHamburgesa = (vcombo_hamburguesa*100)/vtotalizacion
		porctMixto = (vcombo_mixto*100)/vtotalizacion
		porctGiganteMixto = (vcombo_gigantem*100)/vtotalizacion

		totalPrecioItaliano = vcombo_italiano * vprecio1
		totalPrecioHamburguesa = vcombo_hamburguesa * vprecio2
		totalPrecioMixto = vcombo_mixto * vprecio3
		totalPrecioMixtoGi = vcombo_gigantem * vprecio4

		if vtotalizacion>0:
			print("      RESULTADOS     ")
			print("=====================")
			print("Total De Combos: ",vcombo_italiano+vcombo_hamburguesa+vcombo_mixto+vcombo_gigantem)
			print("Total De Ingresos: ",totalPrecioItaliano+totalPrecioHamburguesa+totalPrecioMixto+totalPrecioMixtoGi)
			print("=====================")
			print("Cantidad Combo Italiano: ",vcombo_italiano)
			print("Monto total por Combo Italiano: ",totalPrecioItaliano)
			print("Cantidad Combo Hamburguesa: ",vcombo_hamburguesa)
			print("Monto total por Combo Hamburguesa: ",totalPrecioHamburguesa)
			print("Cantidad Combo Mixto: ",vcombo_mixto)
			print("Monto total por Combo Mixto: ",totalPrecioMixto)
			print("Cantidad Combo Gigante Mixto: ",vcombo_gigantem)
			print("Monto total por Combo Gigante Mixto: ",totalPrecioMixtoGi)
			print("=====================")
			print("[%]Representa Combo Italiano:", porctItaliano) 
			print("[%]Representa Combo Hamburguesa:", porctHamburgesa) 
			print("[%]Representa Combo Mixto:", porctMixto) 
			print("[%]Representa Combo Gigante Mixto:", porctGiganteMixto) 
			print("=====================")
			input("Calculos Procesados Exitosamente Pulse [ENTER]")
		else:
			print("No hay datos que mostrar......!")
			input("[Pulse Enter] para continuar..!")
	if opcion==6:
		if(vcombo_italiano > vcombo_hamburguesa and vcombo_italiano > vcombo_mixto and vcombo_italiano > vcombo_gigantem):
			x=vcombo_italiano, "Combo italiano"
		else:
			if(vcombo_hamburguesa > vcombo_italiano and vcombo_hamburguesa > vcombo_mixto and vcombo_hamburguesa > vcombo_gigantem):
				x=vcombo_hamburguesa, "Combo Hamburguesa"
			else:
				if(vcombo_mixto > vcombo_italiano and vcombo_mixto > vcombo_hamburguesa and vcombo_mixto > vcombo_gigantem):
						x=vcombo_mixto, "Combo Mixto"
				else: x=vcombo_gigantem, "Combo gigante mixto"
		if(vcombo_italiano < vcombo_hamburguesa and vcombo_italiano < vcombo_mixto and vcombo_italiano < vcombo_gigantem):
			y=vcombo_italiano, "Combo italiano"
		else:
			if(vcombo_hamburguesa < vcombo_italiano and vcombo_hamburguesa < vcombo_mixto and vcombo_hamburguesa < vcombo_gigantem):
				y=vcombo_hamburguesa, "Combo hamburguesa"
			else:
				if(vcombo_mixto < vcombo_italiano and vcombo_mixto < vcombo_hamburguesa and vcombo_mixto < vcombo_gigantem):
					y=vcombo_mixto, "Combo mixto"
				else:
					y=vcombo_gigantem, "Combo gigante mixto"
		print("La cantidad y el combo ganador es "+str(x)+" y el combo perdedor es "+str(y))
		input("Pulse [ENTER] para continuar")

	if opcion==7:
            vcontinuar=False
print("Gracias Por Usar El TheFatherSystem ")
input("[Pulse Enter] Para Continuar..!")


