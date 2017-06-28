
import pygame, sys
pygame.init()

i= 1

inv = []
#Code below will add an item to that list.
w, h = 1000, 600
DISPLAYSURF = pygame.display.set_mode((w, h))
while True:
        DISPLAYSURF.fill((255, 255, 255))
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_x:
                                if len(inv) < 6:
                                        inv.append("item")
                                else:
                                        print("No inventory space")
                        if event.key == pygame.K_z:
                                inv.pop()
                                print('Pop Successful')
                        if event.key == pygame.K_c:
                                print(inv)

