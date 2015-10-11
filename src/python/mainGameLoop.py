#!/usr/bin/env python 

# Import the library pygame 
import pygame
from pygame import *
from player import *
# Declare variables 
gWindowsWidth = 800  # The width of the window being created 
gWindowsHeight = 640  # Height 
gWindowsDisplay = (gWindowsWidth,gWindowsHeight) # Group the width and height of a single variable 
gWindowsBgColor = "#444400"
gPlatformWidth= 32 
gPlatformHeight = 32
gPlatformDisplay = (gPlatformWidth,gPlatformHeight)
gPlatformColor = "#FF6262"
def main(): 
    pygame.init () # Initiation PyGame, mandatory line 
    screen = pygame.display.set_mode(gWindowsDisplay) # Create the window 
    pygame.display.set_caption ("CSCI3308 Project Demo") # write in caption
    bg = pygame.Surface(gWindowsDisplay) # Create the visible surface of the 
                                         # will be used as background 
    bg.fill( pygame.Color(gWindowsBgColor) )      # Fill the surface of a solid color
    hero = Player(55,55)
    left = right = False
    while  1: # The main program loop
        for e in pygame.event.get (): # handle the event 
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
        screen.blit(bg,(0, 0))       # each iteration All you need to redraw 
        level = ["-------------------------",
                "-                        -",
                "-                        -",
                "-                        -",
                "-                        -",
                "-                        -",
                "-                        -",
                "-                        -",
                "-                        -",
                "-                        -",
                "-                        -",
                "-                        -",
                "-                        -",
                "-                        -",
                "-                        -",
                "-                        -",
                "-                        -",
                "-                        -",
                "-                        -",
                "-------------------------"]    
        x = y = 0  # coordinates 
        for row in level: # entire r
            for col in row:
                if col == "-":
                    pf = Surface (gPlatformDisplay )
                    pf.fill (Color(gPlatformColor))
                    screen.blit (pf, (x, y))
                x = gPlatformWidth + x
            y = gPlatformHeight + y
            x = 0
        hero.update (left, right) # movement 
        hero.draw (screen) # display
        pygame.display.update ()      # update and withdrawal of all changes to the screen

if __name__ == "__main__":
    main ()
