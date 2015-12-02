#!/usr/bin/env python 
# Instructions from: 
# http://habrahabr.ru/post/193888/
# 
# File:mainGameLoop.py
# DateCreated:2015/10/11/  
#

# imports
import pygame
import math
from pygame import *
from player import *
from blocks import *
from monsters import *


# 
gWindowsWidth = 800  
gWindowsHeight = 320  
gWindowsDisplay = (gWindowsWidth,gWindowsHeight) 
gWindowsBgColor = "#000000"
gPlatformWidth= 32 
gPlatformHeight = 32
gPlatformDisplay = (gPlatformWidth,gPlatformHeight)
gPlatformColor = "#FF6262"

class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0,0, width, height)
    def apply(self, target):
        return target.rect.move(self.state.topleft)
    def update(self, target):
        self.state = self.camera_func(self.state, target.rect) 
def camera_configure(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = gWindowsWidth/2-l, -t + gWindowsHeight/2
    l =  min (0, l)                            # Do not move on the left border
    l =  max (- (camera.width - gWindowsWidth), l)    # Do not move on the right border
    t =  max (- (camera.height - gWindowsHeight), t) # Do not move on the bottom border
    t =  min (0, t)                            # Do not move on the upper border
    return Rect(l,t,w,h)
def main(): 
    pygame.init ()
    screen = pygame.display.set_mode(gWindowsDisplay) 
    pygame.display.set_caption ("CSCI3308 Project Demo") 
    bg = pygame.Surface(gWindowsDisplay)
    bg.fill( pygame.Color(gWindowsBgColor) )      
    left = right = up = False
    timer = pygame.time.Clock()
    total_level_width = len (level [0]) * gPlatformWidth# calculates the actual width of the level 
    total_level_height = len (level) * gPlatformHeight    # height
    camera = Camera (camera_configure, total_level_width, total_level_height) 
    x = y = 0
    for row in level:
        for col in row:
            if col == "-":
                pf = Platform(x,y)
                entities.add(pf)
                platforms.append(pf)
            if col == "*":
                bd = BlockDie(x,y)
                entities.add(bd)
                platforms.append(bd)
            if col == "P":
                pr = Princess (x, y)
                entities.add (pr)
                platforms.append (pr)
                animatedEntities.add (pr)
            x = gPlatformWidth + x
        y = gPlatformHeight + y
        x = 0

        
        timer.tick(60)
        #timer
        message = 0
        pygame.font.init()
        Font = pygame.font.Font("font.ttf",32)
        frameCounter = 0
        mn = Monster (190, 200, 2, 3, 200, 15)
        entities.add(mn)
        platforms.append(mn)
        monsters.add(mn)

    while not hero.win:
        timerText = Font.render("Final project for CSCI3308.      Time:0"+ str(message)+"   Death:0"+str(hero.deathCounter
            ), 2,[200,50, 0])
        boxSize = timerText.get_rect() 
        scoreXpos = (gWindowsWidth-boxSize[2])/2
        for e in pygame.event.get ():
            if e.type == KEYDOWN and e.key == K_q:
                 raise SystemExit, "QUIT"
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
            if e.type == KEYDOWN and e.key == K_r:
                frameCounter = 0
                hero.deathCounter = 0
                hero.teleporting(100,100)
        #
        #
        monsters.update(platforms)
        if(hero.rect.y>400):
            hero.die()
        screen.blit(bg,(0, 0))       
        hero.update(left, right, up, platforms) 
        for e in entities:
            screen.blit (e.image, camera.apply (e))
        screen.blit(timerText, (0,0))
        camera.update(hero)
        pygame.display.update ()
        message = frameCounter// 60
        frameCounter = frameCounter + 1;
level = ["                                   ",
        "----------------------------------",
        "-                       ----------",
        "-                                -",
        "-            *                   -",
        "-                                -",
        "-        -      -                -",
        "-               -                -",
        "-      ----  *  -               P-",
        "----------- ----------------------"]  
entities = pygame.sprite.Group()
hero = Player(100,100)
platforms = []
entities.add(hero)
animatedEntities = pygame.sprite.Group()
monsters = pygame.sprite.Group()
if __name__ == "__main__":
    main()

