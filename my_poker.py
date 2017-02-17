import random

def deckNew():
    rank=['2','3','4','5','6','7','8','9','10','11','12','13','14']
#heart->h diamond->d, clud->c, spade->s
    suit=['h','d','c','s']
    return [(i,j) for i in rank for j in suit]

def playdeck():
    deck=deckNew()
    random.shuffle(deck)
    return deck

#q_players- numbers of players
def handCards(q_players):
    deck=playdeck()
    players=[[(0,0) for _ in range(2)] for i in range(q_players)]
    for i in range(q_players*2):
        if i<q_players:
            players[i][0]=deck.pop()
        else:
            players[i-q_players][1]=deck.pop()
    return players


print(handCards(5))
