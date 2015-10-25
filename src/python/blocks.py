#!/usr/bin/env python
# Instructions from: 
# http://habrahabr.ru/post/193888/
# 
# File: blocks.py
# DateCreated:2015/10/11/  
#

from pygame import *
import os
gIconDir = os.path.dirname(__file__)
gPlatformWidth = 32
gPlatformHeight = 32
gPlatformDisplay = (gPlatformWidth,gPlatformHeight)
gPlatformColor = "#FF6262"

class Platform(sprite.Sprite):
    def __init__(self,x,y):
        sprite.Sprite.__init__(self)
        self.image = Surface(gPlatformDisplay)
        self.image = image.load("%s/blocks/platform.png" % gIconDir)
        self.image.set_colorkey(Color(gPlatformColor))
        self.rect = Rect(x,y,gPlatformWidth,gPlatformHeight)
class BlockDie(Platform):
    def __init__(self, x, y):
        Platform.__init__(self,x,y)
        self.image= image.load("%s/blocks/dieBlock.png"%gIconDir)
