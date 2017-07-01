from Object import *
from settings import *

pygame.init()

class PrisonMap:
	def __init__(self):

		# Textures on the map 
		self.textures = {
			'R' :  pygame.image.load('../Resources/Tiles/ground.png'),
			'G' :  pygame.image.load('../Resources/Tiles/grass.png'),
			'W' :  pygame.image.load('../Resources/Tiles/water.png'), 
			'D' :  pygame.image.load('../Resources/Tiles/dirt.png'),
			'P' :  pygame.image.load('../Resources/Tiles/prisonwall.png'),
			' ' :  pygame.image.load('../Resources/Tiles/base.png')
		}

		# set the display size of window
		self.WIDTH = TILESIZE * MAPWIDTH
		self.HEIGHT = TILESIZE * MAPHEIGHT

		# Create a list for the tiles
		self.tile_list = [None]*MAPHEIGHT*MAPWIDTH

		# Assign the tiles from the file to the list
		file = open('map.txt', 'r')
		for i in range (0, MAPHEIGHT*MAPWIDTH):
			return_char = file.read(1)
			if return_char == '\n':
				return_char = file.read(1)
			self.tile_list[i] = return_char
		file.close()

	def add_objects(self):
		index = 0
		for i in range (0, MAPHEIGHT):
			for j in range (0, MAPWIDTH):
				if self.tile_list[index] == PRISON_WALL:
					wall = Object("prisonwall", j*TILESIZE, i*TILESIZE, BLOCKING)
				index += 1


	def render(self, DISPLAYSURF):
		index = 0
		for i in range (0, MAPHEIGHT):
			for j in range (0, MAPWIDTH):
				DISPLAYSURF.blit(self.textures[self.tile_list[index]],(j*TILESIZE,i*TILESIZE))
				index += 1