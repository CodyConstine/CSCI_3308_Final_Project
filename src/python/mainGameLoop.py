#!/usr/bin/env python 
# Instructions from: 
# http://habrahabr.ru/post/193888/
# 
# File:mainGameLoop.py
# DateCreated:2015/10/11/  
#
import pygame
from pygame import *
from player import *
from blocks import *
# 
gWindowsWidth = 800  
gWindowsHeight = 640  
gWindowsDisplay = (gWindowsWidth,gWindowsHeight) 
gWindowsBgColor = "#444400"
gPlatformWidth= 32 
gPlatformHeight = 32
gPlatformDisplay = (gPlatformWidth,gPlatformHeight)
gPlatformColor = "#FF6262"
def main(): 
    pygame.init ()
    screen = pygame.display.set_mode(gWindowsDisplay) 
    pygame.display.set_caption ("CSCI3308 Project Demo") 
    bg = pygame.Surface(gWindowsDisplay)
                                         
    bg.fill( pygame.Color(gWindowsBgColor) )      
    left = right = up = False
    timer = pygame.time.Clock()
    
    while  1:
        timer.tick(100)
        for e in pygame.event.get ():
            if e.type == QUIT:
                 raise SystemExit, "QUIT"
            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True 
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True
            if e.type == KEYUP and e.key == K_RIGHT:
                right = False 
            if e.type == KEYUP and e.key == K_LEFT:
                left = False
            if e.type == KEYDOWN and e.key == K_UP:
                up = True
            if e.type == KEYUP and e.key == K_UP:
                up = False
        screen.blit(bg,(0, 0))       
   
        x = y = 0
        for row in level:
            for col in row:
                if col == "-":
                    pf = Platform(x,y)
                    entities.add(pf)
                    platforms.append(pf)    
                x = gPlatformWidth + x
            y = gPlatformHeight + y
            x = 0
        hero.update(left, right, up, platforms) 
        entities.draw(screen)
        pygame.display.update ()      

level = ["-------------------------",
        "-                       -",
        "-                       -",
        "-                       -",
        "-                       -",
        "-                       -",
        "-                       -",
        "-                       -",
        "-                       -",
        "-                       -",
        "-                       -",
        "-                ---    -",
        "-           --          -",
        "-              ----     -",
        "-  ---                  -",
        "-                       -",
        "-                   --  -",
        "-              --       -",
        "-      ---              -",
        "-------------------------"]  
entities = pygame.sprite.Group()
hero = Player(55,55)
platforms = []
entities.add(hero)
if __name__ == "__main__":
    main()

