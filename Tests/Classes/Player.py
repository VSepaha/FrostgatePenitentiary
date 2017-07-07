from Actor import *

class Player(Actor):
	def __init__(self, offset_x, offset_y, actor_type, collision_type, threat_level):
		Actor.__init__(self, offset_x, offset_y, actor_type, collision_type)

		# The threat level that the player will start from
		self.threat_level = threat_level

		# Health of the player
		self.health = 100

		# Skills that the player has
		self.strength_level = 1
		self.intelligence_level = 1
		self.charisma_level = 1

	# Works Nicely
	def update(self, move, direction):
	    self.direction = direction
	    if move == True:
	        self.count += 1
	        if self.count % self.change_timer == 0:
	            self.index += 1
	        if self.index >= len(self.direction_map[direction]):
	            self.index = 1
	        self.current_image = self.direction_map[direction][self.index]
	        if direction == UP:
	            self.move(0, -self.speed)
	            self.move_camera(UP)
	        if direction == DOWN:
	            self.move(0, self.speed)
	            self.move_camera(DOWN)
	        if direction == LEFT:
	            self.move(-self.speed, 0)
	            self.move_camera(LEFT)
	        if direction == RIGHT:
	            self.move(self.speed, 0)
	            self.move_camera(RIGHT)
	    else:
	        self.index = 0
	        self.count = 0
	        self.current_image = self.direction_map[direction][self.index]

	def move(self, dx, dy):
	    if dx != 0:
	        self.move_single_axis(dx, 0)
	    if dy != 0:
	        self.move_single_axis(0, dy)

	def move_single_axis(self, dx, dy):
	    # Move the rect
	    self.rect.x += dx
	    self.rect.y += dy

	    for other_object in self.collision_list:
	        if self.rect.colliderect(other_object) and other_object.collision_type == BLOCKING:
	            pos_x, pos_y = self.camera_pos
	            if dx > 0: # Moving right; Hit the left side of the object
	                self.rect.right = other_object.rect.left
	                # Code for the camera
	                if other_object.get_direction() == RIGHT:
	                    pos_x += self.speed - other_object.get_speed()
	                else:
	                    pos_x += self.speed
	            if dx < 0: # Moving left; Hit the right side of the object
	                self.rect.left = other_object.rect.right
	                # Code for the camera
	                if other_object.get_direction() == LEFT:
	                    pos_x -= self.speed - other_object.get_speed()
	                else:
	                    pos_x -= self.speed
	            if dy > 0: # Moving down; Hit the top side of the object
	                self.rect.bottom = other_object.rect.top
	                # Code for the camera
	                if other_object.get_direction() == DOWN:
	                    pos_y += self.speed - other_object.get_speed()
	                else:
	                    pos_y += self.speed
	            if dy < 0: # Moving up; Hit the bottom side of the object
	                self.rect.top = other_object.rect.bottom
	                if other_object.get_direction() == UP:
	                    pos_y -= self.speed - other_object.get_speed()
	                else:
	                    pos_y -= self.speed
	            self.camera_pos = (pos_x, pos_y)


	def move_camera(self, direction):

	    pos_x,pos_y = self.camera_pos # Split camara_pos

	    if direction == UP: # Check Key
	        pos_y += self.speed # Move Camara Coord Against Player Rect
	    if direction == RIGHT:
	        pos_x -= self.speed
	    if direction == DOWN:
	        pos_y -= self.speed
	    if direction == LEFT:
	        pos_x += self.speed

	    self.camera_pos = (pos_x,pos_y) # Return New Camera Pos

	def collided(self, other):
		delta_x = other.rect.x - self.rect.x
		delta_y = other.rect.y - self.rect.y

		if abs(delta_x) < TILESIZE and abs(delta_y) < TILESIZE:
			return True
		else:
			return False


	def interact(self, flag):
		if flag:
			for npc in interactable_group:
				if self.collided(npc):
					print "collided with npc"
					npc.perform_action(self)
			for item in items_group:
				if self.collided(item):
					print "collided with item"
					item.pickup()
		else:
			return
