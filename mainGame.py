import pygame, sys
from pygame.locals import *
from PrisonMap import *
from Guard import *
from Actor import *
from Object import *

sys.path.insert(0, 'Settings') # This add the system path
from settings import *

pygame.init()

# handler function for all the key up events
def key_up_events(event):

    if event.key == K_w:
        camera_pos = player.update(False, UP)
    if event.key == K_s:
        camera_pos = player.update(False, DOWN)
    if event.key == K_a:
        camera_pos = player.update(False, LEFT)
    if event.key == K_d:
        camera_pos = player.update(False, RIGHT)
    if event.key == K_e:
    	interactPressed = False


# Route assigned to the guard
route = [
	(800, 320),
	(300, 320),
	(300, 20),
	(800, 20) 
]

prison_map = PrisonMap()
player = Actor(prison_map.WIDTH/2, prison_map.HEIGHT/2, PLAYER, BLOCKING)
guard = Guard(800, 20, PRISON_GUARD, BLOCKING, route)
ball = Object(400, 400, OVERLAPPING)

# All the actors in the game should get added to this list
actors.add(player)
actors.add(guard)
items.add(ball)

# All objects will be added to the collison list
player.collision_list.append(guard)
guard.collision_list.append(player)

# Set up the window and caption
DISPLAYSURF = pygame.display.set_mode((prison_map.WIDTH, prison_map.HEIGHT), 0, 32)
pygame.display.set_caption('Prison Escape')
DISPLAYSURF.fill(WHITE)

# Initialize interact button
interactPressed = False

# Main game loop
while True:

	# Event handler
	for event in pygame.event.get():
		if event.type == KEYUP:
			key_up_events(event)
		elif event.type == QUIT:
			pygame.quit()
			sys.exit()

	# Key pressed events
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

	# Run the patrol for the guard
	guard.run_patrol(PATROL)

	# Renderings
	prison_map.render(DISPLAYSURF)

	for item in items:
		item.render(DISPLAYSURF)
		# if the player collides with the object and presses a key delete the object from group
		if player.rect.colliderect(item) and interactPressed:
			items.remove(item)

	# Render all the actors in the game
	for actor in actors:
		actor.render(DISPLAYSURF)

	pygame.display.update()
	fps_clock.tick(FPS)
