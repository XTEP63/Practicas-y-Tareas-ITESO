from random import randint


lineas = [line.rstrip('\n') for line in open("Gis/G.txt")]
lI = [line.rstrip('\n') for line in open("Gis/Res.txt")]


PREGUNTAS_QUIMICA = {
    1: lineas[0], 
    2: lineas[1], 
    3: lineas[2], 
    4: lineas[3], 
    }

RESPUESTAS_QUIMICA = {
    1: lI[0], 
    2: lI[1], 
    3: lI[2], 
    4: lI[3], 
    }

print(PREGUNTAS_QUIMICA[1])
print(RESPUESTAS_QUIMICA[1])
#print(lineas)
