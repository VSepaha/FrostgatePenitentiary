from SmartNPC import *

# The is the basic Prisoner class for now
class Prisoner(SmartNPC):
    def __init__(self, offset_x, offset_y, actor_type, collision_type, patrol_route, threat_level)
        SmartNPC.__init__(self, offset_x, offset_y, actor_type, collision_type, patrol_route)

        self.threat_level = threat_level

    # Make a function here to perform a prison job
