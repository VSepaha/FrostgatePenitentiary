from NPC import *

# Basic Nurse class for now
class Warden(NPC):
    def __init__(self, offset_x, offset_y, actor_type, collision_type, patrol_route, game_map):
        NPC.__init__(self, offset_x, offset_y, actor_type, collision_type, patrol_route, game_map)

        interactable_group.add(self)

        self.influence = 1

        self.speed = 0

    def perform_action(self, other):
        print "Stopping route"
        print "Threat level might change for", other

    def decrease_threat(self, other):
        other.threat_level -= self.influence

    def increase_threat(self, other):
        other.threat_level += self.influence
