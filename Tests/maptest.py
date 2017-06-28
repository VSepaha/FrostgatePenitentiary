import pygame, sys, time
from pygame.locals import *

pygame.init()


########## Settings
# FPS 
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

# Map Values
TILESIZE = 40
MAPWIDTH = 25
MAPHEIGHT = 15

#######################


class Map:
	def __init__(self):

		# Textures on the map 
		self.textures = {
			'R' :  pygame.image.load('../Resources/ground.png'),
			'G' :  pygame.image.load('../Resources/grass.png'),
			'W' :  pygame.image.load('../Resources/water.png'), 
			'D' :  pygame.image.load('../Resources/dirt.png')
		}

		# set the display size of window
		self.WIDTH = TILESIZE * MAPWIDTH
		self.HEIGHT = TILESIZE * MAPHEIGHT

		self.tile_list = [None]*MAPHEIGHT*MAPWIDTH

		file = open('map.txt', 'r')
		for i in range (0, MAPHEIGHT*MAPWIDTH):
			return_char = file.read(1)
			if return_char == '\n' or return_char == '':
				return_char = file.read(1)
			self.tile_list[i] = return_char
		file.close()


	def createMap(self, DISPLAYSURF):
		index = 0
		for i in range (0, MAPHEIGHT):
			for j in range (0, MAPWIDTH):
				DISPLAYSURF.blit(game_map.textures[self.tile_list[index]],(j*TILESIZE,i*TILESIZE))
				index += 1

# Instantiate Map
game_map = Map()

# Used to ensure a maximum fps setting
fps_clock = pygame.time.Clock()

# Set up the window and caption
DISPLAYSURF = pygame.display.set_mode((game_map.WIDTH, game_map.HEIGHT), 0, 32)
DISPLAYSURF.fill(WHITE)


# Main game loop
while True:

	game_map.createMap(DISPLAYSURF)

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()


	pygame.display.update()
	fps_clock.tick(FPS)
