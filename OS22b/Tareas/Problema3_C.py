n = int(input())
m = input()
separador = " "
lista_num = m.split(separador)
lista_num = [int(x) for x in lista_num]
num_or = list(lista_num)
num_or.sort()
con = 0
lis_index = []

for i in range(n):
    if lista_num[i] != num_or[i]:
        con += 1
        lis_index.append(i+1)

if lista_num == num_or:
    print("Ordenada")
elif con > 2:
    print("Desordenada")
else:
    print("Casi ordenada: intercambiar "+str(lis_index[0])+" y "+str(lis_index[1]))
