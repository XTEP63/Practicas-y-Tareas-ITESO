n = 4
lista = [] 
for i in range(4):
    numeros = int(input())
    lista.append(numeros)
lista.sort()

for i in lista:
    print(i)