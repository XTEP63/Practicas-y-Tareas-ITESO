import random  
from itertools import product  
import math  

outerplay = ""
innerplay = ""

suit = ['clubs', ' spades', 'diamonds', 'hearts']
value_cards = {
    'Four': 4,
    'Two': 2,
    'Three': 3,
    'Five': 5,
    'Six': 6,
    'Seven': 7,
    'Eight': 8,
    'Nine': 9,
    'Ten': 10,
    'Jack': 10,
    'Queen': 10,
    'King': 10,
    'Ace': 11
}
face_cards = ['king', 'queen', 'jack', 'ace', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']

class CardGen():
    def __init__(self):
        self.face_cards = face_cards
        self.suit = suit
        self.deck = []
        for suite, rankie in product(self.suit, self.face_cards):
            self.deck.append((rankie, suite))

    def cardsrandom(self):
        random.shuffle(self.deck)  
        f1, s1 = self.deck.pop()
        return f1, s1
class money():
    def __init__(self, chips):
        self.chips = chips
        self.wincase = 1.5  

    def wincasecalc(self, bet):  
        if bet <= self.chips:
            self.chips = self.chips + bet * self.wincase
            print(f'You are now left with {self.chips}\n')
            print(f'You have gained an additional of {bet * self.wincase}\n')

    def loosecase(self, bet):  
        if bet <= self.chips:
            self.chips = self.chips - bet
            print(f'You are now left with {self.chips}\n')
            print(f'You lost an amount of {bet}\n')

def carddisplay(ts1, tf1):  
    print(f' {tf1} of {ts1} ')


def bettake(amount):  
    betting_amount = int(input('How much would you like to bet?\n'))
    if amount < betting_amount:
        print(f'Sorry your betting amount exceeds your balance! You currently have a balance of {amount}\n')
        bettake(amount)  
        return betting_amount
    else:
        return betting_amount


def scorecalculator(currentcard, score=0):   
    if currentcard == 'ACE':
        score1 = score + 11   
        score2 = score + 1   
        if math.fabs(21 - score1) < math.fabs(21 - score2):    
            return score1
        else:
            return score2
    else:
        score = score + value_cards.get(currentcard.capitalize(), 0)
        return score


def wincheck(playerscore, dealerscore, balance, bettin_gamount):   
    if playerscore > 21:  
        print('Player bust!\n')
        print('You have lost the game!\n')
        print(f'Your score:{playerscore}, and dealers score : {dealerscore}\n')
        balance.loosecase(bettin_gamount)
        return 'LOST'
    elif dealerscore > 21:   
        print('You have won!\n')
        print(f'Your score:{playerscore}, and dealers score : {dealerscore}\n')
        balance.wincasecalc(bettin_gamount)
        return 'WON'

    elif playerscore == 21:  
        if dealerscore ==21:  #
            print('ITS A TIE!\n')
            print(f'balance{balance.chips}\n')
            return 'TIE'
        else:
            print('Player wins!\n')  
            print('You have won the game!\n')
            print(f'Your score:{playerscore}, and dealers score : {dealerscore}\n')
            balance.wincasecalc(bettin_gamount)
            return 'WON'
    elif dealerscore == 21:  
        print('Player bust!\n')
        print('You have lost the game!\n')
        print(f'Your score:{playerscore}, and dealers score : {dealerscore}\n')
        balance.loosecase(bettin_gamount)
        return 'LOST'
    elif playerscore < 21 and 21 > dealerscore >= 17:  
        if playerscore > dealerscore:   
            print('Player wins!\n')
            print('You have won the game!\n')
            print(f'Your score:{playerscore}, and dealers score : {dealerscore}\n')
            balance.wincasecalc(bettin_gamount)
            return 'WON'
        elif dealerscore > playerscore:  
            print('Player bust!\n')
            print('You have lost the game!\n')
            print(f'Your score:{playerscore}, and dealers score : {dealerscore}\n')
            balance.loosecase(bettin_gamount)
            return 'LOST'
    


def hitorstand(turns, dscore, playercards, dealercards):   
    if turns == 'PLAYER':  
        choice = input('Would you like to hit or stand?').upper()   
        if choice == 'HIT':
            print('YOUR CARD:')
            pf, ps = playercards.cardsrandom()
            return ps, pf
        elif choice == 'STAND':
            return 0, 0

    elif turns == 'DEALER':  
        if dscore <= 17:   
            print('DEALERS CARD:')
            df, ds = dealercards.cardsrandom()
            return ds, df
        else:
            print('As per the rules dealer chooses to stand!')
            return 0, 0


def playagain(replaychoice):   
    global innerplay
    global outerplay
    if replaychoice == 'Y':
        innerplay = False
    elif replaychoice == 'N':
        outerplay = 'n'
        innerplay = False
        print('Thank you for playing have a great day!\n')
        



print('HELLO WELCOME TO BLACK JACK GAME!')
outerplay = input('Ready to play, type y for yes n for no\n').upper()  
while outerplay == 'Y':
    amount = int(input('What amount would you want in chips?\n'))  
    Balance = money(amount)  
    print('Let the game begin, dealer hits\n')
    turn = 'PLAYER'  
    pscore = 0  
    dscore = 0  
    playercards = CardGen()  
    dealercards = CardGen()  
    df1, ds1 = dealercards.cardsrandom()  
    df2, ds2 = dealercards.cardsrandom()  
    print('DEALERS CARD:\n')
    print('<card hidden>')
    carddisplay(ds2, df2)  
    dscore = scorecalculator(df2, dscore)  
    pf1, ps1 = playercards.cardsrandom()  
    pf2, ps2 = playercards.cardsrandom()

    print('YOUR CARDS:\n')
    carddisplay(ps1, pf1)  
    carddisplay(ps2, pf2)
    bettingmoney = bettake(amount)  
    pscore = scorecalculator(pf1, pscore)  
    pscore = scorecalculator(pf2, pscore)

    print('DEALERS CARDS:')
    carddisplay(ds1, df1)
    carddisplay(ds2, df2)
    dscore = scorecalculator(df1, dscore)
    
    currentstatus = wincheck(pscore, dscore, Balance, bettingmoney)
    if currentstatus == 'WON' or currentstatus == 'LOST' or currentstatus == 'TIE':
        break  
    innerplay = True
    turn = 'PLAYER'   
    while innerplay:   
        if turn == 'PLAYER':
            ps, pf = hitorstand('PLAYER', dscore, playercards, dealercards)  
            if pf == 0:
                turn = 'DEALER'  
            else:
                carddisplay(ps, pf)
                pscore = scorecalculator(pf, pscore)
                currentstatus = wincheck(pscore, dscore, Balance, bettingmoney)
                if currentstatus == 'WON' or currentstatus == 'LOST' or currentstatus == 'TIE':
                    break
                turn = 'DEALER'
        elif turn == 'DEALER':
            ds, df = hitorstand('DEALER', dscore, playercards, dealercards)
            if df == 0:
                turn = 'PLAYER'
            else:
                carddisplay(ds, df)
                dscore = scorecalculator(df, dscore)
                currentstatus = wincheck(pscore, dscore, Balance, bettingmoney)
                if currentstatus == 'WON' or currentstatus == 'LOST' or currentstatus == 'TIE':
                    break
                turn = 'PLAYER'
    replaychoice = input('Would you like to play again? Y for yes and N for no.').upper()
    playagain(replaychoice)   
rating = input('How  would you like to rate this game play out of 5?\n')
print(rating)
print('THANK YOU!\n')