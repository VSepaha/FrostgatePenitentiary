import pygame, sys, time
from pygame.locals import *

pygame.init()

TILESIZE = 40
MAPWIDTH = 25
MAPHEIGHT = 15


class Map:
	def __init__(self):

		# Textures on the map 
		self.textures = {
			'R' :  pygame.image.load('../Resources/ground.png'),
			'G' :  pygame.image.load('../Resources/grass.png'),
			'W' :  pygame.image.load('../Resources/water.png'), 
			'D' :  pygame.image.load('../Resources/dirt.png')
		}

# FPS Setting
FPS = 30

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

# Instantiate Map
game_map = Map()
WIDTH = TILESIZE * MAPWIDTH
HEIGHT = TILESIZE * MAPHEIGHT

# Used to ensure a maximum fps setting
fps_clock = pygame.time.Clock()

# Set up the window and caption
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
DISPLAYSURF.fill(WHITE)

for i in range (0,MAPWIDTH):
	for j in range (0,MAPHEIGHT):
		DISPLAYSURF.blit(game_map.textures[WATER],(i*TILESIZE,j*TILESIZE))


# Main game loop
while True:


	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()


	pygame.display.update()
	fps_clock.tick(FPS)
