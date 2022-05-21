
notas = []
cantidad_notas = int(input("Ingrese cantidad de notas a promediar: "))

i = 0
while i < cantidad_notas:
    nota = float(input(f"Ingrese nota nro {i + 1}: "))
    notas.append(nota)
    i = i + 1

acum = 0
i = 0
while i < cantidad_notas:
    acum = acum + notas[i]
    i = i + 1
prom = acum/cantidad_notas

print(f'''
      Notas: {notas}
      Cantidad de Notas: {cantidad_notas}
      Promedio: {prom}
''')