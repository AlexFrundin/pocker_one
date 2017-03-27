import pygame
from pygame.locals import *

wall=[1]*15
wall_=[1,0,0,0,0,0,0,0,0,0,0,0,0,0,1]

level=[wall, wall_,wall_,wall_,wall_,wall_,wall_,wall_,
wall_,wall_,wall_,wall_,wall_,wall_,wall_,wall_,wall_,wall]

class Block(pygame.sprite.Sprite):
    def __init__ (self,x,y, H, W):
        super().__init__()

        self.H=H
        self.W=W
        self.X=x
        self.Y=y
        self.color="#FFFFFF"
        self.image=pygame.Surface((self.W, self.H))
        self.image.fill(pygame.Color(self.color))
        self.rect=pygame.Rect(self.X, self.Y, self.W, self.H)


pygame.init()

display_game=pygame.display.set_mode((800,600))
pygame.display.set_caption("Test")
field=pygame.Surface((800,600))
field.fill(pygame.Color('#550055'))

all_object=pygame.sprite.Group()
all_block=[]

timer=pygame.time.Clock()
done=True
x=y=0
W=40
H=40
for row in level:
    for col in row:
        if col==1:
            wall_block=Block(x,y,W,H)
            all_object.add(wall_block)
            all_block.append(wall_block)
        x+=W
    y+=H
    x=0


while done:
    timer.tick(60)
    for event in pygame.event.get():
        if event.type==QUIT:
            done=False
            continue
    display_game.blit(field,(0,0))
    all_object.draw(display_game)
    pygame.display.update()
