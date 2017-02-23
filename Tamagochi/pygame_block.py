import pygame

BLOCK_W=20
BLOCK_H=20
BLOCK_COLOR='#343245'

class Block(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((BLOCK_W,BLOCK_H))
        self.image.fill(pygame.Color(BLOCK_COLOR))
        self.rect=pygame.Rect(x,y,BLOCK_W,BLOCK_H)
