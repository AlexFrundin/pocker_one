import pygame
from pygame.locals import *
wall=[1]*20
wall_=[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
level=[wall,wall_,wall_,wall_,wall_,wall_,wall_,wall_,wall_,wall_,wall]

class Block(pygame.sprite.Sprite):
    def __init__ (self,x,y, H, W):
        super().__init__()

        self.H=H
        self.W=W
        self.X=x
        self.Y=y
        self.color="#000000"
        self.image=pygame.Surface((self.W, self.H))
        self.image.fill(pygame.Color(self.color))
        self.rect=pygame.Rect(self.X, self.Y, self.W, self.H)

class Hero(pygame.sprite.Sprite):
    def __init__ (self, x,y,H,W):
        super().__init__()
        self.xspeed=0
        self.yspeed=0
        self.H=H
        self.W=W
        self.X=x
        self.Y=y
        self.color="#347689"
        self.image=pygame.Surface((self.W, self.H))
        self.image.fill(pygame.Color(self.color))
        self.rect=pygame.Rect(self.X, self.Y, self.W, self.H)


    def update(self, left, right,up,down,platform,blocks_hero):
        if left:
            self.xspeed=-3
        if right:
            self.xspeed=3
        if up:
            self.yspeed=-3
        if down:
            self.yspeed=3

        if not(left or right):
            self.xspeed=0

        if not(up or down):
            self.yspeed=0

        self.rect.x+=self.xspeed
        self.collide(self.xspeed,0,platform)
        self.collide(self.xspeed,0,blocks_hero)

        self.rect.y+=self.yspeed
        self.collide(0,self.yspeed, platform)
        self.collide(0,self.yspeed, blocks_hero)


    def collide(self,xspeed,yspeed,platform):
        for p in platform:
            if pygame.sprite.collide_rect(self,p):
                if xspeed>0:
                    self.rect.right=p.rect.left
                if xspeed<0:
                    self.rect.left=p.rect.right
                if yspeed>0:
                    self.rect.bottom=p.rect.top
                if yspeed<0:
                    self.rect.top=p.rect.bottom
class Hero1(pygame.sprite.Sprite):
    def __init__ (self, x,y,H,W):
        super().__init__()
        self.xspeed=0
        self.yspeed=0
        self.H=H
        self.W=W
        self.X=x
        self.Y=y
        self.color="#347689"
        self.image=pygame.Surface((self.W, self.H))
        self.image.fill(pygame.Color(self.color))
        self.rect=pygame.Rect(self.X, self.Y, self.W, self.H)


    def update(self, left, right,up,down,platform):
        if left:
            self.xspeed=-3
        if right:
            self.xspeed=3
        if up:
            self.yspeed=-3
        if down:
            self.yspeed=3

        if not(left or right):
            self.xspeed=0

        if not(up or down):
            self.yspeed=0

        self.rect.x+=self.xspeed
        self.collide(self.xspeed,0,platform)
        #self.collide(self.xspeed,0,hero_blocks)

        self.rect.y+=self.yspeed
        self.collide(0,self.yspeed, platform)
        #self.collide(0,self.yspeed, hero_blocks)


    def collide(self,xspeed,yspeed,platform):
        for p in platform:
            if pygame.sprite.collide_rect(self,p):
                if xspeed>0:
                    self.rect.right=p.rect.left
                if xspeed<0:
                    self.rect.left=p.rect.right
                if yspeed>0:
                    self.rect.bottom=p.rect.top
                if yspeed<0:
                    self.rect.top=p.rect.bottom

pygame.init()

display_game=pygame.display.set_mode((800,600))
pygame.display.set_caption("Test")
field=pygame.Surface((800,600))
field.fill(pygame.Color('#FFFFFF'))

all_object=pygame.sprite.Group()
all_block=[]

timer=pygame.time.Clock()
done=True
x=y=0
W=40
H=40
left=right=left1=right1=False
up=down=up1=down1=False

for row in level:
    for col in row:
        if col==1:
            wall_block=Block(x,y,W,H)
            all_object.add(wall_block)
            all_block.append(wall_block)
        x+=W
    y+=H
    x=0

block_hero=Hero(120, 140, 50, 70)
block_hero2=Hero(280,280,30,20)
all_object.add(block_hero)
all_object.add(block_hero2)

# all_block.append(block_hero)
# all_block.append(block_hero2)
# hero_blocs=[]
# hero_blocs.append(block_hero)
# hero_blocs.append(block_hero2)

while done:
    timer.tick(60)
    for event in pygame.event.get():
        if event.type==QUIT or event.type==KEYDOWN and event.key == K_ESCAPE:
            done=False
            break
        if event.type ==   KEYDOWN and event.key ==K_UP:
            up=True
        if event.type ==   KEYDOWN and event.key ==K_DOWN:
            down=True
        if event.type ==   KEYDOWN and event.key ==K_LEFT:
            left=True
        if event.type ==   KEYDOWN and event.key ==K_RIGHT:
            right=True
        if event.type ==   KEYUP and event.key ==K_UP:
            up=False
        if event.type ==   KEYUP and event.key ==K_DOWN:
            down=False
        if event.type ==   KEYUP and event.key ==K_LEFT:
            left=False
        if event.type ==   KEYUP and event.key ==K_RIGHT:
            right=False

        if event.type ==   KEYDOWN and event.key ==K_w:
            up1=True
        if event.type ==   KEYDOWN and event.key ==K_s:
            down1=True
        if event.type ==   KEYDOWN and event.key ==K_a:
            left1=True
        if event.type ==   KEYDOWN and event.key ==K_d:
            right1=True
        if event.type ==   KEYUP and event.key ==K_w:
            up1=False
        if event.type ==   KEYUP and event.key ==K_s:
            down1=False
        if event.type ==   KEYUP and event.key ==K_a:
            left1=False
        if event.type ==   KEYUP and event.key ==K_d:
            right1=False

    display_game.blit(field,(0,0))
    block_hero.update(left, right,up,down,all_block,[block_hero2])
    block_hero2.update(left1,right1,up1,down1,all_block,[block_hero])
    all_object.draw(display_game)
    pygame.display.update()
