from NPC import *

# Basic Nurse class for now
class Nurse(NPC):
    def __init__(self, offset_x, offset_y, actor_type, collision_type, patrol_route, game_map):
        NPC.__init__(self, offset_x, offset_y, actor_type, collision_type, patrol_route, game_map)

        interactable_group.add(self)
        self.health_boost = 25

        self.speed = 0

    def perform_action(self, other):
        # Stop its route here
        if other.health <= 100 - self.health_boost:
            other.health = other.health + self.health_boost
        else:
            other.health = 100
