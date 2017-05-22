import random
score = []
for i in range(20):
    r = random.randint(1,100)
    score.append(r)
score_2=[0]*20
for i in range(len(score_2)):
    score_2[i]=random.randint(-100, -1)
print(score)
print('----------------------------------------------')
print(score_2)
summ_pos=0
summ_neg=0
for i in score:
    summ_pos+=i
summ_neg=sum(score_2)
print("score = {}".format(summ_pos))
print("score_2 = {}".format(summ_neg))
if summ_pos>abs(summ_neg):
    print("Win positive")
elif summ_pos<abs(summ_neg):
    print("Win negative")
else:
    print("==")
