from NPC import *

# Need to implement collision avoidance

# This is the class that will be used by the NPCs
class SmartNPC(NPC):
	def __init__(self, offset_x, offset_y, actor_type, collision_type, patrol_route):
		# Don't forget to call the parent class!
		NPC.__init__(self, offset_x, offset_y, actor_type, collision_type, patrol_route)

		# Route set for the NPC
		self.route = patrol_route
		self.route_index = 0

		self.next_point = (self.rect.x, self.rect.y)

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
		if self.state == CHASE_STATE:
			self.chase_algorithm(player)

	def chase_algorithm(self, player):
		self.speed = 3
		self.change_timer = 7

		# Get the player location
		player_location = (player.rect.x/TILESIZE, player.rect.y/TILESIZE)
		self_location = (self.rect.x/TILESIZE, self.rect.y/TILESIZE)

		# Calculate the x and y tile distances to the player
		x_tile_dist = (player_location[0] - self_location[0])
		y_tile_dist = (player_location[1] - self_location[1])

		x_pixel_dist = (player.rect.x - self.rect.x)
		y_pixel_dist = (player.rect.y - self.rect.y)

		print ""
		print "player location =", player_location
		print "self location=", self_location

		# We'll stick with this collision for now
		if abs(x_pixel_dist) < 40 and abs(y_pixel_dist) < 40:
			print "player caught"
			return

		# This is what we are going to go with for now
		if y_tile_dist == 0 and x_tile_dist != 0:
			self.next_point = (self.rect.x + (x_tile_dist*TILESIZE), self.rect.y)
		elif x_tile_dist == 0 and y_tile_dist != 0:
			self.next_point = (self.rect.x, self.rect.y + (y_tile_dist*TILESIZE))
		# If delta x and delta y are equal
		elif abs(y_tile_dist) == abs(x_tile_dist) and x_tile_dist != 0:
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
		elif abs(x_tile_dist) < abs(y_tile_dist):
			if y_tile_dist > 0:
				self.next_point = (self.rect.x, self.rect.y + TILESIZE)
			else:
				self.next_point = (self.rect.x, self.rect.y - TILESIZE)
		else:
			self.next_point = (self.rect.x, self.rect.y)
			print "player caught"


		if self.rect.x != self.next_point[0] or self.rect.y != self.next_point[1]:
			self.move_to_location(self.next_point)
