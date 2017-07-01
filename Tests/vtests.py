import pygame, sys, time
from pygame.locals import *
from PrisonMap import *
from Actor import *
from Guard import *

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

# Directions
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

# Actor types used to get the image from directory
PLAYER = "player"
PRISON_GUARD = "guard"

# States that the guard can be in 
PATROL = 0 
STAND = 1
CHASE = 2

# Collision Type
BLOCKING = 0
OVERLAPPING = 1

# actors that are in game
actors = pygame.sprite.Group()

#items that are in game
items = pygame.sprite.Group()

####################### Class Definitions

class Object(pygame.sprite.Sprite):
   def __init__(self, offset_x, offset_y, collision_type):
       pygame.sprite.Sprite.__init__(self)

       # layer priority so that the player "steps over" the object
       # Unused # self.layer = 1

       self.image = pygame.image.load('../Resources/an_item.png')

       # Position of the image
       self.rect = self.image.get_rect()
       self.rect.x = offset_x
       self.rect.y = offset_y

       self.collision_type = collision_type

###################### Main code

def key_up_events(event):
	if event.key == K_w:
		player.update(False, UP)
	if event.key == K_s:
		player.update(False, DOWN)
	if event.key == K_a:
		player.update(False, LEFT)
	if event.key == K_d:
		player.update(False, RIGHT)
	if event.key == K_e:
		interactPressed = False

# Route set for the NPC
route = [
	(800, 20 + 300),
	(800-500, 20 + 300),
	(800-500, 20),
	(800, 20) 
]

# Instantiate the classes
game_map = PrisonMap()
player = Actor(200,200, PLAYER, BLOCKING)
guard = Guard(800, 20, PRISON_GUARD, BLOCKING, route)
ball = Object(400, 200, OVERLAPPING)

# add the actors to their respective groups
actors.add(player)
actors.add(guard)
items.add(ball)

# initialize the collision objects
# Only add the collisions for blocking objects
player.collision_list.append(guard)
player.collision_list.append(ball)
guard.collision_list.append(player)
guard.collision_list.append(ball)

# Used to ensure a maximum fps setting
fps_clock = pygame.time.Clock()

# Set up the window and caption
DISPLAYSURF = pygame.display.set_mode((game_map.WIDTH, game_map.HEIGHT), 0, 32)

# pressed variables
interactPressed = False

# Main game loop
while True:
	game_map.display_map(DISPLAYSURF)

	for event in pygame.event.get():
		if event.type == KEYUP:
			key_up_events(event)
		elif event.type == QUIT:
			pygame.quit()
			sys.exit()

	# The key pressed events
	key_pressed = pygame.key.get_pressed()

	if key_pressed[K_w]: 
		player.update(True, UP)
	elif key_pressed[K_s]:
		player.update(True, DOWN)
	elif key_pressed[K_a]:
		player.update(True, LEFT)
	elif key_pressed[K_d]:
		player.update(True, RIGHT)

	if key_pressed[K_e]:
		interactPressed = True

	# Guard start its patrol
	guard.run_patrol(PATROL)

	# Display every item in the game at its position
	for item in items:
		DISPLAYSURF.blit(item.image, (item.rect.x, item.rect.y))
		# if the player collides with the object and presses a key delete the object from group
		if player.rect.colliderect(item) and interactPressed:
			print "Picked up", item
			items.remove(item)

	#display all the actors in the game
	for actor in actors:
		DISPLAYSURF.blit(actor.current_image, (actor.rect.x, actor.rect.y))


	pygame.display.update()
	fps_clock.tick(FPS)
