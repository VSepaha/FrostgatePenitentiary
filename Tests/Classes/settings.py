import pygame, sys
from pygame.locals import *

pygame.init()

# FPS Setting
FPS = 30

# Used to ensure a maximum fps setting
fps_clock = pygame.time.Clock()

# Window size
WIN_WIDTH = 1000
WIN_HEIGHT = 600

# Map Values
TILESIZE = 40
MAPWIDTH = 25
MAPHEIGHT = 15

#General Font
general_font = pygame.font.SysFont(None,20)

# Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW =(255,255,0)

# Values for the tiles
GROUND = 'R'
GRASS = 'G'
WATER = 'W'
DIRT = 'D'
PRISON_WALL = 'P'

# Directions
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
NA = 4

# Actor types used to get the image from directory
PLAYER = "player"
PRISON_GUARD = "guard"
WARDEN = "warden"

# States that the guard can be in 
PATROL = 0 
STAND = 1
CHASE = 2

# Collision Type
BLOCKING = 0
OVERLAPPING = 1

# actors that are in game
actors_group = pygame.sprite.Group()

#objects that are in game
objects_group = pygame.sprite.Group()
