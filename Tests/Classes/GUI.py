import pygame
from settings import *

nothing_object = "nothing.png"
item_object = "an_item.png"

class GUI:
    def __init__(self, player):

        self.falsexpflag = False
        self.truexpflag = True

        self.player = player

        self.health = player.get_stat(HEALTH)
        self.stamina = player.get_stat(STAMINA)

        self.strength = player.get_skill(STRENGTH_SKILL, self.falsexpflag)
        self.strength_exp = player.get_skill(STRENGTH_SKILL, self.truexpflag)

        self.intelligence = player.get_skill(INTELLIGENCE_SKILL, self.falsexpflag)
        self.intelligence_exp = player.get_skill(INTELLIGENCE_SKILL, self.truexpflag)

        self.charisma = player.get_skill(CHARISMA_SKILL, self.falsexpflag)
        self.charisma_exp = player.get_skill(CHARISMA_SKILL, self.truexpflag)

        self.ramen = 100
        self.ramen_image = pygame.image.load('ramen.png')
        self.inventory_frame = pygame.image.load('../Resources/inventory_frame.png')
        self.inventory_frame_inventory = pygame.image.load('../Resources/inventory_frame_inventory.png')
        self.inventory_frame_stats = pygame.image.load('../Resources/inventory_frame_stats.png')

        self.health_stamina_frame = pygame.image.load('../Resources/health_stamina_frame.png')
        self.ramen_frame = pygame.image.load('../Resources/ramen_frame.png')
        self.inv = [nothing_object, nothing_object, nothing_object, nothing_object, nothing_object]

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
            DISPLAYSURF.blit(self.inventory_frame_inventory, (320, 460))
        else:
            DISPLAYSURF.blit(self.inventory_frame_stats, (320, 460))
            DISPLAYSURF.blit(strengthSurf,strengthRect)
            DISPLAYSURF.blit(intelSurf,intelRect)
            DISPLAYSURF.blit(charSurf, charRect)
            pygame.draw.rect(DISPLAYSURF, BLUE, pygame.Rect(450, 480, self.strength_exp, 20))
            pygame.draw.rect(DISPLAYSURF, BLUE, pygame.Rect(470, 510, self.intelligence_exp, 20))
            pygame.draw.rect(DISPLAYSURF, BLUE, pygame.Rect(450, 545, self.charisma_exp, 20))


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
