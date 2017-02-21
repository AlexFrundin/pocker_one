import pygame
#for event your system
from pygame.locals import *
HEIGHT=23
WIDTH=12
COLOR='#645721'
class Tamagochi(pygame.sprite.Sprite):
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
        self.time=0

    def getTime(self):
        return str(self.time)
    def setTime(self):
        self.time+=1

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
