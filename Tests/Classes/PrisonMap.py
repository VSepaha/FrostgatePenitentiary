from Object import *
from settings import *

pygame.init()

class PrisonMap:
	def __init__(self):

		# Textures on the map 
		self.textures = {
			'B' :  pygame.image.load('../Resources/Tiles/ground.png'),
			'G' :  pygame.image.load('../Resources/Tiles/grass.png'),
			'W' :  pygame.image.load('../Resources/Tiles/water.png'), 
			'D' :  pygame.image.load('../Resources/Tiles/dirt.png'),
			' ' :  pygame.image.load('../Resources/Tiles/base.png')
		}

		# Permanent objects on the map
		self.objects = {
			'W' : pygame.image.load('../Resources/BasicObjects/prisonwall.png'),
			'P' : pygame.image.load('../Resources/BasicObjects/prisonbars.png'),
			'B' : pygame.image.load('../Resources/BasicObjects/bed.png'),
			'T' : pygame.image.load('../Resources/Tiles/base.png'), #toilet
			'D' : pygame.image.load('../Resources/Tiles/base.png'), #desk
			'C' : pygame.image.load('../Resources/Tiles/base.png'), #cabinet
			'O' : pygame.image.load('../Resources/Tiles/base.png'), #door
			' ' : pygame.image.load('../Resources/Tiles/base.png') #nothing

		}

		# set the display size of window
		self.WIDTH = TILESIZE * MAPWIDTH
		self.HEIGHT = TILESIZE * MAPHEIGHT

		# Create a list for the tiles
		self.tile_list = [None]*MAPHEIGHT*MAPWIDTH
		self.permanent_item_list = [None]*MAPHEIGHT*MAPWIDTH

		# Assign the tiles from the file to the list
		file = open('map.txt', 'r')
		for i in range (0, MAPHEIGHT*MAPWIDTH):
			return_char = file.read(1)
			if return_char == '\n':
				return_char = file.read(1)
			self.tile_list[i] = return_char
		file.close()

		# Assign the objects from the file to the list
		obj_file = open('objects.txt', 'r')
		for i in range (0, MAPHEIGHT*MAPWIDTH):
			return_char = obj_file.read(1)
			if return_char == '\n':
				return_char = obj_file.read(1)
			self.permanent_item_list[i] = return_char
		obj_file.close()


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

				# not working properly right now
				DISPLAYSURF.blit(self.objects[self.permanent_item_list[index]],(j*TILESIZE,i*TILESIZE))
				index += 1