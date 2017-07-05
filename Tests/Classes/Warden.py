from NPC import *

# Basic Nurse class for now
class Warden(NPC):
    def __init__(self, offset_x, offset_y, actor_type, collision_type, patrol_route):
        NPC.__init__(self, offset_x, offset_y, actor_type, collision_type, patrol_route)

        self.influence = 1

    def decrease_threat(self, other):
        other.threat_level -= self.influence

    def increase_threat(self, other):
        other.threat_level += self.influence
