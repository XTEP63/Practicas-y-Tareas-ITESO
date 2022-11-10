from random import randint

CARD_MAP = {1: "Ace", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 
            9: "9", 10: "10", 11: "Jack", 12: "Queen", 13: "King"}

def deal():
    """Deal a card - returns a value indicating a card with the Ace
    represented by 1 and the Jack, Queen and King by 11, 12, 13
    respectively.
    """
    return randint(1, 13)

def _get_hand_value(cards):
    """Get the value of a hand based on the rules for Black Jack."""
    val = 0
    for card in cards:
        if 1 < card <= 10:
            val += card # 2 thru 10 are worth their face values
        elif card > 10:
            val += 10 # Jack, Queen and King are worth 10

    # Deal with the Ace if present.  Worth 11 if total remains 21 or lower
    # otherwise it's worth 1.
    if 1 in cards and val + 11 <= 21:
        return val + 11
    elif 1 in cards:
        return val + 1
    else:
        return val    

def show_hand(name, cards):
    """Print a message showing the contents and value of a hand."""
    faces = [CARD_MAP[card] for card in cards]
    val = _get_hand_value(cards)

    if val == 21:
        note = "BLACK JACK!"
    else:
        note = ""

    print (name, faces, val, note)


# Deal 2 cards to both the dealer and a player and show their hands
for name in ("Dealer", "Player"):
    cards = (deal(), deal())
    show_hand(name, cards)



