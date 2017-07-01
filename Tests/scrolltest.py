import pygame, sys, time
from pygame.locals import *
from PrisonMap import *
from Guard import *

###
pygame.init()

# Directions
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
NA = 4

# Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW =(255,255,0)


# Actor types
PLAYER = "player"
PRISON_GUARD = "guard"

# Collision Type
BLOCKING = 0
OVERLAPPING = 1

# States that the guard can be in 
PATROL = 0 
STAND = 1
CHASE = 2

#######################

# This is the actor class that all people will inherit from
class Actor(pygame.sprite.Sprite):
    def __init__(self, offset_x, offset_y, actor_type, collision_type):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

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

    def add_item(self, item, item_group):
        if self.rect.colliderect(item):
            if  item_group.has(item):
                item_group.remove(item)

    # Works Nicely
    def update(self, move, direction):
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


    def render(self, display):
        display.blit(self.current_image,(self.rect.x,self.rect.y))

###
def key_up_events(event):

    if event.key == K_w:
        camera_pos = player.update(False, UP)
    if event.key == K_s:
        camera_pos = player.update(False, DOWN)
    if event.key == K_a:
        camera_pos = player.update(False, LEFT)
    if event.key == K_d:
        camera_pos = player.update(False, RIGHT)


# how large the display is (window size)
display = pygame.display.set_mode((1000,600))

pygame.display.set_caption("Frostgate")
clock = pygame.time.Clock()

# how large the world map will be
world = pygame.Surface((1000,600)) # Create Map Surface
world.fill(BLACK) # Fill Map Surface Black

# Route set for the NPC
route = [
    (800, 20 + 300),
    (800-500, 20 + 300),
    (800-500, 20),
    (800, 20) 
]

# create the map
game_map = PrisonMap()

# player = Player() # Initialize Player Class
player = Actor(500,300, PLAYER, BLOCKING)
guard = Guard(800, 20, PRISON_GUARD, BLOCKING, route)

player.collision_list.append(guard)
guard.collision_list.append(player)

#
while True:
    for event in pygame.event.get():
        if event.type == KEYUP:
            key_up_events(event)
        elif event.type == QUIT:
            pygame.quit()
            sys.exit()

    # The key pressed events
    key_pressed = pygame.key.get_pressed()

    if key_pressed[K_w]: 
        player.update(True, UP)
    elif key_pressed[K_s]:
        player.update(True, DOWN)
    elif key_pressed[K_a]:
        player.update(True, LEFT)
    elif key_pressed[K_d]:
        player.update(True, RIGHT)

    display.fill(BLACK) # Fill The Background White To Avoid Smearing

    game_map.display_map(world)

    guard.run_patrol(PATROL)

    player.render(world) # Render The Player on the world
    world.blit(guard.current_image,(guard.rect.x, guard.rect.y))

    display.blit(world, player.camera_pos) # Render Map To The Display
    #

    clock.tick(30)
    pygame.display.update()
