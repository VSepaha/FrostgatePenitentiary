import pygame
from settings import *

nothing_object = "nothing.png"
item_object = "an_item.png"

class GUI:
    def __init__(self, player):

        self.player = player

        self.ramen = 100
        self.ramen_image = pygame.image.load('ramen.png')

<<<<<<< HEAD
        self.inventory_frame = pygame.image.load('../Resources/Inventory3/inventory_frame.png')
        self.inventory_frame_inventory = pygame.image.load('../Resources/Inventory3/inventory_frame_inventory.png')
        self.inventory_frame_stats = pygame.image.load('../Resources/Inventory3/inventory_frame_stats.png')
        self.inventory_frame_chat = pygame.image.load('../Resources/Inventory3/inventory_frame_chat.png')

        self.inventory0 = pygame.image.load('../Resources/Inventory3/inventory_position_0.png')
        self.inventory1 = pygame.image.load('../Resources/Inventory3/inventory_position_1.png')
        self.inventory2 = pygame.image.load('../Resources/Inventory3/inventory_position_2.png')
        self.inventory3 = pygame.image.load('../Resources/Inventory3/inventory_position_3.png')
        self.inventory4 = pygame.image.load('../Resources/Inventory3/inventory_position_4.png')
=======
        self.inventory_frame = pygame.image.load('../Resources/Inventory/inventory_frame.png')
        self.inventory_frame_inventory = pygame.image.load('../Resources/Inventory/inventory_frame_inventory.png')
        self.inventory_frame_stats = pygame.image.load('../Resources/Inventory/inventory_frame_stats.png')

        self.inventory0 = pygame.image.load('../Resources/Inventory/inventory_position_0.png')
        self.inventory1 = pygame.image.load('../Resources/Inventory/inventory_position_1.png')
        self.inventory2 = pygame.image.load('../Resources/Inventory/inventory_position_2.png')
        self.inventory3 = pygame.image.load('../Resources/Inventory/inventory_position_3.png')
        self.inventory4 = pygame.image.load('../Resources/Inventory/inventory_position_4.png')
>>>>>>> f339ec0b0d4628f08abb43170f7a039a71e22c3b

        self.inventory_index = 0
        self.inventory_list = [self.inventory0, self.inventory1, self.inventory2, self.inventory3, self.inventory4]

        self.health_stamina_frame = pygame.image.load('../Resources/health_stamina_frame.png')
        self.ramen_frame = pygame.image.load('../Resources/ramen_frame.png')

    def increase_index(self, tab):
        if tab == INVENTORY_TAB:
            if self.inventory_index >= 4:
                self.inventory_index = 0
            else:
                self.inventory_index += 1

    def decrease_index(self, tab):
        if tab == INVENTORY_TAB:
            if self.inventory_index <= 0:
                self.inventory_index = 4
            else:
                self.inventory_index -= 1

    def get_inv_index(self):
        return self.inventory_index

    def update(self, DISPLAYSURF, tab):
        self.health = self.player.get_stat(HEALTH)
        self.stamina = self.player.get_stat(STAMINA)
        #displays the frame surrounding health & stamina
        self.inv = self.player.get_inventory()

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

        # Prison & Guard Reputation
            #Beating up a guard - +10 PR and -20 GR
            #Beating up a player - +5 PR - 5 GR
            #Depending on the rarity of an illegal item, giving it to a player - +1-5 PR
            #Getting caught with an illegal item - -10 GR
            #Dissing guards behind their back - +2 PR (Cooldown)
            #Snitching about a player (Must talk to them to find something out first) - +15 GR -20 PR
            #Killing a high ranked prisoner- -30 PR
            #Serving a job and getting the quota done - +10 GR
            # At level 5 PR - Picking on newbs - 5 PR
          #Prison Level Perks
            #0 - You are picked on by gang members, and frequently stolen from
            #1 - No longer picked on- but still stolen from
            #2 - You can join a gang (Gangs are interested in picking you up)
            #3 - You can ASK your gang for favors
            #4 - You can buy supplies from your own gang
            #5 - You can pick on the newbies and steal from them (also another method of gaining Prison rep)
            #6 - You can start selling
            #7 - The chance to rank up in your gang
            #8 - You are feared by most of the lower levels and your gang, and will NOT be messed with
            #9 - You can potentially lead your gang, and ALL the gangs want you
            #10 - You are feared by the entire prison and even guards- who will not always
          #Guards will grant favors based on your gang reputation+




        #creates the paramaters for the ramen text
        Font3 = pygame.font.SysFont('monaco', 44)
        ramSurface = Font3.render(': {0}'.format(self.ramen), True, BLACK)
        ramRect = ramSurface.get_rect()
        ramRect.midtop = (240, 478)

        Font4 = pygame.font.SysFont('monaco', 22)

        strengthSurf = Font4.render('Strength: {0}'.format(self.strength), True, BLACK)
        strengthRect = strengthSurf.get_rect()
        strengthRect.midtop = (90, 465)

        intelSurf = Font4.render('Intelligence: {0}'.format(self.intelligence), True, BLACK)
        intelRect = strengthSurf.get_rect()
        intelRect.midtop = (90, 511)

        charSurf = Font4.render('Charisma: {0}'.format(self.charisma), True, BLACK)
        charRect = charSurf.get_rect()
        charRect.midtop = (90, 557)

        if tab == INVENTORY_TAB:
            DISPLAYSURF.blit(self.inventory_list[self.inventory_index], (0, 439))
            #Displays ': (ramen amount)'
            DISPLAYSURF.blit(ramSurface,ramRect)
        elif tab == STATS_TAB:
            DISPLAYSURF.blit(self.inventory_frame_stats, (0, 439))
            DISPLAYSURF.blit(strengthSurf,strengthRect)
            DISPLAYSURF.blit(intelSurf,intelRect)
            DISPLAYSURF.blit(charSurf, charRect)
            pygame.draw.rect(DISPLAYSURF, BLUE, pygame.Rect(170, 464, self.strength_bar, 20))
            pygame.draw.rect(DISPLAYSURF, BLUE, pygame.Rect(170, 510, self.intel_bar, 20))
            pygame.draw.rect(DISPLAYSURF, BLUE, pygame.Rect(170, 556, self.charisma_bar, 20))


    #    Displays the inventory
        x_pos = 415
        for item in self.inv:
            if item != None:
                image = item.image
            if tab == INVENTORY_TAB and item != None:
                #Displays the items
                DISPLAYSURF.blit(image, (x_pos,520))
            x_pos += 38
