import pygame
from settings import *

# This is the actor class that all people will inherit from
class Actor(pygame.sprite.Sprite):
    def __init__(self, offset_x, offset_y, actor_type, collision_type):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # When an actor is spawned, we add it to the list
        actors_group.add(self)

        directory = '../Resources/' + actor_type + '/' + actor_type

        # Set up all of the images for any actor
        self.images_front = []
        self.images_front.append(pygame.image.load(directory + '_front_0.png'))
        self.images_front.append(pygame.image.load(directory + '_front_1.png'))
        self.images_front.append(pygame.image.load(directory + '_front_2.png'))

        self.images_back = []
        self.images_back.append(pygame.image.load(directory + '_back_0.png'))
        self.images_back.append(pygame.image.load(directory + '_back_1.png'))
        self.images_back.append(pygame.image.load(directory + '_back_2.png'))

        self.images_left = []
        self.images_left.append(pygame.image.load(directory + '_left_0.png'))
        self.images_left.append(pygame.image.load(directory + '_left_1.png'))
        self.images_left.append(pygame.image.load(directory + '_left_2.png'))

        self.images_right = []
        self.images_right.append(pygame.image.load(directory + '_right_0.png'))
        self.images_right.append(pygame.image.load(directory + '_right_1.png'))
        self.images_right.append(pygame.image.load(directory + '_right_2.png'))

        # Mapping the direction with the variable
        self.direction_map = {
            UP : self.images_back,
            DOWN: self.images_front,
            LEFT : self.images_left,
            RIGHT : self.images_right
        }

        # Set the speed of the player (change in distance)
        self.speed = 4

        # Set the current image
        self.current_image = self.images_front[0]

        # Setting for the update function
        self.change_timer = 6
        self.index = 1
        self.count = 0

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.current_image.get_rect()
        self.rect.x = offset_x
        self.rect.y = offset_y

        # actor that will be colliding
        self.collision_list = []
        self.collision_type = collision_type

        # camera
        self.camera_pos = (0,0) # Create Camara Starting Position

        # The character starts facing downwards
        self.direction = DOWN

    def get_speed(self):
        return self.speed

    def get_direction(self):
        return self.direction

    def get_tile_location(self):
        return (self.rect.x/TILESIZE, self.rect.y/TILESIZE)

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
            if direction == DOWN:
                self.move(0, self.speed)
            if direction == LEFT:
                self.move(-self.speed, 0)
            if direction == RIGHT:
                self.move(self.speed, 0)
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
                if dx < 0: # Moving left; Hit the right side of the wall
                    self.rect.left = other_object.rect.right
                if dy > 0: # Moving down; Hit the top side of the wall
                    self.rect.bottom = other_object.rect.top
                if dy < 0: # Moving up; Hit the bottom side of the wall
                    self.rect.top = other_object.rect.bottom



    def render(self, display):
        display.blit(self.current_image,(self.rect.x,self.rect.y))
