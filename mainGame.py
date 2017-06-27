import pygame, sys
from pygame.locals import *

sys.path.insert(0, 'Settings') # This add the system path
from settings import *

pygame.init()

# Set up the window and caption
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Prison Escape')


# Main game loop
while True:

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	DISPLAYSURF.fill(WHITE)
	pygame.display.update()
	fps_clock.tick(FPS)
