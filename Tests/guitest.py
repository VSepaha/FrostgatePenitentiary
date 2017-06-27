import pygame

STAMINA = 0
HEALTH = 1


pygame.init()

class GUI:
    def __init__(self):
        self.health = 100
        self.stamina = 100

    def decrease_stat(self, stat):
        if stat == HEALTH:
            if self.health <= 0:
                return # Do nothing
            self.health -= 1
        else:
            if self.stamina <= 0:
                return
            self.stamina -= 1

    def increase_stat(self, stat):

        if stat == HEALTH:
            if self.health >= 100:
                return
            self.health += 1
        else:
            if self.stamina >= 100:
                return
            self.stamina += 1

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
        heatSurface = Font2.render('Stamina: {0}%'.format(self.stamina), True, green)
        heatRect = heatSurface.get_rect()
        heatRect.midtop = (192, 45)
        DISPLAYSURF.blit(heatSurface,heatRect)


w, h = 900, 550
DISPLAYSURF = pygame.display.set_mode((w, h))

GUI_display = GUI()

ramen = pygame.image.load('ramen.png')

#colors
red = (255, 0, 0)
green = (0, 255, 0)



while True:
    DISPLAYSURF.fill((0, 0, 0))
    DISPLAYSURF.blit(ramen, (10,100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

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


    # *2.55 because it ranges from 0-100, and 255 is color max
    health = GUI_display.get_stat(HEALTH)
    tint = 255 - (health * 2.55)
    pygame.draw.rect(DISPLAYSURF, (tint, 255 - tint, 0), pygame.Rect(20, 20, health, 20))

    stamina = GUI_display.get_stat(STAMINA)
    tint1 = 255 - (stamina * 2.55)
    pygame.draw.rect(DISPLAYSURF, (tint1, 0, 255 - tint1), pygame.Rect(20, 45, stamina, 20))
    
 
 
    GUI_display.healthy()
    GUI_display.staminad()
    pygame.display.flip()

