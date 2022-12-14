from random import randint
import time

#TODO dicionario de cartas 
lineas = [line.rstrip('\n') for line in open("Proyecto/Cards_Face.txt")]

CARD_MAP = {}

for i in range(len(lineas)):
    CARD_MAP[i+1] = lineas[i]

#!-----------------------INCIO DE FUNCIONES---------------------------------
def dealer_win():
    print("\n")
    print("The dealer wins")
    print("Que mal parece que haz perdido -_-")
    print("Mejor suerte la proxima ")
    print("\n")
    
def player_win():
    print("\n")
    print("WOW !!!")
    print("Parece que un Jugador a ganado ^w^")
    print("\n")

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

def show_hand(name, cards):
    faces = [CARD_MAP[card] for card in cards]
    val = get_hand_value(cards)
    lis_val.append(val)
    
    if val == 21:
        note = "BLACK JACK! ^w^"
    else:
        note = ""
    print("\n")
    print (name,"Hand:",end=" ") 
    for i in faces:
        print(i, end=" ")
    print(note)
    
def Cards_n(num):
    cards = []
    for i in range(num):
        cards.append(deal())
    return cards
        
def numi():
    while True:
        
        try:
            num = int(input("Con cuantas cartas quieres jugar: "))
        except ValueError:
            print("Debes escribir un número -_-")
            continue

        if num < 2:
            print("Debe ser positivo -_-")
            continue
        else:
            break
    return num

def playeri():
    while True:
        
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
    return Players

def roud_game_begin():
    roud = input("Quieres jugar otras ronda ?: ")
    while True:
        if roud in list_yes:
            game_begin = False
            break
        elif roud in list_no:
            game_begin = True
            break
        else:
            print("Si o No, -_-")
            roud = input("Quieres jugar otras ronda ?: ")
            continue
    return game_begin

#?-------------------------presentacion------------------
def PRESENTATION():
    print("\n")
    print("Hola y bien benidino a este 21 BLACK JACK!!!")
    print("\n")
    print("Esra version del juego a sido modificada")
    print("Por lo que se te entragaran n cartas de manera automatica")
    print("Para obtener tu puntaje")
    print("\n")
    print("Presiona ENTER para comenzar ")
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
n = 30
game_begin = True
list_winers = []
lis_val = []
#* --------------------GAME--------------------------- 

while True:
    if game_begin == True:
        PRESENTATION()
    num = numi()
    Players = playeri()

    list_players_begin = ["Dealear"]
    
    for i in range(Players):
        list_players_begin.append("Player" + str(i + 1))

    for name in list_players_begin:
        cards = Cards_n(num)
        show_hand(name, cards)
    if 21 in lis_val:    
        if lis_val.index(21) == 0 :
            dealer_win()
        else:
            num_player_win = lis_val.index(21)
            player_win()
    else:
        dealer_win()
    
    game_begin = roud_game_begin()