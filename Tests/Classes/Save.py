from settings import *

class Save:
    def __init__(self, player):
        self.player = player

    # def save_game(self):
    #     player_pos = self.player.get_position()
    #     shelfFile = shelve.open('Saves/savedGameTrial')
    #     shelfFile['health'] = self.player.get_stat(HEALTH)
    #     shelfFile['stamina'] = self.player.get_stat(STAMINA)

    #     shelfFile['currency'] = self.player.get_ramen()

    #     shelfFile['playerPosition_x'] = player_pos[0]
    #     shelfFile['playerPosition_y'] = player_pos[1]

    #     shelfFile['strength_exp'] = self.player.get_skill(STRENGTH_SKILL, True)
    #     shelfFile['strength_level'] = self.player.get_skill(STRENGTH_SKILL, False)

    #     shelfFile['intelligence_exp'] = self.player.get_skill(INTELLIGENCE_SKILL, True)
    #     shelfFile['intelligence_level'] = self.player.get_skill(INTELLIGENCE_SKILL, False)

    #     shelfFile['charisma_exp'] = self.player.get_skill(CHARISMA_SKILL, True)
    #     shelfFile['charisma_level'] = self.player.get_skill(CHARISMA_SKILL, False)

    #     shelfFile['inventory'] = self.player.get_inventory()

    #     shelfFile['actors_group'] = actors_group
    def save_game(self):
        player_pos = self.player.get_position()

        inventory = self.player.get_inventory()

        save = open('values.txt', 'w')
        save.write(str(self.player.get_stat(HEALTH))+'\n')
        save.write(str(self.player.get_stat(STAMINA))+'\n')

        save.write(str(self.player.get_ramen())+'\n')

        save.write(str(player_pos[0])+'\n')
        save.write(str(player_pos[1])+'\n')



        save.write(str(self.player.get_skill(STRENGTH_SKILL, True))+'\n')
        save.write(str(self.player.get_skill(STRENGTH_SKILL, False))+'\n')

        save.write(str(self.player.get_skill(INTELLIGENCE_SKILL, True))+'\n')
        save.write(str(self.player.get_skill(INTELLIGENCE_SKILL, False))+'\n')

        save.write(str(self.player.get_skill(CHARISMA_SKILL, True))+'\n')
        save.write(str(self.player.get_skill(CHARISMA_SKILL, False))+'\n')

        for item in inventory:
            save.write(str(item)+'\n')

        for actor in actors_group:
            save.write(str(actor)+'\n')

        for interactable in interactable_group:
            save.write(str(interactable)+'\n')

        for items in items_group:
            save.write(str(item)+'\n')

        for objects in imm_objects_group:
            save.write(str(objects)+'\n')
