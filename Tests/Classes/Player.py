from Actor import *

class Player(Actor):
	def __init__(self, offset_x, offset_y, actor_type, collision_type):
		Actor.__init__(self, offset_x, offset_y, actor_type, collision_type)

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
	            if dx > 0: # Moving right; Hit the left side of the wall
	                self.rect.right = other_object.rect.left
	                # Code for the camera
	                if other_object.get_direction() == RIGHT:
	                    pos_x += 4 - other_object.get_speed()
	                else:
	                    pos_x += 4 
	                ############################
	            if dx < 0: # Moving left; Hit the right side of the wall
	                self.rect.left = other_object.rect.right
	                # Code for the camera
	                if other_object.get_direction() == LEFT:
	                    pos_x -= 4 - other_object.get_speed()
	                else:
	                    pos_x -= 4
	                ############################
	            if dy > 0: # Moving down; Hit the top side of the wall
	                self.rect.bottom = other_object.rect.top
	                # Code for the camera
	                if other_object.get_direction() == DOWN:
	                    pos_y += 4 - other_object.get_speed()
	                else:
	                    pos_y += 4
	                ############################
	            if dy < 0: # Moving up; Hit the bottom side of the wall
	                self.rect.top = other_object.rect.bottom
	                if other_object.get_direction() == UP:
	                    pos_y -= 4 - other_object.get_speed()
	                else:
	                    pos_y -= 4
	            self.camera_pos = (pos_x, pos_y)


	def move_camera(self, direction):

	    pos_x,pos_y = self.camera_pos # Split camara_pos

	    if direction == UP: # Check Key
	        pos_y += 4 # Move Camara Coord Against Player Rect
	    if direction == RIGHT:
	        pos_x -= 4
	    if direction == DOWN:
	        pos_y -= 4
	    if direction == LEFT:
	        pos_x += 4

	    self.camera_pos = (pos_x,pos_y) # Return New Camera Pos