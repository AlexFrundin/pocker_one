from pygame import *

level = [
[1,0,0,0,1],
[0,1,0,1,0],
[0,0.1,0,0],
[0,1,0,1,0],
[1,0,0,0,1]
]

class Block(sprite.Sprite):

    def __init__(self,x,y):
        sprite.Sprite.__init__(self)
        self.H=20
        self.W=20
        self.X=x
        self.Y=y
        self.C="#550055"
        self.image=Surface((self.W,self.H))
        self.image.fill(Color(self.C))
        self.rect=Rect(x,y,self.W,self.H)

    def update(self, x,y):
        self.rect=Rect(x,y,self.W,self.H)

    def setPos(self):
        if (self.)



H=20
W=20
init()



display_=display.set_mode((400,400))
display.set_caption("Anime")
screen=Surface((400,400))
screen.fill(Color("#777777"))
x,y=150,150

all_object=sprite.Group()
for row in level:
    for col in row:
        if col ==1:
            bl=Block(x,y)
            all_object.add(bl)
        x+=W
    y+=H
    x=150
timer=time.Clock()
done=True
while done:
        timer.tick(60)
        for e in event.get():
            if e.type==QUIT:
                done=False
                continue
        display_.blit(screen,(0,0))
        all_object.draw(display_)

        display.update()
