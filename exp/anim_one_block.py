import pygame

level=[[0,0,0,0,0,0,0,1,0,0,0,0,0,0],
       [1,0,0,0,0,0,0,0,0,0,0,0,0,0],
       [0,0,0,0,0,0,0,0,0,0,0,0,0,1]]

class Block(pygame.sprite.Sprite):
    def __init__ (self,x,y):
        #super().__init__(self)
        pygame.sprite.Sprite.__init__(self)
        self.H=20
        self.W=20
        self.X=x
        self.Y=y
        self.color="#555555"
        self.image=pygame.Surface((self.W, self.H))
        self.image.fill(pygame.Color(self.color))
        self.rect=pygame.Rect(self.X, self.Y, self.W, self.H)
        self.len=len(level)
        self.gen=self.setPos()
        self.name=' '.join((str(x),str(y)))

    def update(self):
        next(self.gen)

    def __str__(self):
        return self.name

    def setPos(self):
        while True:
            #self.rect.x=self.X
        #x=self.rect.x
            while self.rect.x>=0 and self.rect.x<(790):
                print("right")
                self.rect.x+=3
                yield
            while self.rect.x<=(800) and self.rect.x>5:
                print("left")
                self.rect.x-=3
                yield

    #def draw(self, screen):
        #screen.blit(self.image,(self.rect.x, self.rect.y))


size=(800,600)
W,H=20,20

pygame.init()

screen=pygame.display.set_mode(size)
pygame.display.set_caption("Block")
display_=pygame.Surface((size))
display_.fill(pygame.Color("#778877"))

x,y=350,200
all_object=pygame.sprite.Group()
bl=[]
for row in level:
    for col in row:
        if col==1:
            bl.append(Block(x,y))
            #all_object.add(bl)
        x+=W
    y+=H
    x=350
for item in bl:
    print(item)
    all_object.add(item)

timer=pygame.time.Clock()
done=True

while done:
    timer.tick(30)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done=False
            continue
    screen.blit(display_,(0,0))
    for item in all_object:
        item.update()
        #item.draw(screen)

    all_object.draw(screen)
    pygame.display.update()
