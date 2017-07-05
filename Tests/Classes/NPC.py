from Actor import *

# Need to implement collision avoidance

# This is the class that will be used by the NPCs
class NPC(Actor):
	def __init__(self, offset_x, offset_y, actor_type, collision_type, patrol_route):
		# Don't forget to call the parent class!
		Actor.__init__(self, offset_x, offset_y, actor_type, collision_type)

		# Route set for the NPC
		self.route = patrol_route
		self.route_index = 0

		# To keep track of whether the NPC is moving
		self.moving = False

		# slowing down the speed for patrol
		self.speed = 2
		self.change_timer = 8

		self.state = None

	# AI pathfinding algorithm can be improved
	def run_state(self, state, player):
		self.state = state
		if self.state == PATROL_STATE:
			self.patrol()

	def move_to_location(self, location):
		if self.rect.x > location[0]:
			self.update(True, LEFT)
		elif self.rect.x < location[0]:
			self.update(True, RIGHT)
		elif self.rect.y > location[1]:
			self.update(True, UP)
		elif self.rect.y < location[1]:
			self.update(True, DOWN)

	def patrol(self):
		self.speed = 2
		self.change_timer = 8
		route_len = len(self.route)
		if route_len > 0:
			location = (self.route[self.route_index][0], self.route[self.route_index][1])

			if self.rect.x != location[0] or self.rect.y != location[1]:
				self.moving = True
				self.move_to_location(location)
			else:
				self.moving = False
			# If we get to the route location and we are no longer moving,
			# go to the next location
			if self.route_index < route_len-1 and self.moving == False:
				self.route_index += 1
			elif self.route_index >= route_len-1 and self.moving == False:
				self.route_index = 0
