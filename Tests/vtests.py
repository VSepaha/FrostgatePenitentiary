import pygame, sys, time
from pygame.locals import *

sys.path.insert(0, 'Classes') # This add the system path
from PrisonMap import *
from Actor import *
from Guard import *
from Object import *

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

# Window size
WIN_WIDTH = 1000
WIN_HEIGHT = 600

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
####################################

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
	(800, 320),
	(300, 320),
	(300, 20),
	(800, 20) 
]

# Instantiate the classes
game_map = PrisonMap()
player = Actor(500,300, PLAYER, BLOCKING)
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
DISPLAYSURF = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT), 0, 32)
pygame.display.set_caption("Frostgate Penitentiary Test") 

# how large the world map will be (Prison dimensions)
world = pygame.Surface((game_map.WIDTH, game_map.HEIGHT)) # Create Map Surface
world.fill(BLACK) # Fill Map Surface Black

# pressed variables
interactPressed = False

# Main game loop
while True:
	DISPLAYSURF.fill(BLACK)

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

	game_map.render(world)

	# Display every item in the game at its position
	for item in items:
		item.render(world)
		# if the player collides with the object and presses a key delete the object from group
		if player.rect.colliderect(item) and interactPressed:
			print "Picked up", item
			items.remove(item)

	#display all the actors in the game
	for actor in actors:
		actor.render(world)

	DISPLAYSURF.blit(world, player.camera_pos) # Render Map To The Display


	pygame.display.update()
	fps_clock.tick(FPS)
