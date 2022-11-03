from random import randint

lineas = [line.rstrip('\n') for line in open("Proyecto/Cards_Face.txt")]
print(lineas)


CARD_MAP = {
    1: lineas[0], 
    2: lineas[1], 
    3: lineas[2], 
    4: lineas[3], 
    5: lineas[4], 
    6: lineas[5], 
    7: lineas[6], 
    8: lineas[7], 
    9: lineas[8], 
    10: lineas[9], 
    11: lineas[10], 
    12: lineas[11],
    13: lineas[12]
    }

def deal():
    return randint(1, 13)

def _get_hand_value(cards):
    
    val = 0
    for card in cards:
        if 1 < card <= 10:
            val += card 
        elif card > 10:
            val += 10 
            
    if 1 in cards and val + 11 <= 21:
        return val + 11
    elif 1 in cards:
        return val + 1
    else:
        return val    
    
cont = 0 
cards = (deal(), deal(), deal())
val = _get_hand_value(cards)
faces = [CARD_MAP[card] for card in cards]

print(faces,val)

