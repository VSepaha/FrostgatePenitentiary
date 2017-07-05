import pygame, sys

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
MAPWIDTH = 115
MAPHEIGHT = 100

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
TILE_GROUND = 'R'
TILE_GRASS = 'G'
TILE_WATER = 'W'
TILE_DIRT = 'D'
TILE_PRISON_WALL = 'P'
TILE_PRISONBAR = 'B'

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
KARATE_GUY = "karate"
PURPLE_BOY = "purpleboy"

# States that the guard can be in 
PATROL_STATE = 0 
STAND_STATE = 1
CHASE_STATE = 2
GUARD_STATE = 4


# Collision Type
BLOCKING = 0
OVERLAPPING = 1

# Stat values
STAMINA = 0
HEALTH = 1
RAMEN = 2

# actors that are in game
actors_group = pygame.sprite.Group()

# items that are in game
items_group = pygame.sprite.Group()

# permanent objects that are in game
p_objects_group = pygame.sprite.Group()
