from random import randint

lineas = [line.rstrip('\n') for line in open("Proyecto/Cards_Face.txt")]

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

def get_hand_value(cards):
    
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
    
def show_hand(name, cards):
    faces = [CARD_MAP[card] for card in cards]
    val = get_hand_value(cards)

    if val == 21:
        note = "BLACK JACK! ^w^"
    elif val > 21:
        note = "PERDISTE -_-"
    else:
        note = ""

    print (name,"Hand:" ,faces,"Total:" ,val, note)    
    
list_yes = ["si","Si","si","sI"]
list_no = ["no","No","NO","nO"]
list_players = ["Dealear"]
roud =True

while roud == True:
    Players = int(input("Cuantos jugadores van a jugar: "))

    for i in range(Players):
        list_players.append("Player" + str(i + 1))

    for name in list_players:
        cards = (deal(), deal(), deal())
        show_hand(name, cards)
        
    roud = input("Quieres jugar otras ronda ?: ")
    
    if roud in list_yes:
        roud = True
    elif roud in list_no:
        roud = False




