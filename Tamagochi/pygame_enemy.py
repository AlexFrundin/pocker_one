import pygame
from pygame_tamagochi import *
#for event your system
from pygame.locals import *
HEIGHT=23
WIDTH=12
COLOR='#777777'
class Enemy(pygame.sprite.Sprite):
    def __init__(self, name, x,y):
        pygame.sprite.Sprite.__init__(self)
        self.xspeed=0
        self.yspeed=0
        self.startX=x
        self.startY=y
        self.name=name
        self.image=pygame.Surface((WIDTH,HEIGHT))
        self.image.fill(pygame.Color(COLOR))
        self.rect=pygame.Rect(x,y,WIDTH,HEIGHT)

    def update(self, one ,platform):
        if one.rect.x<=self.rect.x:
            self.xspeed=1
        if one.rect.x>self.rect.x:
            self.xspeed=-1
        if one.rect.y<self.rect.y:
            self.yspeed=1
        if one.rect.y>=self.rect.y:
            self.yspeed=-1

        #if not(left or right):
            #self.xspeed=0

        #if not(up or down):
            #self.yspeed=0

        self.rect.x+=self.xspeed
        self.collide(self.xspeed,0,platform)

        self.rect.y+=self.yspeed
        self.collide(0,self.yspeed, platform)

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

    def __str__(self):
        return "Name={}".format(self.name)
