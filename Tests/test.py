import pygame, sys
from pygame.locals import *

pygame.init()

# FPS Setting
FPS = 30

# Height and width of the screen
HEIGHT = 550
WIDTH = 900

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

# Stat values
STAMINA = 0
HEALTH = 1
RAMEN = 2

class Map:
	def __init__(self):

		# Textures on the map 
		self.textures = {
			'R' :  pygame.image.load('../Resources/Tiles/ground.png'),
			'G' :  pygame.image.load('../Resources/Tiles/grass.png'),
			'W' :  pygame.image.load('../Resources/Tiles/water.png'), 
			'D' :  pygame.image.load('../Resources/Tiles/dirt.png')
		}

		# set the display size of window
		self.WIDTH = TILESIZE * MAPWIDTH
		self.HEIGHT = TILESIZE * MAPHEIGHT

		self.tile_list = [None]*MAPHEIGHT*MAPWIDTH

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

class GUI:
    def __init__(self):
        self.health = 100
        self.stamina = 100
        self.ramen = 100
        self.ramen_image = pygame.image.load('ramen.png')

    def decrease_stat(self, stat):
        if stat == HEALTH:
            if self.health <= 0:
                return # Do nothing
            self.health -= 1
        elif stat == STAMINA:
            if self.stamina <= 0:
                return
            self.stamina -= 1  
        else:
            if self.ramen <= 0:
                return
            self.ramen -= 1


    def increase_stat(self, stat):
        if stat == HEALTH:
            if self.health >= 100:
                return
            self.health += 1
        elif stat == STAMINA:
            if self.stamina >= 100:
                return
            self.stamina += 1  
        else:
            if self.ramen >= 999:
                return
            self.ramen += 1

    def get_stat(self, stat):
        if stat == HEALTH:
            return self.health
        if stat == STAMINA:
            return self.stamina

    def display_health(self):
        #displays 'health'
        Font1 = pygame.font.SysFont('monaco', 24)
        healthSurface = Font1.render('Health: {0}%'.format(self.health), True, GREEN)
        healthRect = healthSurface.get_rect()
        healthRect.midtop = (200, 20)
        DISPLAYSURF.blit(healthSurface,healthRect)
        tint = 255 - (self.health * 2.55)
        pygame.draw.rect(DISPLAYSURF, (tint, 255 - tint, 0), pygame.Rect(20, 20, self.health, 20))

    def display_stamina(self):
        #displays 'stamina'
        Font2 = pygame.font.SysFont('monaco', 24)
        stamSurface = Font2.render('Stamina: {0}%'.format(self.stamina), True, GREEN)
        stamRect = stamSurface.get_rect()
        stamRect.midtop = (192, 45)
        DISPLAYSURF.blit(stamSurface,stamRect)
        tint1 = 255 - (self.stamina * 2.55)
        pygame.draw.rect(DISPLAYSURF, (tint1, 0, 255 - tint1), pygame.Rect(20, 45, self.stamina, 20))

    def display_ramen(self):
        #displays ': (ramen amount)'
        Font3 = pygame.font.SysFont('monaco', 44)
        ramSurface = Font3.render(': {0}'.format(self.ramen), True, BLACK)
        ramRect = ramSurface.get_rect()
        ramRect.midtop = (940, 23)
        DISPLAYSURF.blit(ramSurface,ramRect)
        DISPLAYSURF.blit(self.ramen_image, (830,13))


game_map = Map()
GUI_display = GUI()

# Used to ensure a maximum fps setting
fps_clock = pygame.time.Clock()

# Set up the window and caption
DISPLAYSURF = pygame.display.set_mode((game_map.WIDTH, game_map.HEIGHT), 0, 32)

# Main game loop
while True:
	game_map.display_map(DISPLAYSURF)

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	GUI_display.display_health()
	GUI_display.display_stamina()
	GUI_display.display_ramen()

	pygame.display.update()
	fps_clock.tick(FPS)
