from NPC import *

# Basic Nurse class for now
class Nurse(NPC):
    def __init__(self, offset_x, offset_y, actor_type, collision_type, patrol_route, game_map):
        NPC.__init__(self, offset_x, offset_y, actor_type, collision_type, patrol_route, game_map)

        interactable_group.add(self)
        self.health_boost = 25

        self.final_time = 0
        self.time_set = True
        self.speed = 0
        self.increment = 20

    def set_final_time(self):
        if self.time_set == False:
            self.time_set = True
            self.final_time = time.clock() + self.increment

    def perform_action(self, other):
        # Stop its route here
        self.set_final_time()

        if self.final_time - time.clock() <= 0:
            self.time_set = False
            if other.health <= 100 - self.health_boost:
                other.health = other.health + self.health_boost
            else:
                other.health = 100
        else:
            print "Please come back in",int(((self.final_time - time.clock())/1)), "seconds"
