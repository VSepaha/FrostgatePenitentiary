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

# Used to ensure a maximum fps setting
fps_clock = pygame.time.Clock()

# Set up the window and caption
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

# Main game loop
while True:

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	DISPLAYSURF.fill(WHITE)
	pygame.display.update()
	fps_clock.tick(FPS)
