import pygame, sys, time
from pygame.locals import *
from Actor import *

# Directions
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

# Actor types
PLAYER = "player"
PRISON_GUARD = "guard"

# States that the guard can be in 
PATROL = 0 
STAND = 1
CHASE = 2

# Collision Type
BLOCKING = 0
OVERLAPPING = 1

#######################

# This is the class that will be used by the NPCs
class Guard(Actor):
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


	# Guard patrol route implementation
	# AI pathfinding algorithm can be improved
	def start_patrol(self, state):
		route_len = len(self.route)
		if state == PATROL:
			if self.rect.x != self.route[self.route_index][0] or self.rect.y != self.route[self.route_index][1]:
				self.moving = True
				if self.rect.x > self.route[self.route_index][0]:
					self.update(True, LEFT)
				elif self.rect.x < self.route[self.route_index][0]:
					self.update(True, RIGHT)
				if self.rect.y > self.route[self.route_index][1]:
					self.update(True, UP)
				elif self.rect.y < self.route[self.route_index][1]:
					self.update(True, DOWN)
				self.moving == True
			else:
				self.moving = False

			if self.route_index < route_len-1 and self.moving == False:
				self.route_index += 1
				self.update(False, DOWN)
			elif self.route_index >= route_len-1 and self.moving == False:
				self.route_index = 0
				self.update(False, DOWN)