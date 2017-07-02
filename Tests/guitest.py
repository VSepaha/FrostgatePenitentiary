import pygame, sys

sys.path.insert(0, 'Classes') # This add the system path
from GUI import *

pygame.init()

w, h = 1000, 600
DISPLAYSURF = pygame.display.set_mode((w, h))
GUI_display = GUI()

#colors
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)

while True:
    DISPLAYSURF.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_j:
                GUI_display.add_item()

            if event.key == pygame.K_k:
                GUI_display.remove_item()

            if event.key == pygame.K_l:
                print(GUI_display.inv)


    # This relies on the previous line being called, or else it won't update,
    key_pressed = pygame.key.get_pressed()
    #checks what key is pressed to change health-- which then decides the size of the rectangle and color
    if key_pressed[pygame.K_x]:
        GUI_display.decrease_stat(HEALTH)
    if key_pressed[pygame.K_z]:
        GUI_display.increase_stat(HEALTH)

    #checks what key is pressed to change heat-- which then decides the size of the rectangle and color

    if key_pressed[pygame.K_v]:
        GUI_display.decrease_stat(STAMINA)
    if key_pressed[pygame.K_c]:
        GUI_display.increase_stat(STAMINA)

    if key_pressed[pygame.K_n]:
        GUI_display.decrease_stat(RAMEN)
    if key_pressed[pygame.K_b]:
        GUI_display.increase_stat(RAMEN)
  
    # *2.55 because it ranges from 0-100, and 255 is color max
    health = GUI_display.get_stat(HEALTH)
    tint = 255 - (health * 2.55)
    pygame.draw.rect(DISPLAYSURF, (tint, 255 - tint, 0), pygame.Rect(20, 20, health, 20))

    stamina = GUI_display.get_stat(STAMINA)
    tint1 = 255 - (stamina * 2.55)
    pygame.draw.rect(DISPLAYSURF, (tint1, 0, 255 - tint1), pygame.Rect(20, 45, stamina, 20))
    
 
    GUI_display.update(DISPLAYSURF)

    pygame.display.flip()

