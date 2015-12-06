#!/usr/bin/env python
# Instructions from: 
# http://habrahabr.ru/post/193888/
# 
# File:player.py
# DateCreated:2015/10/11/  
#

## @package player
#  Defined the behaviors of the player

from pygame import *
import monsters 
import pyganim
import blocks
import os 
gPlayer = 0
gPlayerMoveSpeed =5 
gPlayerWidth = 22
gPlayerHeight = 32
gPlayerDisplay = (gPlayerWidth,gPlayerHeight)
gPlayerColor = "#888888"
gPlayerJumpPower = 8
gEnvGravity = 0.35

ICON_DIR = os.path.dirname (__file__) # full path to the directory with files
ANIMATION_DELAY = 0.1
ANIMATION_RIGHT = [('%s/mario/r1.png'% ICON_DIR), 
            ('%s/mario/r2.png'% ICON_DIR), 
            ('%s/mario/r3.png'% ICON_DIR), 
            ('%s/mario/r4.png'% ICON_DIR), 
            ('%s/mario/r5.png'% ICON_DIR)] 
ANIMATION_LEFT = [('%s/mario/l1.png'% ICON_DIR), 
            ('%s/mario/l2.png'% ICON_DIR), 
            ('%s/mario/l3.png'% ICON_DIR), 
            ('%s/mario/l4.png'% ICON_DIR), 
            ('%s/mario/l5.png'% ICON_DIR)] 
ANIMATION_JUMP_LEFT = [('%s/mario/jl.png'% ICON_DIR, 0.1)] 
ANIMATION_JUMP_RIGHT = [('%s/mario/jr.png'% ICON_DIR, 0.1)] 
ANIMATION_JUMP = [('%s/mario/j.png'% ICON_DIR, 0.1)] 
ANIMATION_STAY = [('%s/mario/0.png'% ICON_DIR, 0.1)] 

## Player class 
#
#  This is the class for player, we define some variables to restrain the behaviors of our character.
class Player(sprite.Sprite):

    ## The constructor
    #  @param self The object pointer.
    #  @param x The initial x location of the character
    #  @param y The initial y location of the character
    def __init__(self,x,y):
        sprite.Sprite.__init__(self)
        ## to keep track whether the game should end
        self.win = False
        ## velocity in x direction
        self.xvel = 0
        ## velocity in y direction
        self.yvel = 0
        ## to see if the character isn't jumping
        self.onGround = False
        ## the initial x location
        self.startX = x
        ## the initial y location
        self.startY = y
        ## count the death
        self.deathCounter = 0
        ## pygame property, the player's image
        self.image = Surface((gPlayerDisplay))
        self.image.fill(Color(gPlayerColor))
        ## pygame rectangle of the player.
        self.rect = Rect(x, y, gPlayerWidth, gPlayerHeight)
        self.image.set_colorkey(Color(gPlayerColor))
        boltAnim = []
        for anim in ANIMATION_RIGHT:
            boltAnim.append ((anim, ANIMATION_DELAY))
        self.boltAnimRight = pyganim.PygAnimation (boltAnim)
        self.boltAnimRight.play ()
        boltAnim = []
        for anim in ANIMATION_LEFT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimLeft = pyganim.PygAnimation(boltAnim)
        self.boltAnimLeft.play()
        self.boltAnimStay = pyganim.PygAnimation (ANIMATION_STAY)
        self.boltAnimStay.play ()
        self.boltAnimStay.blit (self.image, (0, 0)) # By default, the stand
        
        self.boltAnimJumpLeft = pyganim.PygAnimation (ANIMATION_JUMP_LEFT)
        self.boltAnimJumpLeft.play ()
        
        self.boltAnimJumpRight = pyganim.PygAnimation (ANIMATION_JUMP_RIGHT)
        self.boltAnimJumpRight.play ()
        
        self.boltAnimJump = pyganim.PygAnimation (ANIMATION_JUMP)
        self.boltAnimJump.play ()

    ## The method to update the location of the player
    #  @param self The object pointer.
    #  @param left whether the player is moving left
    #  @param right whether the player is moving right 
    #  @param up whether the player is moving up
    #  @param platforms the game platform
    def update(self, left, right, up, platforms):
        if up:
            if self.onGround:
                self.yvel = -gPlayerJumpPower
            self.image.fill(Color(gPlayerColor))
            self.boltAnimJump.blit(self.image, (0,0))
        if left:
            self.xvel = -gPlayerMoveSpeed
            self.image.fill(Color(gPlayerColor))
            if up:
                self.boltAnimJumpLeft.blit(self.image, (0,0))
            else:
                self.boltAnimLeft.blit(self.image, (0,0))
        if right:
            self.xvel = gPlayerMoveSpeed
            self.image.fill(Color(gPlayerColor))
            if up:
                self.boltAnimJumpRight.blit(self.image, (0,0))
            else:
                self.boltAnimRight.blit(self.image, (0,0))
        if not (left or right):
            self.xvel = 0
            if not up:
                self.image.fill(Color(gPlayerColor))
                self.boltAnimStay.blit(self.image,(0,0))
        if not self.onGround:
            self.yvel = self.yvel + gEnvGravity
        self.onGround = False
        self.rect.y = self.rect.y + self.yvel
        self.collide(0, self.yvel,platforms)
        self.rect.x = self.xvel + self.rect.x
        self.collide(self.xvel,0,platforms)
    ## The method to detect whether there's a collision
    #  @param self The object pointer.
    #  @param xvel The velocity in x direction.
    #  @param yvel The velocity in y direction.
    #  @param platforms the game platform
    def  collide (self, xvel, yvel, platforms): 
        for p in platforms:
             if sprite.collide_rect(self, p): 
                if isinstance(p, blocks.BlockDie) or isinstance(p, monsters.Monster):
                    self.die()
                elif isinstance(p, blocks.Princess):
                    self.win = True
                else:
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
    ## The method to teleport the player
    #  @param self The object pointer.
    #  @param goX the x location of the destination.
    #  @param goY the Y location of the destination.
    def teleporting(self, goX, goY):
        self.rect.x = goX
        self.rect.y = goY
    ## The method to kill the player. XD
    #  @param self The object pointer.   
    def die(self):
        time.wait(500)
        self.deathCounter = self.deathCounter + 1
        self.teleporting(self.startX, self.startY) 
