from pygame_tamagochi import *
import pygame

class Name(pygame.sprite.Sprite):
    def __init__(self,one,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.x=x
        self.y=y
        self.myFontName=pygame.font.SysFont("None", 40)
        self.rect=pygame.Rect(x,y,100,40)

    def update(self,one):
        self.name=one.getTime()
        self.image=(self.myFontName.render(self.name, 0, (255,255,0)))
        #self.image=self.myFontName.render(self.name, 0, (255,255,0))
        #self.image.blit(self.image,(self.x,self.y))
