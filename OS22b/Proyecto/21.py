from random import randint
import time
"""import keyboard
"""
#TODO dicionario de cartas 
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

#!-----------------------INCIO DE FUNCIONES---------------------------------
def dealer_win():
    print("The dealer wins")
    print("Que mal parece que haz perdido -_-")
    print("Mejor suerte la proxima ")
    print("\n")
    
def player_win(num_player_win):
    print("WOW !!!")
    print("Parece que un Jugador a ganado ^w^")
    print("Player"+str(num_player_win))

def progres_bar(part,total,leght = 30):
    frac = part/total
    completed = int(frac * leght)
    mising = leght - completed
    bar = f"[{'■'*completed}{' '*mising}]{frac:.2%}"
    return bar

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
lis_val = []
def show_hand(name, cards):
    faces = [CARD_MAP[card] for card in cards]
    val = get_hand_value(cards)
    lis_val.append(val)
    
    if val == 21:
        note = "BLACK JACK! ^w^"
    else:
        note = ""
    print("\n")
    print (name,"Hand:",faces[0],faces[1],faces[2],note)    
    
#?-------------------------presentacion------------------
def PRESENTATION():
    print("\n")
    print("Hola y bien benidino a este 21 BLACK JACK!!!")
    print("\n")
    print("Esra version del juego a sido modificada")
    print("Por lo que se te entragaran 3 cartas de manera automatica")
    print("Para obtener tu puntaje")
    print("\n")
    print("Presiona ENTER para comenzar")
    while True:
        entrada = input()
        if entrada == "":
            for i in range(n + 1):
                time.sleep(0.1)
                print(progres_bar(i,n,100), end = "\r")
            break
        else:
            print("Presiona ENTER para comenzar")
            entrada = input()
    print("\n")

#!-----------------------FIN DE FUNCIONES-----------------------------------

#TODO Varibles iniciales
list_yes = ["si","Si","si","sI"]
list_no = ["no","No","NO","nO"]
rou =True
n = 30
game_begin = True
list_winers = []

#* --------------------GAME--------------------------- 

while rou == True:
    if game_begin == True:
        PRESENTATION()
    
    while True:
        m = 0
        try:
            Players = int(input("Cuantos jugadores van a jugar: "))
        except ValueError:
            print("Debes escribir un número -_-")
            continue

        if Players < 1:
            print("Debe ser positivo -_-")
            continue
        else:
            break
    
    list_players_begin = ["Dealear"]
    
    for i in range(Players):
        list_players_begin.append("Player" + str(i + 1))

    for name in list_players_begin:
        cards = (deal(), deal(),deal())
        show_hand(name, cards)
    if 21 in lis_val:    
        if lis_val.index(21) == 0 :
            dealer_win()
        else:
            num_player_win = lis_val.index(21)
            player_win(num_player_win)
    else:
        dealer_win()
        
    roud = input("Quieres jugar otras ronda ?: ")
    
    while True:
        if roud in list_yes:
            rou = True
            game_begin = False
            break
        elif roud in list_no:
            game_begin = True
            break
        else:
            print("Si o No, -_-")
            roud = input("Quieres jugar otras ronda ?: ")
            continue