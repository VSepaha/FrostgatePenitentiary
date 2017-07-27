from Actor import *

class Player(Actor):
	def __init__(self, offset_x, offset_y, actor_type, collision_type, threat_level):
		Actor.__init__(self, offset_x, offset_y, actor_type, collision_type)

		# The threat level that the player will start from
		self.threat_level = threat_level

		# Health of the player
		shelfFile = shelve.open('Saves/savedGameTrial')
		self.health = shelfFile ['health']

		# Stamina of the player
		shelfFile = shelve.open('Saves/savedGameTrial')
		self.stamina = shelfFile ['stamina']

		# Skills that the player has
		shelfFile = shelve.open('Saves/savedGameTrial')
		self.strength_exp = shelfFile ['strength_exp']
		self.intelligence_exp = shelfFile ['intelligence_exp']
		self.charisma_exp = shelfFile ['charisma_exp']
		shelfFile = shelve.open('Saves/savedGameTrial')
		self.strength_level = shelfFile ['strength_level']
		self.intelligence_level = shelfFile ['intelligence_level']
		self.charisma_level = shelfFile ['charisma_level']

		# Amount of currency that the player has
		shelfFile = shelve.open('Saves/savedGameTrial')
		self.currency = shelfFile ['currency']

		# Inventory list
		shelfFile = shelve.open('Saves/savedGameTrial')
		self.inventory = shelfFile ['inventory']

		shelfFile = shelve.open('Saves/savedGameTrial')
		self.test_list = shelfFile ['test']
		# camera
		self.camera_pos = (-self.rect.x + WIN_WIDTH/2, -self.rect.y + WIN_HEIGHT/2) # Create Camara Starting Position

	def increase_exp(self, skill, amount):
		if skill == STRENGTH_SKILL:
			self.strength_exp += amount
			exp_to_level = self.amount_to_increase_level(skill, self.strength_level)
			if self.strength_exp >= exp_to_level:
				self.strength_level += 1
				self.strength_exp = self.strength_exp - exp_to_level
		if skill == INTELLIGENCE_SKILL:
				self.intelligence_exp += amount
				exp_to_level = self.amount_to_increase_level(skill, self.intelligence_level)
				if self.intelligence_exp >= exp_to_level:
					self.intelligence_level += 1
					self.intelligence_exp = self.intelligence_exp - exp_to_level
		if skill == CHARISMA_SKILL:
			self.charisma_exp += amount
			exp_to_level = self.amount_to_increase_level(skill, self.charisma_level)
			if self.charisma_exp >= exp_to_level:
				self.charisma_level += 1
				self.charisma_exp = self.charisma_exp - exp_to_level

	def amount_to_increase_level(self, skill, level):
		if skill == STRENGTH_SKILL:
			current_exp = self.strength_exp
		if skill == INTELLIGENCE_SKILL:
			current_exp = self.intelligence_exp
		if skill == CHARISMA_SKILL:
			current_exp = self.charisma_exp

		next_level_exp = level**2 * level + 100
		return next_level_exp

	def get_stat(self, stat):
		if stat == HEALTH:
			return self.health
		if stat == STAMINA:
			return self.stamina

	def get_inventory(self):
		return self.inventory

	def get_ramen(self):
		return self.currency

	def add_item(self, item):
		for i in range(0, len(self.inventory)):
			if self.inventory[i] == None:
				print "Item added"
				self.inventory[i] = item
				items_group.remove(item)
				break
		print self.inventory

	def drop_item(self, index):
		if self.inventory[index] != None:
			print "Item dropped"
			item  = self.inventory[index]
			item.rect.x = self.rect.x
			item.rect.y = self.rect.y
			items_group.add(item)
			self.inventory[index] = None
			print self.inventory

	def get_skill(self, skill, exp):
		if exp:
			if skill == STRENGTH_SKILL:
				return self.strength_exp
			elif skill == INTELLIGENCE_SKILL:
				return self.intelligence_exp
			elif skill == CHARISMA_SKILL:
				return self.charisma_exp
		else:
			if skill == STRENGTH_SKILL:
				return self.strength_level
			elif skill == INTELLIGENCE_SKILL:
				return self.intelligence_level
			elif skill == CHARISMA_SKILL:
				return self.charisma_level

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

		if abs(delta_x) < TILESIZE+5 and abs(delta_y) < TILESIZE+5:
			return True
		else:
			return False


	def interact(self, flag):
		if flag:
			for interaction in interactable_group:
				if self.collided(interaction):
					print "action performed"
					interaction.perform_action(self)
			for item in items_group:
				if self.collided(item):
					print "got item"
					self.add_item(item)
					items_group.remove(item)
