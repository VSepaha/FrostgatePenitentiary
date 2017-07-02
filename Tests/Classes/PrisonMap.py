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

	def update_tiles(self, DISPLAYSURF):
		for actor in actors_group:

			# Get the tile coordinates for the four corners of the player
			topleft = (actor.rect.x/TILESIZE, actor.rect.y/TILESIZE)
			topright = ((actor.rect.x + actor.rect.width)/TILESIZE, actor.rect.y/TILESIZE) 
			bottomleft = (actor.rect.x/TILESIZE, (actor.rect.y + actor.rect.height)/TILESIZE)
			bottomright = ((actor.rect.x+actor.rect.width)/TILESIZE, (actor.rect.y + actor.rect.height)/TILESIZE)

			DISPLAYSURF.blit(self.textures[self.tile_list[(topleft[1]-1)*MAPWIDTH+topleft[0]]], (topleft[0]*TILESIZE, (topleft[1]-1)*TILESIZE))
			DISPLAYSURF.blit(self.textures[self.tile_list[(topright[1]-1)*MAPWIDTH+topright[0]]], (topright[0]*TILESIZE, (topright[1]-1)*TILESIZE))

			# Reblit the tiles that are on the actor's top left and right, and bottom left and right
			DISPLAYSURF.blit(self.textures[self.tile_list[topleft[1]*MAPWIDTH+topleft[0]]], (topleft[0]*TILESIZE, topleft[1]*TILESIZE))
			DISPLAYSURF.blit(self.textures[self.tile_list[topright[1]*MAPWIDTH+topright[0]]], (topright[0]*TILESIZE, topright[1]*TILESIZE))
			DISPLAYSURF.blit(self.textures[self.tile_list[bottomleft[1]*MAPWIDTH+bottomleft[0]]], (bottomleft[0]*TILESIZE, bottomleft[1]*TILESIZE))
			DISPLAYSURF.blit(self.textures[self.tile_list[bottomright[1]*MAPWIDTH+bottomright[0]]], (bottomright[0]*TILESIZE, bottomright[1]*TILESIZE))
			
			# print ""
			# print "Player Position = " , topleft
			# print "Player Position = " , topright
			# print "Player Position = " , bottomleft
			# print "Player Position = " , bottomright
			# print ""

	def render(self, DISPLAYSURF):
		index = 0
		for i in range (0, MAPHEIGHT):
			for j in range (0, MAPWIDTH):

				DISPLAYSURF.blit(self.textures[self.tile_list[index]],(j*TILESIZE,i*TILESIZE))
				index += 1