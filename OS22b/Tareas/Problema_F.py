cadena = input()

i = 0
posicion = 0
plasticos = 0
papel_carton = 0
vidrio = 0
metales = 0
otros = 0
caracter = 0

while i < len(cadena):
    posicion = cadena[caracter]
    if posicion == '1':
        plasticos = plasticos+1
    elif posicion == '2':
        papel_carton = papel_carton+1
    elif posicion == '3':
        vidrio = vidrio+1
    elif posicion == '4':
        metales = metales+1
    else:
        otros = otros+1
    caracter = caracter+1
    i += 1

print(plasticos, papel_carton, vidrio, metales, otros)