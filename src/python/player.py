#!/usr/bin/env python
# Instructions from: 
# http://habrahabr.ru/post/193888/
# 
# File:player.py
# DateCreated:2015/10/11/  
#
from pygame import *
gPlayer = 0
gPlayerMoveSpeed = 7
gPlayerWidth = 22
gPlayerHeight = 32
gPlayerDisplay = (gPlayerWidth,gPlayerHeight)
gPlayerColor = "#888888"
gPlayerJumpPower = 8
gEnvGravity = 0.35
class Player(sprite.Sprite):
    def __init__(self,x,y):
        sprite.Sprite.__init__(self)
        self.xvel = 0
        self.yvel = 0
        self.onGround = False
        self.startX = x
        self.startY = y
        self.image = Surface((gPlayerDisplay))
        self.image.fill(Color(gPlayerColor))
        self.rect = Rect(x, y, gPlayerWidth, gPlayerHeight)
        
    def update(self, left, right, up, platforms):
        if up:
            if self.onGround:
                self.yvel = -gPlayerJumpPower
        if left:
            self.xvel = -gPlayerMoveSpeed
        if right:
            self.xvel = gPlayerMoveSpeed
        if not (left or right):
            self.xvel = 0
        if not self.onGround:
            self.yvel = self.yvel + gEnvGravity
        self.onGround = False
        self.rect.y = self.rect.y + self.yvel
        self.collide(0, self.yvel,platforms)
        self.rect.x = self.xvel + self.rect.x
        self.collide(self.xvel,0,platforms)
    def  collide (self, xvel, yvel, platforms): 
        for p in platforms:
             if sprite.collide_rect (self, p): 

                if xvel> 0:                     
                    self.rect.right = p.rect.left

                if xvel <0:                      
                    self.rect.left = p.rect.right  

                if yvel> 0:                     
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yvel = 0

                if yvel <0:                      
                    self.rect.top = p.rect.bottom
                    self.yvel = 0 
