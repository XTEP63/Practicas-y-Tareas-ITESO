lineas = [line.rstrip('\n') for line in open("G.txt")]

CARD_MAP = {
    1: lineas[0], 
    2: lineas[1], 
    3: lineas[2], 
    4: lineas[3], 
    }

#print(CARD_MAP)
print(lineas)