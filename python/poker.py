import random


def deck_new():
    ranks = [ "2", "3", "4", "5", "6", "7", "8", "9",
            "10", "jack", "queen", "king", "ace"]
        # black symbols
    suits = [chr(0x2660), chr(0x2665), chr(0x2663), chr(0x2666)]

    return [(i,j) for i in suits for j in ranks]

def deck_rand():
    deck=deck_new()
    random.shuffle(deck)
    return(deck)


def result_math(a):
    if a == "jack":
            return int(11)
    elif a == "queen":
            return int(12)
    elif a == "king":
            return int(13)
    elif a == "ace":
            return int(14)
    else:
        return int(a)


def result_pairs(user_card, table_card):
    results=0
    for i in range(len(user_card)-1):
        if 
