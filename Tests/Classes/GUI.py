import pygame
from settings import *

nothing_object = "nothing.png"
item_object = "an_item.png"

class GUI:
    def __init__(self, player):

        self.player = player



        self.ramen = 100
        self.ramen_image = pygame.image.load('ramen.png')

        self.inventory_frame = pygame.image.load('../Resources/Inventory/inventory_frame.png')
        self.inventory_frame_inventory = pygame.image.load('../Resources/Inventory/inventory_frame_inventory.png')
        self.inventory_frame_stats = pygame.image.load('../Resources/Inventory/inventory_frame_stats.png')

        self.inventory0 = pygame.image.load('../Resources/Inventory/inventory_position_0.png')
        self.inventory1 = pygame.image.load('../Resources/Inventory/inventory_position_1.png')
        self.inventory2 = pygame.image.load('../Resources/Inventory/inventory_position_2.png')
        self.inventory3 = pygame.image.load('../Resources/Inventory/inventory_position_3.png')
        self.inventory4 = pygame.image.load('../Resources/Inventory/inventory_position_4.png')

        self.inventory_index = 0
        self.inventory_list = [self.inventory0, self.inventory1, self.inventory2, self.inventory3, self.inventory4]

        self.health_stamina_frame = pygame.image.load('../Resources/health_stamina_frame.png')
        self.ramen_frame = pygame.image.load('../Resources/ramen_frame.png')
        self.inv = [nothing_object, nothing_object, nothing_object, nothing_object, nothing_object]
    def increase_index(self):
        if self.inventory_index >= 4:
            self.inventory_index = 0
        else:
            self.inventory_index += 1
    def decrease_index(self):
            if self.inventory_index <= 0:
                self.inventory_index = 4
            else:
                self.inventory_index -= 1

    def update(self, DISPLAYSURF, flag):
        self.health = self.player.get_stat(HEALTH)
        self.stamina = self.player.get_stat(STAMINA)
        #displays the frame surrounding health & stamina

        self.strength = self.player.get_skill(STRENGTH_SKILL, False)
        self.strength_exp = self.player.get_skill(STRENGTH_SKILL, True)
        self.strength_bar_1 = (self.strength_exp)/float(self.player.amount_to_increase_level(STRENGTH_SKILL, self.strength))
        self.strength_bar = self.strength_bar_1*100

        self.intelligence = self.player.get_skill(INTELLIGENCE_SKILL, False)
        self.intelligence_exp = self.player.get_skill(INTELLIGENCE_SKILL, True)
        self.intel_bar_1 = (self.intelligence_exp)/float(self.player.amount_to_increase_level(INTELLIGENCE_SKILL, self.intelligence))
        self.intel_bar = self.intel_bar_1*100


        self.charisma = self.player.get_skill(CHARISMA_SKILL, False)
        self.charisma_exp = self.player.get_skill(CHARISMA_SKILL, True)
        self.charisma_bar_1 = (self.charisma_exp)/float(self.player.amount_to_increase_level(CHARISMA_SKILL, self.charisma))
        self.charisma_bar = self.charisma_bar_1*100
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

        Font4 = pygame.font.SysFont('monaco', 22)

        strengthSurf = Font4.render('Strength: {0}'.format(self.strength), True, BLACK)
        strengthRect = strengthSurf.get_rect()
        strengthRect.midtop = (400, 480)

        intelSurf = Font4.render('Intelligence: {0}'.format(self.intelligence), True, BLACK)
        intelRect = strengthSurf.get_rect()
        intelRect.midtop = (400, 511)

        charSurf = Font4.render('Charisma: {0}'.format(self.charisma), True, BLACK)
        charRect = charSurf.get_rect()
        charRect.midtop = (400, 547)

        if flag == True:
            DISPLAYSURF.blit(self.inventory_list[self.inventory_index], (320, 460))
        else:
            DISPLAYSURF.blit(self.inventory_frame_stats, (320, 460))
            DISPLAYSURF.blit(strengthSurf,strengthRect)
            DISPLAYSURF.blit(intelSurf,intelRect)
            DISPLAYSURF.blit(charSurf, charRect)
            pygame.draw.rect(DISPLAYSURF, BLUE, pygame.Rect(450, 480, self.strength_bar, 20))
            pygame.draw.rect(DISPLAYSURF, BLUE, pygame.Rect(470, 510, self.intel_bar, 20))
            pygame.draw.rect(DISPLAYSURF, BLUE, pygame.Rect(450, 545, self.charisma_bar, 20))


        # Displays the inventory
        x_pos = 415
        for item in self.inv:
            image = pygame.image.load('../Resources/' + item)
            if flag == True:
                #Displays the items
                DISPLAYSURF.blit(image, (x_pos,518))
                #Displays ': (ramen amount)'
                DISPLAYSURF.blit(ramSurface,ramRect)

            x_pos += 38
