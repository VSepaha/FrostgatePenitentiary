import pygame, sys
from settings import *

class Object(pygame.sprite.Sprite):
      def __init__(self, image, offset_x, offset_y, collision_type):
            pygame.sprite.Sprite.__init__(self)

            # Add itself to the item group
            objects_group.add(self)

            # image of the object
            if image == "prisonwall":
                  self.image = pygame.image.load('../Resources/Tiles/' + image +'.png')
            else:
                  self.image = pygame.image.load('../Resources/' + image +'.png')

            # Position of the image
            self.rect = self.image.get_rect()
            self.rect.x = offset_x
            self.rect.y = offset_y

            self.collision_type = collision_type

            self.speed = 0
            self.direction = NA

      def get_speed(self):
            return self.speed

      def get_direction(self):
            return self.direction

      def render(self, display):
            display.blit(self.image,(self.rect.x,self.rect.y))
