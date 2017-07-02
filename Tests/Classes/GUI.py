import pygame
from settings import *

nothing_object = "nothing.png"
item_object = "an_item.png"

class GUI:
    def __init__(self):
        self.health = 100
        self.stamina = 100
        self.ramen = 100
        self.ramen_image = pygame.image.load('ramen.png')
        self.inventory_image = pygame.image.load('../Resources/inventory.png')

        self.inv = [nothing_object, nothing_object, nothing_object, nothing_object, nothing_object]


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

    def add_item(self):
        for i in range(0, len(self.inv)):
            if self.inv[i] == nothing_object:
                self.inv[i] = item_object
                break

    def remove_item(self):
        for i in range(len(self.inv)-1, -1, -1):
            if self.inv[i] == item_object:
                self.inv[i] = nothing_object
                break

    def update(self, DISPLAYSURF):
        #displays 'health'
        Font1 = pygame.font.SysFont('monaco', 24)
        healthSurface = Font1.render('Health: {0}%'.format(self.health), True, GREEN)
        healthRect = healthSurface.get_rect()
        healthRect.midtop = (200, 20)
        DISPLAYSURF.blit(healthSurface,healthRect)
        tint = 255 - (self.health * 2.55)
        pygame.draw.rect(DISPLAYSURF, (tint, 255 - tint, 0), pygame.Rect(20, 20, self.health, 20))

        #displays 'stamina'
        Font2 = pygame.font.SysFont('monaco', 24)
        stamSurface = Font2.render('Stamina: {0}%'.format(self.stamina), True, GREEN)
        stamRect = stamSurface.get_rect()
        stamRect.midtop = (192, 45)
        DISPLAYSURF.blit(stamSurface,stamRect)
        tint1 = 255 - (self.stamina * 2.55)
        pygame.draw.rect(DISPLAYSURF, (tint1, 0, 255 - tint1), pygame.Rect(20, 45, self.stamina, 20))

        #displays ': (ramen amount)'
        Font3 = pygame.font.SysFont('monaco', 44)
        ramSurface = Font3.render(': {0}'.format(self.ramen), True, BLACK)
        ramRect = ramSurface.get_rect()
        ramRect.midtop = (940, 23)
        DISPLAYSURF.blit(ramSurface,ramRect)
        DISPLAYSURF.blit(self.ramen_image, (830,13))

        # Displays the inventory
        DISPLAYSURF.blit(self.inventory_image, (402, 502))
        x_pos = 410
        for item in self.inv:
            image = pygame.image.load('../Resources/' + item)
            DISPLAYSURF.blit(image, (x_pos,510))
            x_pos += 40

