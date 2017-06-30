
import pygame, sys
pygame.init()

an_item = 1
baton = 2
bat = 3
key = 4
pos0 = 0
pos1 = 0
pos2 = 0
pos3 = 0
pos4 = 0

inv = [None, None, None, 'an_item', None]
#Code below will add an item to that list.
w, h = 1000, 600
inventory = pygame.image.load('../Resources/inventory.png')
DISPLAYSURF = pygame.display.set_mode((w, h))
DISPLAYSURF.fill((255, 255, 255))

while True:
        DISPLAYSURF.blit(inventory, (400, 500))
        if pos0 == 1:
                pos0image = pygame.image.load('../Resources/an_item.png')
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_x:
                                if inv[0] == None:
                                        inv[0] = 'an_item'
                                        pos0 = 1

                                elif inv[1] == None:
                                        inv[1] = 'an_item'
                                        pos1 = 1
                                elif inv[2] == None:
                                        inv[2] = 'an_item'
                                        pos2 = 1
                                elif inv[3] == None:
                                        inv[3] = 'an_item'
                                        pos3 = 1
                                elif inv[4] == None:
                                        inv[4] = 'an_item'
                                        pos4 = 1n
                                else:
                                        print("No inventory space")
                        if event.key == pygame.K_z:
                                if inv[4] == None:
                                        if inv[3] == None:
                                                if inv[2] == None:
                                                        if inv[1] == None:
                                                                if inv[0] == None:
                                                                        print('Nothing to drop!')
                                                                else: inv[0] = None

                                                        else:
                                                                inv[1] = None
                                                else:
                                                        inv[2] = None
                                        else:
                                                inv[3] = None
                                else:
                                        inv[4] = None
                        if event.key == pygame.K_c:
                                print(inv)
                        if event.key == pygame.K_f:
                                DISPLAYSURF.blit(pos0image, (400, 500))


