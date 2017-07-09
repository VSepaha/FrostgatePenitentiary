from Object import *

class InteractableObject(Object):
      def __init__(self, image, offset_x, offset_y, collision_type):
            Object.__init__(self, offset_x, offset_y, collision_type)

            # image of the object
            self.image = pygame.image.load('../Resources/InteractableObjects/' + image +'.png')

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
