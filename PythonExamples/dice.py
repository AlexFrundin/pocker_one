import random

def flyp():
    i=random.randint(1,6)
    return i

def flyp_player():
    total=flyp()+flyp()
    return total


score_play1=0
score_play2=0


while score_play1<36 and score_play2<36:
    player1=flyp_player()
    player2=flyp_player()
    if player1>player2:
        score_play1+=player1-player2
        print("Первый игрок выиграл в этом раунде")
    elif player2>player1:
        score_play2+=player2-player1
        print("Второй игрок выиграл в этом раунде")
    else:
        print("Ничья в этом раунде")


if score_play1>=36:
    print("Fisrt victory")
else:
    print("Second victory")
