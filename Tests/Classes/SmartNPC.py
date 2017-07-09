from NPC import *

# Need to implement collision avoidance

# This is the class that will be used by the NPCs
class SmartNPC(NPC):
	def __init__(self, offset_x, offset_y, actor_type, collision_type, patrol_route, game_map):
		# Don't forget to call the parent class!
		NPC.__init__(self, offset_x, offset_y, actor_type, collision_type, patrol_route, game_map)

		# Route set for the NPC
		self.route = patrol_route
		self.route_index = 0

		# The next waypoint for the NPC
		self.next_point = (self.rect.x, self.rect.y)

		# To keep track of whether the NPC is moving
		self.moving = False

		# slowing down the speed for patrol
		self.speed = 2
		self.change_timer = 8

		# State of the NPC
		self.state = None

		# Health of the NPC
		self.health = 100

		# If we spotted the player
		self.raycast_set = False

		# Sight distances
		self.sight_distance = 6

	# AI pathfinding algorithm can be improved
	def run_state(self, state, player):
		self.state = state
		if self.state == PATROL_STATE:
			self.patrol()
		elif self.state == CHASE_STATE:
			self.chase_algorithm(player)
		elif self.state == LOCKDOWN_STATE:
			if self.in_raycast(player) and self.raycast_set == False:
				self.raycast_set = True
			if self.raycast_set == True:
				self.chase_algorithm(player)
			else:
				self.state = PATROL_STATE

	def in_raycast(self, player):
		direction = self.direction
		if direction == UP:
			if (self.rect.y/TILESIZE - self.sight_distance) < ((player.rect.y+player.rect.height)/TILESIZE) and player.rect.y < self.rect.y:
				if player.rect.x/TILESIZE == self.rect.x/TILESIZE or (player.rect.x+player.rect.width)/TILESIZE == self.rect.x/TILESIZE:
					return True
		if direction == DOWN:
			if (self.rect.y/TILESIZE + self.sight_distance) > (player.rect.y/TILESIZE) and player.rect.y > self.rect.y:
				if player.rect.x/TILESIZE == self.rect.x/TILESIZE or (player.rect.x+player.rect.width)/TILESIZE == self.rect.x/TILESIZE:
					return True
		if direction == RIGHT:
			if (self.rect.x/TILESIZE + self.sight_distance) > ((player.rect.x)/TILESIZE) and player.rect.x > self.rect.x:
				if player.rect.y/TILESIZE == self.rect.y/TILESIZE or (player.rect.y+player.rect.height)/TILESIZE == self.rect.y/TILESIZE:
					return True
		if direction == LEFT:
			if (self.rect.x/TILESIZE - self.sight_distance) < ((player.rect.x+player.rect.width)/TILESIZE) and player.rect.x < self.rect.x:
				if player.rect.y/TILESIZE == self.rect.y/TILESIZE or (player.rect.y+player.rect.height)/TILESIZE == self.rect.y/TILESIZE:
					return True
		return False

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

		# We'll stick with this collision for now
		if abs(x_pixel_dist) < 40 and abs(y_pixel_dist) < 40:
			print "player caught"
			return

		# This is what we are going to go with for now
		if y_tile_dist == 0 and x_tile_dist != 0:
			self.next_point = ((self.rect.x + (x_tile_dist*TILESIZE))/TILESIZE, self.rect.y/TILESIZE)
		elif x_tile_dist == 0 and y_tile_dist != 0:
			self.next_point = (self.rect.x/TILESIZE, (self.rect.y + (y_tile_dist*TILESIZE))/TILESIZE)
		# If delta x and delta y are equal
		elif abs(y_tile_dist) == abs(x_tile_dist) and x_tile_dist != 0:
		 	if x_tile_dist < 0 and y_tile_dist < 0:
		  		self.next_point = ((self.rect.x - TILESIZE)/TILESIZE, (self.rect.y - TILESIZE)/TILESIZE)
			if x_tile_dist > 0 and y_tile_dist > 0:
		 		self.next_point = ((self.rect.x + TILESIZE)/TILESIZE, (self.rect.y + TILESIZE)/TILESIZE)
			if x_tile_dist < 0 and y_tile_dist > 0:
				self.next_point = ((self.rect.x - TILESIZE)/TILESIZE, (self.rect.y + TILESIZE)/TILESIZE)
			if x_tile_dist > 0 and y_tile_dist < 0:
				self.next_point = ((self.rect.x + TILESIZE)/TILESIZE, (self.rect.y - TILESIZE)/TILESIZE)
		elif abs(x_tile_dist) > abs(y_tile_dist):
			if x_tile_dist > 0:
				self.next_point = ((self.rect.x + TILESIZE)/TILESIZE, self.rect.y/TILESIZE)
			else:
				self.next_point = ((self.rect.x - TILESIZE)/TILESIZE, self.rect.y/TILESIZE)
		elif abs(x_tile_dist) < abs(y_tile_dist):
			if y_tile_dist > 0:
				self.next_point = (self.rect.x/TILESIZE, (self.rect.y + TILESIZE)/TILESIZE)
			else:
				self.next_point = (self.rect.x/TILESIZE, (self.rect.y - TILESIZE)/TILESIZE)
		else:
			self.next_point = (self.rect.x/TILESIZE, self.rect.y/TILESIZE)
			print "player caught"


		if self.rect.x/TILESIZE != self.next_point[0]/TILESIZE or self.rect.y/TILESIZE != self.next_point[1]/TILESIZE:
			self.move_to_location(self.next_point)
