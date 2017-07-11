from Object import *

# Need to figure out system for setting items and their attributes
class Item(Object):
	def __init__(self, image, offset_x, offset_y, collision_type):
		Object.__init__(self, offset_x, offset_y, collision_type)

		# Add self in the permanent object group
		items_group.add(self)

		# Need to implement variables here

		self.image = pygame.image.load('../Resources/Items/' + image +'.png')

		# Position of the image
		self.rect = self.image.get_rect()
		self.rect.x = offset_x
		self.rect.y = offset_y

		# Permanent objects should always have blocking collision
		self.collision_type = collision_type
