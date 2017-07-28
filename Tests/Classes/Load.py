from settings import *

class Load:
    def __init__(self):
        self.player = player

    def load_game(self):
        inventory = player.get_inventory()

        save = open('values.txt', 'r')
        self.player.health = save.readline()
        self.player.stamina = save.readline()

        self.player.currency = save.readline()

        playerStart_x = save.readline()
        playerStart_y = save.readline()

        self.player.strength_exp = save.readline()
        self.player.strength_level = save.readline()

        self.player.intelligence_exp = save.readline()
        self.player.intelligence_level = save.readline()

        self.player.charisma_exp = save.readline()
        self.player.intelligence_level = save.readline()

        for item in inventory:
            item = save.readline()

        for actor in actors_group
            actor = save.readline()

        for interactable in interactable_group:
            interactable = save.readline()

        for items in items_group:
            items = save.readline()

        for objects in imm_objects_group:
            objects = save.readline()
