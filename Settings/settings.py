import pygame, sys
from pygame.locals import *

pygame.init()

# FPS Setting
FPS = 30

# Used to ensure a maximum fps setting
fps_clock = pygame.time.Clock()

# Height and width of the screen
HEIGHT = 550
WIDTH = 900

#General Font
general_font = pygame.font.SysFont(None,20)

# Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW =(255,255,0)