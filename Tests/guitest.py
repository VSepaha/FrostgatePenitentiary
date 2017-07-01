import pygame, sys

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

class GUI:
    def __init__(self):
        self.health = 100
        self.stamina = 100
        self.ramen = 100

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

    def healthy(self):
        #displays 'health'
        Font1 = pygame.font.SysFont('monaco', 24)
        healthSurface = Font1.render('Health: {0}%'.format(self.health), True, green)
        healthRect = healthSurface.get_rect()
        healthRect.midtop = (200, 20)
        DISPLAYSURF.blit(healthSurface,healthRect)
    def staminad(self):
        #displays 'stamina'
        Font2 = pygame.font.SysFont('monaco', 24)
        stamSurface = Font2.render('Stamina: {0}%'.format(self.stamina), True, green)
        stamRect = stamSurface.get_rect()
        stamRect.midtop = (192, 45)
        DISPLAYSURF.blit(stamSurface,stamRect)
    def ramened(self):
        #displays ': (ramen amount)'
        Font3 = pygame.font.SysFont('monaco', 44)
        ramSurface = Font3.render(': {0}'.format(self.ramen), True, black)
        ramRect = ramSurface.get_rect()
        ramRect.midtop = (940, 23)
        DISPLAYSURF.blit(ramSurface,ramRect)


nothing_object = "nothing.png"
item_object = "an_item.png"

w, h = 1000, 600
DISPLAYSURF = pygame.display.set_mode((w, h))
GUI_display = GUI()
inv = [nothing_object, nothing_object, nothing_object, item_object, nothing_object]
ramen = pygame.image.load('ramen.png')
inventory = pygame.image.load('../Resources/inventory.png')

#colors
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)

while True:
    DISPLAYSURF.fill((255, 255, 255))
    DISPLAYSURF.blit(ramen, (830,13))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_j:
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
                    if inv[3] == nothing_object:
                        if inv[2] == nothing_object:
                            if inv[1] == nothing_object:
                                if inv[0] == nothing_object:
                                    print('Nothing to drop!')
                                else: 
                                    inv[0] = nothing_object
                            else:
                                inv[1] = nothing_object
                        else:
                            inv[2] = nothing_object
                    else:
                        inv[3] = nothing_object
                else:
                    inv[4] = nothing_object
            if event.key == pygame.K_l:
                print(inv)


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


    pos0image = pygame.image.load('../Resources/' + inv[0])
    pos1image = pygame.image.load('../Resources/' + inv[1])
    pos2image = pygame.image.load('../Resources/' + inv[2])
    pos3image = pygame.image.load('../Resources/' + inv[3])
    pos4image = pygame.image.load('../Resources/' + inv[4])

  
    # *2.55 because it ranges from 0-100, and 255 is color max
    health = GUI_display.get_stat(HEALTH)
    tint = 255 - (health * 2.55)
    pygame.draw.rect(DISPLAYSURF, (tint, 255 - tint, 0), pygame.Rect(20, 20, health, 20))

    stamina = GUI_display.get_stat(STAMINA)
    tint1 = 255 - (stamina * 2.55)
    pygame.draw.rect(DISPLAYSURF, (tint1, 0, 255 - tint1), pygame.Rect(20, 45, stamina, 20))
    
 
 
    GUI_display.healthy()
    GUI_display.staminad()
    GUI_display.ramened()
    DISPLAYSURF.blit(pos0image, (410, 510))
    DISPLAYSURF.blit(pos1image, (450, 510))
    DISPLAYSURF.blit(pos2image, (490, 510))
    DISPLAYSURF.blit(pos3image, (528, 510))
    DISPLAYSURF.blit(pos4image, (568, 510))
    DISPLAYSURF.blit(inventory, (402, 502))
    pygame.display.flip()

