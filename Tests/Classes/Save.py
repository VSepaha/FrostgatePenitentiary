from settings import *

class Save:
    def __init__(self, player):
        self.player = player

    def save_game(self):
        player_pos = self.player.get_position()
        shelfFile = shelve.open('Saves/savedGameTrial')
        shelfFile['health'] = self.player.get_stat(HEALTH)
        shelfFile['stamina'] = self.player.get_stat(STAMINA)

        shelfFile['currency'] = self.player.get_ramen()

        shelfFile['playerPosition_x'] = player_pos[0]
        shelfFile['playerPosition_y'] = player_pos[1]

        shelfFile['strength_exp'] = self.player.get_skill(STRENGTH_SKILL, True)
        shelfFile['strength_level'] = self.player.get_skill(STRENGTH_SKILL, False)

        shelfFile['intelligence_exp'] = self.player.get_skill(INTELLIGENCE_SKILL, True)
        shelfFile['intelligence_level'] = self.player.get_skill(INTELLIGENCE_SKILL, False)

        shelfFile['charisma_exp'] = self.player.get_skill(CHARISMA_SKILL, True)
        shelfFile['charisma_level'] = self.player.get_skill(CHARISMA_SKILL, False)

        shelfFile['inventory'] = self.player.get_inventory()
