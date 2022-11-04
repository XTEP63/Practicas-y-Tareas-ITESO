from random import randint
columna = 30
fila = 16
tablero_Valores = [["-" for a in range(columna)]for x in range(fila)]
tablero_Estados = [["-" for a in range(columna)]for x in range(fila)]
minas = 99

while(minas!=0):
    n_aleatorio = randint(0,479)
    fila = n_aleatorio // 30
    columna = n_aleatorio % 30
    if (tablero_Estados[fila][columna]=="-"):
        tablero_Estados[fila][columna]="*"
        minas-=1
for a in range(len(tablero_Estados)):
    print('[%s]' % '| '.join(map(str, tablero_Valores[a])))

def GenerarMinas(tablero_Valores):
    minas = 0
    while minas < 100:
        n_aleatorio = randint(0, 479)
        fila = n_aleatorio // 30 
        columna = n_aleatorio % 30
        
        if tablero_Valores[fila][columna] != "*":
            minas += 1
            tablero_Valores[fila][columna] = "*"
    return tablero_Valores

def MostrarTablero(tablero_Valores, tablero_Estados):
    for i in range(16):
        for j in range(30):
            print(tablero_Valores[i][j], end = " ")
            print()
        
tablero_Estados = []
tablero_Valores = []

for i in range(16):
    fila = [0] * 30
    tablero_Valores.append(fila)
    fila = [0] * 30
    tablero_Estados.append(fila)

