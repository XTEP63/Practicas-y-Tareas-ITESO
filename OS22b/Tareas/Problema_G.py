"""juegos = int(input())
separador = "-"

for i in range(juegos):
    cel_rond = input()
    lista = cel_rond.split(separador)
    lista = [int(x) for x in lista]
    celdas = lista [0]
    rondas = lista [1]
    celd = ["cerrado"] * celdas    
    for j in range(rondas):
        for k in range(celdas):
<<<<<<< HEAD
            if k % (j+1) == 0:
=======
            if k % j == 0:
>>>>>>> Tareas
                if celd[k] == "cerrado":
                    celd[k] = "abierto"
                elif celd[k] == "abierto":
                    celd[k] = "cerrado"
print(celd.count("abierto"))"""

nc = (int(input()))
lista1 = []
lista2 = []

for i in range(nc):
    lista2.append(input())
    lista1.append(lista2)

for i in range(nc):
    g = lista1[i][i].find("-")
    puertas = int(lista1[i][i][:g])
    ciclos = int(lista1[i][i][g + 1::])
    prueba = []
    pos = 1
    cas = 1
    c = 0
    for j in range(puertas):
        prueba.append(1)

    for j in range(ciclos):
        pos = j + 1
        cas = j + 1
        while pos <= puertas:
            prueba[pos - 1] *= -1
            pos += cas

    for j in range(len(prueba)):

        if prueba[j] < 0:
            c += 1
    print(c)