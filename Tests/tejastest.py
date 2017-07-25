import pygame, sys, time, threading
from pygame.locals import *

sys.path.insert(0, 'Classes') # This add the system path
from PrisonMap import *
from Player import *
from SmartNPC import *
from Nurse import *
from Warden import *
from Item import *
from InteractableObject import *
from settings import *
from GUI import *

pygame.init()

exitFlag = 0

# This causes the blinking of the press any key
class new_thread (threading.Thread):
	def __init__(self, threadID, name, DISPLAYSURF):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.DISPLAYSURF = DISPLAYSURF
		self.name = name
		self.image = pygame.image.load("../Resources/menu_screen.jpg")
		self.text_image = pygame.image.load("../Resources/text_blink.jpg")
	def run(self):
		print "Starting " + self.name
		self.flash_text(1, self.DISPLAYSURF)
		print "Exiting " + self.name

	def flash_text(self, delay, DISPLAYSURF):
		while True:
			if exitFlag:
				break
			DISPLAYSURF.blit(self.image, (0,0))
			time.sleep(delay)
			DISPLAYSURF.blit(self.text_image, (0, 400))
			time.sleep(delay)

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

	global exitFlag
	flash = new_thread(1, "flash_thread", DISPLAYSURF)

	flash.start()

	while True:
		for event in pygame.event.get():
			if event.type == KEYDOWN:
				exitFlag = 1
				return
			elif event.type == QUIT:
				pygame.quit()
				sys.exit()

		pygame.display.update()
		fps_clock.tick(FPS)
def save_game():
		shelfFile = shelve.open('../savedGameTrial')
		shelfFile['health'] = player.health

if __name__ == '__main__':

	# Set up the window and caption
	DISPLAYSURF = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT), 0, 32)
	pygame.display.set_caption("Frostgate Penitentiary Test")

	load_menu(DISPLAYSURF)

	# For testing purposes of A*
	# For horizontal tests (420, 300)
	ball = Item("pokeball", 210, 240, OVERLAPPING)
	# Route set for the NPC
	# (14*40, 8*40),
	route = [
		(14*TILESIZE, 6*TILESIZE),
		(200, 440)
	]

	# Instantiate the classes
	game_map = PrisonMap()
	# how large the world map will be (Prison dimensions)
	world = pygame.Surface((game_map.WIDTH, game_map.HEIGHT)) # Create Map Surface
	world.fill(BLACK) # Fill Map Surface Black
	# We only want to render the entire map once
	game_map.render(world)
	for objects in imm_objects_group:
		objects.render(world)

	door_images = []
	door_images.append("door")
	door_images.append("opendoor")

	door = InteractableObject(door_images, 61*TILESIZE, 11*TILESIZE, BLOCKING, "DOOR")

	player = Player(400,400, PLAYER, BLOCKING, 2)
	gui = GUI(player)
	# player.speed = 20
	# For horizontal tests (120, 300)
	guard = SmartNPC(200, 444, PRISON_GUARD, BLOCKING, route, game_map)
	warden = Warden(100, 100, WARDEN, BLOCKING, route, game_map)
	nurse = Nurse(52*TILESIZE, 96*TILESIZE, NURSE, BLOCKING, route, game_map)

	# initialize the collision objects
	# Only add the collisions for blocking objects
	player.collision_list.append(guard)
	player.collision_list.append(warden)
	player.collision_list.append(door)
	player.collision_list.append(nurse)
	guard.collision_list.append(player)

	for item in items_group: # add all items in collision list
		player.collision_list.append(item)
		guard.collision_list.append(item)

	for p_object in imm_objects_group:
		player.collision_list.append(p_object)
		guard.collision_list.append(p_object)

	inv_flag = True
	player.speed = 20
	# Main game loop
	while True:
		DISPLAYSURF.fill(BLACK)

		for event in pygame.event.get():
			if event.type == KEYUP:
				key_up_events(event)
				if event.key == K_e:
					player.interact(False)
				elif event.key == K_q:
					player.drop_item(gui.get_inv_index())
			if event.type == KEYDOWN:
				if event.key == K_e:
					player.interact(True)
				if event.key == K_o:
					save_game()
				if event.key == K_RIGHT:
					gui.increase_index(tab1)
				elif event.key == K_LEFT:
					gui.decrease_index(tab1)

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

		if key_pressed[K_5]:
			tab1 = EMPTY_TAB
			tab2 = EMPTY_TAB
		if key_pressed[K_4]:
			tab2 = REPUTATION_TAB
		if key_pressed[K_3]:
			tab2 = CHAT_TAB
		if key_pressed[K_2]:
			tab1 = STATS_TAB
		if key_pressed[K_1]:
			tab1 = INVENTORY_TAB

		# Guard start running its state
		guard.run_state(PATROL_STATE, player)

		# render the game map onto the world
		game_map.update_tiles(world)

		door.render(world)

		# Display every item in the game at its position
		for item in items_group:
			item.render(world)

		#display all the actors in the game
		for actor in actors_group:
			actor.render(world)

		# Render everything onto the display surface
		DISPLAYSURF.blit(world, player.camera_pos) # Render Map To The Display

		gui.update(DISPLAYSURF, tab1, tab2)

		pygame.display.update()
		fps_clock.tick(FPS)
