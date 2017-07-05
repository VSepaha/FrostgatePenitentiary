from NPC import *

# Basic Nurse class for now
class Nurse(NPC):
    def __init__(self, offset_x, offset_y, actor_type, collision_type, patrol_route):
        NPC.__init__(self, offset_x, offset_y, actor_type, collision_type, patrol_route)

        interactable_group.add(self)
        self.health_boost = 25

        self.speed = 0

    def perform_action(self, other):
        print "Stopping route"
        other.health = other.health + self.health_boost
        print "Player health =", other.health
