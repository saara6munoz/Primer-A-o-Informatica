#La recursividad es una técnica muy empleada en la programación informática y consiste en que una función se llame a sí misma. 
#El ejemplo clásico es la función que calcula el factorial de un número

def sumatoria(n):
    if n == 1:
        return 1
    else:
        return n + sumatoria(n-1)
        
def sumatoria2(acum,i,n):
    if i == n:
        return acum + n
    else:
        return sumatoria2(acum + i, i+1, n)

def sumatoria3(acum,n):
    if n == 1:
        return acum + n
    else:
        return sumatoria3(acum+n, n-1)

suma1 = sumatoria(10)
suma2 = sumatoria2(0,1,10)
suma3 = sumatoria3(0,10)

print("suma1: ", suma1)
print("suma2: ", suma2)
print("suma3: ", suma3)
