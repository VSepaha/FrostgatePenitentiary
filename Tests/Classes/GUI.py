import pygame
from settings import *

nothing_object = "nothing.png"
item_object = "an_item.png"

class GUI:
    def __init__(self, player):

        self.player = player

        self.health = player.get_stat(HEALTH)
        self.stamina = player.get_stat(STAMINA)

        self.strength = 1

        self.ramen = 100
        self.ramen_image = pygame.image.load('ramen.png')
        self.inventory_frame = pygame.image.load('../Resources/inventory_frame.png')
        self.inventory_frame_inventory = pygame.image.load('../Resources/inventory_frame_inventory.png')
        self.inventory_frame_stats = pygame.image.load('../Resources/inventory_frame_stats.png')

        self.health_stamina_frame = pygame.image.load('../Resources/health_stamina_frame.png')
        self.ramen_frame = pygame.image.load('../Resources/ramen_frame.png')
        self.inv = [nothing_object, nothing_object, nothing_object, nothing_object, nothing_object]

    def add_item(self, item):
        for i in range(0, len(self.inv)):
            if self.inv[i] == None:
                self.inv[i] = item
                break

    def remove_item(self, item):
        for i in range(len(self.inv)-1, -1, -1):
            if self.inv[i] == item:
                self.inv[i] = None
                break

    def update(self, DISPLAYSURF, flag):
        self.health = self.player.get_stat(HEALTH)
        self.stamina = self.player.get_stat(STAMINA)
        #displays the frame surrounding health & stamina

        DISPLAYSURF.blit(self.health_stamina_frame, (0, 4))

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

        #creates the paramaters for the ramen text
        Font3 = pygame.font.SysFont('monaco', 44)
        ramSurface = Font3.render(': {0}'.format(self.ramen), True, BLACK)
        ramRect = ramSurface.get_rect()
        ramRect.midtop = (540, 477)

        strengthSurf = Font2.render('Strength: {0}'.format(self.strength), True, BLACK)
        strengthRect = strengthSurf.get_rect()
        strengthRect.midtop = (402, 500)
        if flag == True:
            DISPLAYSURF.blit(self.inventory_frame_inventory, (320, 460))
        else:
            DISPLAYSURF.blit(self.inventory_frame_stats, (320, 460))


        # Displays the inventory
        x_pos = 415
        for item in self.inv:
            image = pygame.image.load('../Resources/' + item)
            if flag == True:
                #Displays the items
                DISPLAYSURF.blit(image, (x_pos,518))
                #Displays ': (ramen amount)'
                DISPLAYSURF.blit(ramSurface,ramRect)
            if flag == False:
                DISPLAYSURF.blit(strengthSurf,strengthRect)
            x_pos += 38
