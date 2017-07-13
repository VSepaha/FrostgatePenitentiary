import pygame, sys

sys.path.insert(0, 'Settings') # This add the system path
from settings import *

class Object(pygame.sprite.Sprite):
      def __init__(self, offset_x, offset_y, collision_type):
            pygame.sprite.Sprite.__init__(self)

            # image of the object
            self.image = pygame.image.load('Resources/an_item.png')

            # Position of the image
            self.rect = self.image.get_rect()
            self.rect.x = offset_x
            self.rect.y = offset_y

            self.collision_type = collision_type

            self.speed = 0
            self.direction = NA

      def render(self, display):
            display.blit(self.image,(self.rect.x,self.rect.y))
