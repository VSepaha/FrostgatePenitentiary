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

# Directions
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

# Move delta
DELTA_MOVE = 4

#######################

# Total movement execution in the main game loop could be made to be better
class Player(pygame.sprite.Sprite):
	def __init__(self, offset_x, offset_y):
		# Call the parent class (Sprite) constructor
		pygame.sprite.Sprite.__init__(self)

		# Set up all of the images for the player
		self.images_front = []
		self.images_front.append(pygame.image.load('../Resources/Player/player_front_0.png'))
		self.images_front.append(pygame.image.load('../Resources/Player/player_front_1.png'))
		self.images_front.append(pygame.image.load('../Resources/Player/player_front_2.png'))

		self.images_back = []
		self.images_back.append(pygame.image.load('../Resources/Player/player_back_0.png'))
		self.images_back.append(pygame.image.load('../Resources/Player/player_back_1.png'))
		self.images_back.append(pygame.image.load('../Resources/Player/player_back_2.png'))

		self.images_left = []
		self.images_left.append(pygame.image.load('../Resources/Player/player_left_0.png'))
		self.images_left.append(pygame.image.load('../Resources/Player/player_left_1.png'))
		self.images_left.append(pygame.image.load('../Resources/Player/player_left_2.png'))

		self.images_right = []
		self.images_right.append(pygame.image.load('../Resources/Player/player_right_0.png'))
		self.images_right.append(pygame.image.load('../Resources/Player/player_right_1.png'))
		self.images_right.append(pygame.image.load('../Resources/Player/player_right_2.png'))

		# Mapping the direction with the variable
		self.direction_map = {
			UP : self.images_back,
			DOWN: self.images_front,
			LEFT : self.images_left,
			RIGHT : self.images_right
		}

		self.current_image = self.images_front[0]
		self.index = 1
		self.count = 0
		self.player_move = False

		# Fetch the rectangle object that has the dimensions of the image
		# Update the position of this object by setting the values of rect.x and rect.y
		self.rect = self.current_image.get_rect()
		self.rect.x = offset_x
		self.rect.y = offset_y

	# Works Nicely
	def update(self, move, direction):
		if move == True:
			self.count += 1
			if self.count%6 == 0:
				self.index += 1
			if self.index >= len(self.direction_map[direction]):
				self.index = 1
			self.current_image = self.direction_map[direction][self.index]
  		else:
  			self.index = 0
  			self.count = 0
  			self.current_image = self.direction_map[direction][self.index]

  	def move(self, dx, dy):
  		if dx != 0:
  			self.move_single_axis(dx, 0)
  		if dy != 0:
  			self.move_single_axis(0, dy)

  	def move_single_axis(self, dx, dy):
  		# Move the rect
  		self.rect.x += dx
  		self.rect.y += dy

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

		# Create a list for the tiles
		self.tile_list = [None]*MAPHEIGHT*MAPWIDTH

		# Assign the tiles from the file to the list
		file = open('map.txt', 'r')
		for i in range (0, MAPHEIGHT*MAPWIDTH):
			return_char = file.read(1)
			if return_char == '\n' or return_char == '':
				return_char = file.read(1)
			self.tile_list[i] = return_char
		file.close()


	def display_map(self, DISPLAYSURF):
		index = 0
		for i in range (0, MAPHEIGHT):
			for j in range (0, MAPWIDTH):
				DISPLAYSURF.blit(game_map.textures[self.tile_list[index]],(j*TILESIZE,i*TILESIZE))
				index += 1


def key_down_events(event):
	# Nothing for now
	print "Key down:", event.key

def key_up_events(event):
	if event.key == K_w:
		player.update(False, UP)
	if event.key == K_s:
		player.update(False, DOWN)
	if event.key == K_a:
		player.update(False, LEFT)
	if event.key == K_d:
		player.update(False, RIGHT)

# Instantiate Map
game_map = Map()
player = Player(100,100)

# Used to ensure a maximum fps setting
fps_clock = pygame.time.Clock()

# Set up the window and caption
DISPLAYSURF = pygame.display.set_mode((game_map.WIDTH, game_map.HEIGHT), 0, 32)

# Main game loop
while True:
	game_map.display_map(DISPLAYSURF)

	for event in pygame.event.get():
		if event.type == KEYDOWN:
			key_down_events(event)
		if event.type == KEYUP:
			key_up_events(event)
		elif event.type == QUIT:
			pygame.quit()
			sys.exit()

	key_pressed = pygame.key.get_pressed()

	if key_pressed[K_w]: 
		player.update(True, UP)
		player.move(0, -DELTA_MOVE)
	elif key_pressed[K_s]:
		player.update(True, DOWN)
		player.move(0, DELTA_MOVE)
	elif key_pressed[K_a]:
		player.update(True, LEFT)
		player.move(-DELTA_MOVE, 0)
	elif key_pressed[K_d]:
		player.update(True, RIGHT)
		player.move(DELTA_MOVE, 0)



	DISPLAYSURF.blit(player.current_image, (player.rect.x, player.rect.y))

	pygame.display.update()
	fps_clock.tick(FPS)
