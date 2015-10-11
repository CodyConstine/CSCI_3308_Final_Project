#!/usr/bin/env python

from pygame import *
gPlayer = 0
gPlayerMoveSpeed = 7
gPlayerWidth = 22
gPlayerHeight = 32
gPlayerDisplay = (gPlayerWidth,gPlayerHeight)
gPlayerColor = "#888888"

class Player(sprite.Sprite):
    def __init__(self,x,y):
        sprite.Sprite.__init__(self)
        self.xvel = 0
        self.startX = x
        self.startY = y
        self.image = Surface((gPlayerDisplay))
        self.image.fill(Color(gPlayerColor))
        self.rect = Rect(x, y, gPlayerWidth, gPlayerHeight)
        
    def update(self, left, right):
        if left:
            self.xvel = -gPlayerMoveSpeed
        if right:
            self.xvel = gPlayerMoveSpeed
        if not (left or right):
            self.xvel = 0
        self.rect.x = self.xvel + self.rect.x
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
    
