import pygame, sys, time
import threading
from pygame.locals import *

sys.path.insert(0, 'Classes') # This add the system path
from PrisonMap import *
from Player import *
from SmartNPC import *
from Nurse import *
from Warden import *
from Item import *
from settings import *

pygame.init()

class NewThread(threading.Thread):
	def __init__(self, name):
		threading.Thread.__init__(self)
		print "start"

	def run(self, num):
		for i in range(0, 10):
			print num
			time.sleep(1)

# Taking care of all the key up events
def key_up_events(event):
	if event.key == K_w:
		player.update(False, UP)
	if event.key == K_s:
		player.update(False, DOWN)
	if event.key == K_a:
		player.update(False, LEFT)
	if event.key == K_d:
		player.update(False, RIGHT)

# This functino will load the menu
def load_menu(DISPLAYSURF):
	image = pygame.image.load("../Resources/menu_screen.jpg")
	text_image = pygame.image.load("../Resources/text_blink.jpg")
	DISPLAYSURF.blit(image, (0, 0))

	while True:
		for event in pygame.event.get():
			if event.type == KEYDOWN:
				return
			elif event.type == QUIT:
				pygame.quit()
				sys.exit()

		DISPLAYSURF.blit(text_image, (0, 400))

		pygame.display.update()
		fps_clock.tick(FPS)

if __name__ == '__main__':

	# Set up the window and caption
	DISPLAYSURF = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT), 0, 32)
	pygame.display.set_caption("Frostgate Penitentiary Test")

	load_menu(DISPLAYSURF)

	# Route set for the NPC
	route = [
		(800, 320),
		(300, 320),
		(300, 50),
		(800, 50)
	]

	# Instantiate the classes
	game_map = PrisonMap()
	# how large the world map will be (Prison dimensions)
	world = pygame.Surface((game_map.WIDTH, game_map.HEIGHT)) # Create Map Surface
	world.fill(BLACK) # Fill Map Surface Black
	# We only want to render the entire map once
	game_map.render(world)

	player = Player(400,300, PLAYER, BLOCKING, 2)
	guard = SmartNPC(100, 250, PRISON_GUARD, BLOCKING, route)
	warden = Warden(100, 100, WARDEN, BLOCKING, route)
	ball = Item("pokeball", 200, 200, OVERLAPPING)

	# initialize the collision objects
	# Only add the collisions for blocking objects
	player.collision_list.append(guard)
	player.collision_list.append(warden)
	guard.collision_list.append(player)

	for item in items_group: # add all items in collision list
		player.collision_list.append(item)
		guard.collision_list.append(item)

	for p_object in imm_objects_group:
		player.collision_list.append(p_object)
		guard.collision_list.append(p_object)

	# pressed variables
	interactPressed = False


	# Main game loop
	while True:
		DISPLAYSURF.fill(BLACK)

		for event in pygame.event.get():
			if event.type == KEYUP:
				key_up_events(event)
				if event.key == K_e:
					player.interact(False)
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
			player.interact(True)

		# Guard start running its state
		# guard.run_state(CHASE_STATE, player)

		# render the game map onto the world
		game_map.update_tiles(world)

		# Display every item in the game at its position
		for item in items_group:
			item.render(world)
			# if the player collides with the object and presses a key delete the object from group
			if player.rect.colliderect(item) and interactPressed:
				print "Picked up", item
				items_group.remove(item)

		for objects in imm_objects_group:
			objects.render(world)

		#display all the actors in the game
		for actor in actors_group:
			actor.render(world)

		# Render everything onto the display surface
		DISPLAYSURF.blit(world, player.camera_pos) # Render Map To The Display


		pygame.display.update()
		fps_clock.tick(FPS)
