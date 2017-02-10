import random



class Card ():
    def __init__(self,rank,suit,image=None):
        self.__rank=rank
        self.__suit=suit
        self.__image=image

    def matches(self):
        if self.__rank == "jack":
                return int(11)
        elif self.__rank == "queen":
                return int(12)
        elif self.__rank == "king":
                return int(13)
        elif self.__rank == "ace":
                return int(14)
        else:
            return int(self.__rank)

    def __str__(self):
        return ("{}:{}".format(self.__rank, self.__suit))



def deck_new():
    ranks = [ "2", "3", "4", "5", "6", "7", "8", "9",
            "10", "jack", "queen", "king", "ace"]
        # black symbols
    suits = [chr(0x2660), chr(0x2665), chr(0x2663), chr(0x2666)]

    return [Card(i,j) for i in suits for j in ranks]

def deck_rand():
    deck=deck_new()
    random.shuffle(deck)
    return(deck)


#def result_math(a):

def result_pairs(user_card, table_card):
    pass

for item in deck_rand():
    print(item)
