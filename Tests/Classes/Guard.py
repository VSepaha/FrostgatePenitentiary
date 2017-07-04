from Actor import *

# This is the class that will be used by the NPCs
class Guard(Actor):
	def __init__(self, offset_x, offset_y, actor_type, collision_type, patrol_route):
		# Don't forget to call the parent class!
		Actor.__init__(self, offset_x, offset_y, actor_type, collision_type)

		# Route set for the NPC
		self.route = patrol_route
		self.route_index = 0

		self.next_point = (self.rect.x, self.rect.y)
		self.ratio = 1

		# To keep track of whether the NPC is moving
		self.moving = False

		# slowing down the speed for patrol
		self.speed = 2
		self.change_timer = 8

		self.state = None

	# Guard patrol route implementation
	# AI pathfinding algorithm can be improved
	def run_state(self, state, player):
		self.state = state
		if self.state == PATROL_STATE:
			self.patrol()
		if self.state == CHASE_STATE:
			self.chase_algorithm(player)

	def move_to_location(self, location):
		if self.rect.x > location[0]:
			self.update(True, LEFT)
		elif self.rect.x < location[0]:
			self.update(True, RIGHT)
		elif self.rect.y > location[1]:
			self.update(True, UP)
		elif self.rect.y < location[1]:
			self.update(True, DOWN)

	def chase_algorithm(self, player):
		self.speed = 3
		self.change_timer = 7

		# Get the player location
		player_location = (player.rect.x/TILESIZE, player.rect.y/TILESIZE)
		self_location = (self.rect.x/TILESIZE, self.rect.y/TILESIZE)
		# Calculate the x and y tile distances to the player
		print ""

		x_tile_dist = (player_location[0] - self_location[0])
		y_tile_dist = (player_location[1] - self_location[1])

		print "distance = ", (x_tile_dist, y_tile_dist)

		# This is what we are going to go with for now
		if y_tile_dist == 0 and x_tile_dist != 0:
			print "y = 0"
			self.next_point = (self.rect.x + (x_tile_dist*TILESIZE), self.rect.y)
		elif x_tile_dist == 0 and y_tile_dist != 0:
			print "x = 0"
			self.next_point = (self.rect.x, self.rect.y + (y_tile_dist*TILESIZE))
		# If delta x and delta y are equal
		elif abs(y_tile_dist) == abs(x_tile_dist) and x_tile_dist != 0:
		 	print "x = y"
		 	if x_tile_dist < 0 and y_tile_dist < 0:
		  		self.next_point = (self.rect.x - TILESIZE, self.rect.y - TILESIZE)
			if x_tile_dist > 0 and y_tile_dist > 0:
		 		self.next_point = (self.rect.x + TILESIZE, self.rect.y + TILESIZE)
			if x_tile_dist < 0 and y_tile_dist > 0:
				self.next_point = (self.rect.x - TILESIZE, self.rect.y + TILESIZE)
			if x_tile_dist > 0 and y_tile_dist < 0:
				self.next_point = (self.rect.x + TILESIZE, self.rect.y - TILESIZE)
		elif abs(x_tile_dist) > abs(y_tile_dist):
			if x_tile_dist > 0:
				self.next_point = (self.rect.x + TILESIZE, self.rect.y)
			else:
				self.next_point = (self.rect.x - TILESIZE, self.rect.y)
		else:
			if y_tile_dist > 0:
				self.next_point = (self.rect.x, self.rect.y + TILESIZE)
			else:
				self.next_point = (self.rect.x, self.rect.y - TILESIZE)


		print "next point = ",self.next_point
		print ""

		if self.rect.x != self.next_point[0] or self.rect.y != self.next_point[1]:
			self.move_to_location(self.next_point)

	def patrol(self):
		self.speed = 2
		self.change_timer = 8
		route_len = len(self.route)
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
