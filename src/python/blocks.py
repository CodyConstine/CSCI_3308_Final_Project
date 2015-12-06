#!/usr/bin/env python
# Instructions from: 
# http://habrahabr.ru/post/193888/
# 
# File: blocks.py
# DateCreated:2015/10/11/  
#
 ## @package blocks
 #  class file for the blocks
from pygame import * 
import pyganim
import os
gIconDir = os.path.dirname(__file__)
gPlatformWidth = 32
gPlatformHeight = 32
gPlatformDisplay = (gPlatformWidth,gPlatformHeight)
gPlatformColor = "#FF6262"

## blocks that makes the platform
#
# The basic elements of the game background.
class Platform(sprite.Sprite):
    ## The constructor.
    # @param self the object pointer
    # @param x the x location
    # @param y the y location
    def __init__(self,x,y):
        sprite.Sprite.__init__(self)
        self.image = Surface(gPlatformDisplay)
        self.image = image.load("%s/blocks/platform.png" % gIconDir)
        self.image.set_colorkey(Color(gPlatformColor))
        self.rect = Rect(x,y,gPlatformWidth,gPlatformHeight)
## blocks that would kill the player
class BlockDie(Platform):
    ## The constructor.
    # @param self the object pointer
    # @param x the x location
    # @param y the y location
    def __init__(self, x, y):
        Platform.__init__(self,x,y)
        self.image= image.load("%s/blocks/dieBlock.png"%gIconDir)
## The end of the game
class Princess(Platform):
    ## The constructor.
    # @param self the object pointer
    # @param x the x location
    # @param y the y location
    def __init__(self, x, y):
        Platform.__init__(self, x,y)
        self.image = Surface(gPlatformDisplay)
        self.image = image.load("%s/blocks/princess_l.png"%gIconDir)
        
