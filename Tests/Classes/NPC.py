from Actor import *
import math, time, sys

# Need to implement collision avoidance

# This is the class that will be used by the NPCs
class NPC(Actor):
	def __init__(self, offset_x, offset_y, actor_type, collision_type, patrol_route, game_map):
		# Don't forget to call the parent class!
		Actor.__init__(self, offset_x, offset_y, actor_type, collision_type)

		# Route set for the NPC
		self.route = patrol_route

		# indexes for the lists
		self.route_index = 0
		self.astar_index = 0

		# Tile location of self
		self.tile_location = (self.rect.x/TILESIZE, self.rect.y/TILESIZE)

		#Tile math stuff
		self.next_tile = (0,0)

		# To keep track of whether the NPC is moving
		self.moving = False

		# slowing down the speed for patrol
		self.speed = 2
		self.change_timer = 8

		# Current state of the NPC
		self.state = None

		# The map of the game (used to check for objects on tiles)
		self.game_map = game_map

		# Check to see if path is done and index is set
		self.set = False
		self.set_index = False

	# AI pathfinding algorithm can be improved
	def run_state(self, state, player):
		self.state = state
		if self.state == PATROL_STATE:
			self.patrol()

# A* with errors
	def set_path(self, destination):
		self.tile_location = self.get_tile_location()
		# Set of nodes already evaluated
		self.closed_set = []
		# Set of currently discovered nodes, not evaluated yet
		self.open_set = [self.tile_location]
		# Contain the most efficient previous steps
		self.came_from = {}
		# cost from going from start to node
		self.g_score = {}
		for i in range (0, MAPHEIGHT):
			for j in range (0, MAPWIDTH):
				self.g_score[(j,i)] = sys.maxint
		self.g_score[self.tile_location] = 0
		# total current cost from getting start to finish
		self.f_score = {
			self.tile_location : math.hypot(destination[0]-self.tile_location[0], destination[1]-self.tile_location[1])
		}
		print "starting point =", self.tile_location
		print "destination =", destination
		while len(self.open_set) != 0:
			current_tile = (0,0)
			current_value = MAPWIDTH*MAPHEIGHT
			for node in self.open_set:
				if self.f_score[node] < current_value:
					current_value = self.f_score[node]
					current_tile = node

			if current_tile == destination:
				print "Path found"
				self.reconstruct_path(current_tile)
				return

			self.open_set.remove(current_tile)
			self.closed_set.append(current_tile)

			self.explore_neighbors(current_tile, destination)

	def reconstruct_path(self, current_tile):
		self.total_path = [current_tile]
		for key, value in self.came_from.iteritems():
			if current_tile not in self.came_from:
				break
			current_tile = self.came_from[current_tile]
			self.total_path.append(current_tile)
		self.total_path.remove(current_tile)


	def explore_neighbors(self, current_tile, destination):
		neighbors = []
		# left_tile
		neighbors.append((current_tile[0]-1, current_tile[1]))
		# right_tile
		neighbors.append((current_tile[0]+1, current_tile[1]))
		# above_tile
		neighbors.append((current_tile[0], current_tile[1]-1))
		# below_tile
		neighbors.append((current_tile[0], current_tile[1]+1))

		# check every neighbor
		for neighbor in neighbors:
			if neighbor in self.closed_set:
				continue

			if neighbor not in self.open_set:
				# If there is not an object there
				if self.game_map.tile_has_object(neighbor) == False:
					self.open_set.append(neighbor)
				else:
					continue

			# distance from start to neighbor
			g_dist = math.hypot(current_tile[0]-neighbor[0], current_tile[1]-neighbor[1])
			tentative_g_score = self.g_score[current_tile] + g_dist

			if tentative_g_score >= self.g_score[neighbor]:
				continue # Not a good path to take

			# Possibly a good path, so map
			self.came_from[neighbor] = current_tile
			self.g_score[neighbor] = tentative_g_score

			h_score = math.hypot(destination[0] - neighbor[0], destination[1]-neighbor[1])
			self.f_score[neighbor] = self.g_score[neighbor] + h_score


	# Movement using tiles
	def move_to_location(self, location):
		if (self.direction == LEFT or self.direction == NA):
			if (self.rect.x + self.rect.width)/TILESIZE > location[0]:
				self.update(True, LEFT)
				return
			else:
				self.direction = NA

		if (self.direction==RIGHT or self.direction==NA):
			if self.rect.x/TILESIZE < location[0]:
				self.update(True, RIGHT)
				return
			else:
				self.direction = NA

		if (self.direction == UP or self.direction == NA):
			if (self.rect.y + self.rect.height)/TILESIZE > location[1]:
				self.update(True, UP)
				return
			else:
				self.direction = NA

		if (self.direction == DOWN or self.direction == NA):
			if self.rect.y/TILESIZE < location[1]:
				self.update(True, DOWN)
				return
			else:
				self.direction = NA

	def patrol(self):
		# If nothing in route, then return
		if len(self.route) <= 0:
			return

		# Speed the NPC is moving
		self.speed = 2
		self.change_timer = 8

		# Consists of elements in the route list
		destination = (self.route[self.route_index][0]/TILESIZE, self.route[self.route_index][1]/TILESIZE)

		# If no path is set, then set a path
		if self.set == False:
			self.set = True
			self.set_path(destination)
			print "-------------------------------------------------------------"

		# Getting the next tile to move to
		route_len = len(self.total_path)
		if self.set_index == False:
			self.astar_index = route_len - 1
			self.set_index = True
		location = self.total_path[self.astar_index]
		if self.rect.x/TILESIZE != location[0] or self.rect.y/TILESIZE != location[1]:
			self.moving = True
			self.move_to_location(location)
		else:
			self.tile_location = (self.rect.x/TILESIZE, self.rect.y/TILESIZE)
			self.moving = False

		# If we get to the route location and we are no longer moving,
		# go to the next location
		if self.astar_index > 0 and self.moving == False:
			self.astar_index -= 1
		elif self.astar_index <= 0 and self.moving == False:
			if self.route_index < len(self.route)-1:
				self.route_index += 1
			else:
				self.route_index = 0
			self.set = False
			self.set_index = False

	def stop(self):
		self.speed = 0
		self.update(False, self.direction)
