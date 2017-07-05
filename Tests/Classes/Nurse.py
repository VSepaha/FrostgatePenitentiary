from NPC import *

# Basic Nurse class for now
class Nurse(NPC):
    def __init__(self, offset_x, offset_y, actor_type, collision_type, patrol_route):
        NPC.__init__(self, offset_x, offset_y, actor_type, collision_type, patrol_route)

        self.health_boost = 25

    def boost_health(self, other):
        other.health = health + self.health_boost
