from pygame import *
#
# level=[
# [1,1,1,1,1,1,1,1,1,1],
# [1,0,0,0,0,0,0,0,1,1],
# [1,0,1,0,1,0,1,0,1,1],
# [1,1,1,1,2,2,1,1,1,1],
# [1,0,0,0,0,0,0,0,0,1],
# [2,2,0,0,0,1,1,0,0,1],
# [1,1,0,0,0,0,0,0,2,2],
# [1,0,0,0,1,1,0,0,0,1],
# [1,0,2,2,0,0,0,1,1,1],
# [2,2,2,2,2,1,1,1,2,2],
# ]
import random

row_=10
col_=10

def create_level(row,col):
    print('start')
    level_=[]
    for i in range(row):
        level_.append([])
        for j in range(col):
            level_[i].append(random.randint(0,2))
    print('end')
    return level_

class Block(sprite.Sprite):

    def __init__(self,x,y,rgb):
        sprite.Sprite.__init__(self)
        self.H=20
        self.W=20
        self.X=x
        self.Y=y
        self.C=rgb
        self.image=Surface((self.W,self.H))
        self.image.fill(Color(self.C))
        self.rect=Rect(x,y,self.W,self.H)
        self.gen=self.setPos()

    def update(self):
        next(self.gen)

    def setPos(self):
        while True:
            while (self.rect.x>=0 and self.rect.x<390):
                self.rect.x+=5
                yield
            while (self.rect.x>5 and self.rect.x<=410):
                self.rect.x-=5
                yield




H=20
W=20
init()
level = create_level(row_,col_)
print(level)


display_=display.set_mode((800,800))
display.set_caption("Anime")
screen=Surface((400,400))
screen.fill(Color("#777777"))
x,y=150,150

all_object=sprite.Group()

for row in level:
    for col in row:
        if col ==1:
            bl=Block(x,y,"#252525")
            all_object.add(bl)
        elif col ==2:
            bl=Block(x,y,"#76345A")
            all_object.add(bl)
        x+=W
    y+=H
    x=150


timer=time.Clock()
done=True
while done:
        timer.tick(20)
        for e in event.get():
            if e.type==QUIT:
                done=False
                continue
        display_.blit(screen,(0,0))
        # for item in all_object:
        #     item.update()
            #display_.blit(item.image,(item.rect.x,item.rect.y))
        all_object.draw(display_)

        display.update()
