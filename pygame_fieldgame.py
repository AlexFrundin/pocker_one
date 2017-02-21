from pygame_tamagochi import *
from pygame_block import *
from pygame_enemy import *
from pygame_name import *
import pygame
from pygame.locals import *
import os
import time

WIN_W=800
WIM_H=740
SCREEN=(WIN_W,WIM_H)
BACKGROUND_COLOR="#005500"

def main():
    pygame.init()
    display_game=pygame.display.set_mode(SCREEN)
    pygame.display.set_caption("Tamagochi")
    field=pygame.Surface((WIN_W,WIM_H))
    field.fill(pygame.Color(BACKGROUND_COLOR))

    one=Tamagochi("Ster",155,155)

    left=right=False
    up=down=False
    name_font=Name(one,10,10)
    two=Enemy("asd",500,400)

    all_object=pygame.sprite.Group()
    all_object.add(name_font)
    all_block=[]

    all_object.add(name_font)
    all_object.add(one)
    all_object.add(two)

    str_all="-"*40
    str_bend="-"+" "*38+"-"
    str_space=" "*40
    level=[
            str_space,
            str_space,
            str_space,
            str_all,
            str_bend,str_bend,str_bend,str_bend,str_bend,str_bend,str_bend,str_bend,str_bend,str_bend,
            str_bend,str_bend,str_bend,str_bend,str_bend,str_bend,str_bend,str_bend,str_bend,str_bend,
            str_bend,str_bend,str_bend,str_bend,str_bend,str_bend,str_bend,str_bend,str_bend,str_bend,
            str_all
    ]

    timer = pygame.time.Clock()

    x=y=0
    for row in level:
        for col in row:
            if col == '-':
                wall_block=Block(x,y)
                all_object.add(wall_block)
                all_block.append(wall_block)

            x+=BLOCK_W
        y+=BLOCK_H
        x=0

    done=True
    pause=False
    while done:
        timer.tick(60)
        for event in pygame.event.get():
            if event.type==QUIT:
                done=False
                continue
            if event.type ==   KEYDOWN and event.key ==K_UP:
                up=True

            if event.type ==   KEYDOWN and event.key ==K_DOWN:
                down=True

            if event.type ==   KEYDOWN and event.key ==K_LEFT:
                left=True

            if event.type ==   KEYDOWN and event.key ==K_RIGHT:
                right=True
            if event.type==KEYDOWN and event.key ==K_SPACE:
                    if pause:
                        pause=False
                    else:
                        pause=True
            if pause:
                time.sleep(2)
                pause=False

            if event.type ==   KEYUP and event.key ==K_UP:
                up=False
            if event.type ==   KEYUP and event.key ==K_DOWN:
                down=False
            if event.type ==   KEYUP and event.key ==K_LEFT:
                left=False
            if event.type ==   KEYUP and event.key ==K_RIGHT:
                right=False

        display_game.blit(field,(0,0))
        one.update(left, right,up,down,all_block)
        one.setTime()
        name_font.update(one)
        two.update(one,all_block)
        all_object.draw(display_game)

        #display_game.blit()

        pygame.display.update()

if __name__ =="__main__":
    main()
