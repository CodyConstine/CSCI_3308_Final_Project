#!/usr/bin/env python

from pygame import *
import pyganim
import os

gMonsterWidth = 32
gMonsterHeight = 32
gMonsterColor ="#2110FF"
gIconDir = os.path.dirname(__file__)
AnimationMonster = [('%s/monsters/fire1.png' % gIconDir),('%s/monsters/fire2.png' % gIconDir)]
class Monster(sprite.Sprite):
    def __init__(self, x, y, left, up, maxLeft, maxUp):
        sprite.Sprite.__init__(self)
        self.image = Surface((gMonsterWidth,gMonsterHeight))
        self.image.fill(Color(gMonsterColor))
        self.rect = Rect(x,y, gMonsterWidth, gMonsterHeight)
        self.image.set_colorkey(Color(gMonsterColor))
        self.startX = x
        self.startY = y
        self.maxLengthLeft = maxLeft
        self.maxLengthUp = maxUp
        self.xvel = left
        self.yvel = up
        boltAnim=[]
        for anim in AnimationMonster:
            boltAnim.append((anim, 0.3))
        self.boltAnim = pyganim.PygAnimation(boltAnim)
        self.boltAnim.play()
    def update(self, platforms):
        self.image.fill(Color(gMonsterColor))
        self.boltAnim.blit(self.image, (0,0))
        self.rect.y += self.yvel
        self.rect.x += self.xvel 
        self.collide(platforms)

        if(abs(self.startX - self.rect.x) > self.maxLengthLeft):
            self.xvel = -self.xvel
        if(abs(self.startY - self.rect.y) > self.maxLengthUp):
            self.yvel = -self.yvel

    def collide(self, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p ) and self != p:
                self.xvel = -self.xvel
                self.yvel = -self.yvel
        

