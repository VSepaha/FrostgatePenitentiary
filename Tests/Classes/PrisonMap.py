from settings import *
from ImmutableObject import *

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
			'W' : "prisonwall",
			'P' : "prisonbars",
			'B' : "bed",
			'T' : "toilet",
			'D' : "desk",
			'C' : "cabinet1",
			'O' : "door",
			'L' : "library",
			'J' : "computerdesk",
			'R' : "crate",
			'1' : "fencefront",
			'2' : "fenceside",
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

		# List that contains where the objects are located (In tiles)
		self.object_locations = {}

	def tile_has_object(self, location):
		if location in self.object_locations:
			return True
		else:
			return False

	def get_tile_at_location(self, location):
		if self.tile_has_object(location):
			return self.object_locations[location]

	def update_tiles(self, DISPLAYSURF):
		for actor in actors_group:

			# Get the tile coordinates for the four corners of the player
			topleft = (actor.rect.x/TILESIZE, actor.rect.y/TILESIZE)
			topright = ((actor.rect.x + actor.rect.width)/TILESIZE, actor.rect.y/TILESIZE)
			bottomleft = (actor.rect.x/TILESIZE, (actor.rect.y + actor.rect.height)/TILESIZE)
			bottomright = ((actor.rect.x+actor.rect.width)/TILESIZE, (actor.rect.y + actor.rect.height)/TILESIZE)

			# Reblit the map tiles
			DISPLAYSURF.blit(self.textures[self.tile_list[(topleft[1]-1)*MAPWIDTH+topleft[0]]], (topleft[0]*TILESIZE, (topleft[1]-1)*TILESIZE))
			DISPLAYSURF.blit(self.textures[self.tile_list[(topright[1]-1)*MAPWIDTH+topright[0]]], (topright[0]*TILESIZE, (topright[1]-1)*TILESIZE))

			# Re-blit the objects
			if self.tile_has_object((topleft[0], topleft[1]-1)):
				location = (topleft[0], topleft[1]-1)
				DISPLAYSURF.blit(self.get_tile_at_location(location), (location[0]*TILESIZE, location[1]*TILESIZE))
			if self.tile_has_object((topright[0], topright[1]-1)):
				location = (topright[0], topright[1]-1)
				DISPLAYSURF.blit(self.get_tile_at_location(location), (location[0]*TILESIZE, location[1]*TILESIZE))


			# Reblit the tiles that are on the actor's top left and right, and bottom left and right
			DISPLAYSURF.blit(self.textures[self.tile_list[topleft[1]*MAPWIDTH+topleft[0]]], (topleft[0]*TILESIZE, topleft[1]*TILESIZE))
			DISPLAYSURF.blit(self.textures[self.tile_list[topright[1]*MAPWIDTH+topright[0]]], (topright[0]*TILESIZE, topright[1]*TILESIZE))
			DISPLAYSURF.blit(self.textures[self.tile_list[bottomleft[1]*MAPWIDTH+bottomleft[0]]], (bottomleft[0]*TILESIZE, bottomleft[1]*TILESIZE))
			DISPLAYSURF.blit(self.textures[self.tile_list[bottomright[1]*MAPWIDTH+bottomright[0]]], (bottomright[0]*TILESIZE, bottomright[1]*TILESIZE))

			# Reblit the objects
			if self.tile_has_object((topleft[0], topleft[1])):
				location = (topleft[0], topleft[1])
				DISPLAYSURF.blit(self.get_tile_at_location(location), (location[0]*TILESIZE, location[1]*TILESIZE))
			if self.tile_has_object((topright[0], topright[1])):
				location = (topright[0], topright[1])
				DISPLAYSURF.blit(self.get_tile_at_location(location), (location[0]*TILESIZE, location[1]*TILESIZE))
			if self.tile_has_object((bottomleft[0], bottomleft[1])):
				location = (bottomleft[0], bottomleft[1])
				DISPLAYSURF.blit(self.get_tile_at_location(location), (location[0]*TILESIZE, location[1]*TILESIZE))
			if self.tile_has_object((bottomright[0], bottomright[1])):
				location = (bottomright[0], bottomright[1])
				DISPLAYSURF.blit(self.get_tile_at_location(location), (location[0]*TILESIZE, location[1]*TILESIZE))


	# Render everything onto the screen, should only be called once
	def render(self, DISPLAYSURF):
		index = 0
		for i in range (0, MAPHEIGHT):
			for j in range (0, MAPWIDTH):
				DISPLAYSURF.blit(self.textures[self.tile_list[index]],(j*TILESIZE,i*TILESIZE))
				if self.permanent_item_list[index] != ' ' and self.permanent_item_list[index] != '':
		 			imm_object = ImmutableObject(self.objects[self.permanent_item_list[index]], j*TILESIZE, i*TILESIZE, BLOCKING)
					self.object_locations[(j, i)] = imm_object.image
				index += 1
