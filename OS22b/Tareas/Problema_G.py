juegos = int(input())
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
            if k % j == 0:
                if celd[k] == "cerrado":
                    celd[k] = "abierto"
                elif celd[k] == "abierto":
                    celd[k] = "cerrado"
print(celd.count("abierto"))