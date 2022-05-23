print("Se mostrara los 100 numeros de la  serie fibonnaci ")
while True: 

    n=100
    if n>2:
        break
x = [1,1]
for  i in range(n-2):
    x.append(x[-1] + x[-2])
print(x, end=",")
#AlexisGonzalez (ˉ﹃ˉ)