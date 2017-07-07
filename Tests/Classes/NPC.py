from Actor import *
import math, time

# Need to implement collision avoidance

# This is the class that will be used by the NPCs
class NPC(Actor):
	def __init__(self, offset_x, offset_y, actor_type, collision_type, patrol_route, game_map):
		# Don't forget to call the parent class!
		Actor.__init__(self, offset_x, offset_y, actor_type, collision_type)

		# Route set for the NPC
		self.route = patrol_route

		self.astar_route = []
		self.avoid_route = [(0,0)]

		self.route_index = 0
		self.astar_index = 0

		#Tile math stuff
		self.next_tile = (0,0)

		# To keep track of whether the NPC is moving
		self.moving = False

		# slowing down the speed for patrol
		self.speed = 2
		self.change_timer = 8

		self.state = None

		# The map of the game (used to check for objects on tiles)
		self.game_map = game_map

		# Tile location of self
		self.tile_location = (self.rect.x/TILESIZE, self.rect.y/TILESIZE)

	# AI pathfinding algorithm can be improved
	def run_state(self, state, player):
		self.state = state
		if self.state == PATROL_STATE:
			self.patrol()

	def move_to_location(self, location):
		if (self.direction==LEFT or self.direction==NA):
			if (self.rect.x + self.rect.width)/TILESIZE > location[0]:
				self.update(True, LEFT)
				return
			else:
				self.direction=NA

		if (self.direction==RIGHT or self.direction==NA):
			if self.rect.x/TILESIZE < location[0]:
				self.update(True, RIGHT)
				return
			else:
				self.direction=NA

		# Something has to be done here
		if (self.direction==UP or self.direction==NA):
			if (self.rect.y + self.rect.height)/TILESIZE > location[1]:
				self.update(True, UP)
				return
			else:
				self.direction = NA

		if (self.direction==DOWN or self.direction==NA):
			if self.rect.y/TILESIZE < location[1]:
				self.update(True, DOWN)
				return
			else:
				self.direction = NA

	# Will be implemnting the a* algorithm
	def new_patrol(self):
		if len(self.route) <= 0:
			return
		self.speed = 2
		self.change_timer = 8

		# The first element in the route list
		destination = (self.route[self.route_index][0]/TILESIZE, self.route[self.route_index][1]/TILESIZE)
		if destination == self.tile_location:
			print "Done"
			# route_index += 1
			return

		# Getting the next tile to move to
		self.astar_route.append(self.get_next_tile(destination))

		self.move_to_location(self.astar_route[self.astar_index])
		self.astar_index += 1
		time.sleep(0.5)



	# f(n) = g(n) + h(n)
	def get_next_tile(self, destination):
		print ""
		# Get own tile
		self.tile_location = self.get_tile_location()
		#self.tile_location = self.get_tile_location()
		print "Current tile =", self.tile_location

		# if self.tile_location == (0,0):
		# 	print "Next tile =", self.next_tile
		# 	return self.next_tile

		max_fn = MAPWIDTH*MAPHEIGHT
		current_fn = 0
		next_tile = (0,0)

		# Tile to the left
		left_tile = (self.tile_location[0]-1, self.tile_location[1])
		if self.game_map.tile_has_object(left_tile) == False and self.not_avoid(left_tile):
			gn = math.hypot(left_tile[0]-self.tile_location[0], left_tile[1]-self.tile_location[1])
			hn = math.hypot(left_tile[0]-destination[0], left_tile[1]-destination[1])
			current_fn = gn + hn
			if current_fn <= max_fn:
				max_fn = current_fn
				next_tile = left_tile
		# Tile to the right
		right_tile = (self.tile_location[0]+1, self.tile_location[1])
		if self.game_map.tile_has_object(right_tile) == False and self.not_avoid(right_tile):
			gn = math.hypot(right_tile[0]-self.tile_location[0], right_tile[1]-self.tile_location[1])
			hn = math.hypot(right_tile[0]-destination[0], right_tile[1]-destination[1])
			current_fn = gn + hn
			if current_fn <= max_fn:
				max_fn = current_fn
				next_tile = right_tile
		# Tile above
		above_tile = (self.tile_location[0], self.tile_location[1]-1)
		if self.game_map.tile_has_object(above_tile) == False and self.not_avoid(above_tile):
			gn = math.hypot(above_tile[0]-self.tile_location[0], above_tile[1]-self.tile_location[1])
			hn = math.hypot(above_tile[0]-destination[0], above_tile[1]-destination[1])
			current_fn = gn + hn
			if current_fn <= max_fn:
				max_fn = current_fn
				next_tile = above_tile
		# Tile below
		below_tile = (self.tile_location[0], self.tile_location[1]+1)
		if self.game_map.tile_has_object(below_tile) == False and self.not_avoid(below_tile):
			gn = math.hypot(below_tile[0]-self.tile_location[0], below_tile[1]-self.tile_location[1])
			hn = math.hypot(below_tile[0]-destination[0], below_tile[1]-destination[1])
			current_fn = gn + hn
			if current_fn <= max_fn:
				max_fn = current_fn
				next_tile = below_tile

		if self.next_tile == next_tile:
			print "Next tile =", self.next_tile
			return self.next_tile
		else:
			self.avoid_route.append(self.next_tile)
			self.next_tile = next_tile

			print "Next tile =", self.next_tile
			return self.next_tile


	def not_avoid(self, tile):
		if tile in self.avoid_route:
			print "Cannot go to", tile
			return False
		else:
			return True

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

	def stop(self):
		self.speed = 0
		self.update(False, self.direction)
