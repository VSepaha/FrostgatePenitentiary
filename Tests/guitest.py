import pygame, sys

<<<<<<< HEAD
sys.path.insert(0, 'Classes') # This add the system path
from GUI import *
=======
STAMINA = 0
HEALTH = 1
RAMEN = 2

#inventory ids
an_item = 1
baton = 2
bat = 3
key = 4
pos0 = 1
pos1 = 1
pos2 = 1
pos3 = 1
pos4 = 1
pygame.init()
index = 4
>>>>>>> 60412b2270b7cca2bfa344619b110e110825d37e

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
<<<<<<< HEAD
                GUI_display.add_item()

            if event.key == pygame.K_k:
                GUI_display.remove_item()

=======
                if inv[0] == nothing_object:
                    #when I call this later while blitting the image, it is because the image is an_item.png
                    inv[0] = item_object
                    item = inv[0]
                elif inv[1] == nothing_object:
                    inv[1] = item_object
                    item = inv[1]
                elif inv[2] == nothing_object:
                    inv[2] = item_object
                    item = inv[2]
                elif inv[3] == nothing_object:
                    inv[3] = item_object
                    item = inv[3]
                elif inv[4] == nothing_object:
                    inv[4] = item_object
                    item = inv[4]

                else:
                        print('No inventory space')

            if event.key == pygame.K_k:
                if inv[4] == nothing_object:
                    #the image is called None.png so it should work later
                    # while index >= 0:

                    #     if inv[index] == 0:
                    #         index -= 1
                    #         continue
                    #     else:
                    #         inv[index] = nothing_object
                    #         index -= 1
                    #         break
                    for item in inv:
                        if item == nothing_object:
                            continue
                        else:
                            item = nothing_object
                            break

                #     if inv[3] == nothing_object:
                #         if inv[2] == nothing_object:
                #             if inv[1] == nothing_object:
                #                 if inv[0] == nothing_object:
                #                     print('Nothing to drop!')
                #                 else: 
                #                     inv[0] = nothing_object
                #             else:
                #                 inv[1] = nothing_object
                #         else:
                #             inv[2] = nothing_object
                #     else:
                #         inv[3] = nothing_object
                # else:
                #     inv[4] = nothing_object
>>>>>>> 60412b2270b7cca2bfa344619b110e110825d37e
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

