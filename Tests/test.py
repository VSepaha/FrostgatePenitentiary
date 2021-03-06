import pygame, sys
from pygame.locals import *
from PrisonMap import *

pygame.init()

# FPS Setting
FPS = 30

# Height and width of the screen
HEIGHT = 550
WIDTH = 900

# Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW =(255,255,0)

# Values for the tiles
GROUND = 'R'
GRASS = 'G'
WATER = 'W'
DIRT = 'D'

# Map Values
TILESIZE = 40
MAPWIDTH = 25
MAPHEIGHT = 15

# Stat values
STAMINA = 0
HEALTH = 1
RAMEN = 2

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

# This is the actor class that all people will inherit from
class Actor(pygame.sprite.Sprite):
        def __init__(self, offset_x, offset_y, actor_type):
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
                self.other_actor = None


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

                # Using only for testing purposes
                # TODO: Remove and replace
                if self.rect.colliderect(self.other_actor):
                        if dx > 0: # Moving right; Hit the left side of the wall
                                self.rect.right = self.other_actor.rect.left
                        if dx < 0: # Moving left; Hit the right side of the wall
                                self.rect.left = self.other_actor.rect.right
                        if dy > 0: # Moving down; Hit the top side of the wall
                                self.rect.bottom = self.other_actor.rect.top
                        if dy < 0: # Moving up; Hit the bottom side of the wall
                                self.rect.top = self.other_actor.rect.bottom


# This is the class that will be used by the NPCs
class Guard(Actor):
        def __init__(self, offset_x, offset_y, actor_type):
                # Don't forget to call the parent class!
                Actor.__init__(self, offset_x, offset_y, actor_type)

                # Route set for the NPC
                self.route = [
                        (offset_x, offset_y + 300),
                        (offset_x-500, offset_y + 300),
                        (offset_x-500, offset_y),
                        (offset_x, offset_y) 
                ]
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


def key_down_events(event):
        # Nothing for now
        print "Key down:", event.key

def key_up_events(event):
        if event.key == K_w:
                player.update(False, UP)
        if event.key == K_s:
                player.update(False, DOWN)
        if event.key == K_a:
                player.update(False, LEFT)
        if event.key == K_d:
                player.update(False, RIGHT)

class GUI:
    def __init__(self):
        self.health = 100
        self.stamina = 100
        self.ramen = 100
        self.ramen_image = pygame.image.load('ramen.png')

    def decrease_stat(self, stat):
        if stat == HEALTH:
            if self.health <= 0:
                return # Do nothing
            self.health -= 1
        elif stat == STAMINA:
            if self.stamina <= 0:
                return
            self.stamina -= 1  
        else:
            if self.ramen <= 0:
                return
            self.ramen -= 1


    def increase_stat(self, stat):
        if stat == HEALTH:
            if self.health >= 100:
                return
            self.health += 1
        elif stat == STAMINA:
            if self.stamina >= 100:
                return
            self.stamina += 1  
        else:
            if self.ramen >= 999:
                return
            self.ramen += 1

    def get_stat(self, stat):
        if stat == HEALTH:
            return self.health
        if stat == STAMINA:
            return self.stamina

    def display_health(self):
        #displays 'health'
        Font1 = pygame.font.SysFont('monaco', 24)
        healthSurface = Font1.render('Health: {0}%'.format(self.health), True, GREEN)
        healthRect = healthSurface.get_rect()
        healthRect.midtop = (200, 20)
        DISPLAYSURF.blit(healthSurface,healthRect)
        tint = 255 - (self.health * 2.55)
        pygame.draw.rect(DISPLAYSURF, (tint, 255 - tint, 0), pygame.Rect(20, 20, self.health, 20))

    def display_stamina(self):
        #displays 'stamina'
        Font2 = pygame.font.SysFont('monaco', 24)
        stamSurface = Font2.render('Stamina: {0}%'.format(self.stamina), True, GREEN)
        stamRect = stamSurface.get_rect()
        stamRect.midtop = (192, 45)
        DISPLAYSURF.blit(stamSurface,stamRect)
        tint1 = 255 - (self.stamina * 2.55)
        pygame.draw.rect(DISPLAYSURF, (tint1, 0, 255 - tint1), pygame.Rect(20, 45, self.stamina, 20))

    def display_ramen(self):
        #displays ': (ramen amount)'
        Font3 = pygame.font.SysFont('monaco', 44)
        ramSurface = Font3.render(': {0}'.format(self.ramen), True, BLACK)
        ramRect = ramSurface.get_rect()
        ramRect.midtop = (940, 23)
        DISPLAYSURF.blit(ramSurface,ramRect)
        DISPLAYSURF.blit(self.ramen_image, (830,13))


game_map = PrisonMap()
GUI_display = GUI()
player = Actor(100, 100, PLAYER)
guard = Guard(800, 20, PRISON_GUARD)
player.other_actor = guard
guard.other_actor = player

# Used to ensure a maximum fps setting
fps_clock = pygame.time.Clock()

# Set up the window and caption
DISPLAYSURF = pygame.display.set_mode((game_map.WIDTH, game_map.HEIGHT), 0, 32)

# Main game loop
while True:
        game_map.display_map(DISPLAYSURF)

        for event in pygame.event.get():
                if event.type == KEYDOWN:
                        key_down_events(event)
                if event.type == KEYUP:
                        key_up_events(event)
                elif event.type == QUIT:
                        pygame.quit()
                        sys.exit()

        key_pressed = pygame.key.get_pressed()

        if key_pressed[K_w]: 
                player.update(True, UP)
        elif key_pressed[K_s]:
                player.update(True, DOWN)
        elif key_pressed[K_a]:
                player.update(True, LEFT)
        elif key_pressed[K_d]:
                player.update(True, RIGHT)

        GUI_display.display_health()
        GUI_display.display_stamina()
        GUI_display.display_ramen()

        guard.start_patrol(PATROL)

        DISPLAYSURF.blit(guard.current_image, (guard.rect.x, guard.rect.y))
        DISPLAYSURF.blit(player.current_image, (player.rect.x, player.rect.y))

        pygame.display.update()
        fps_clock.tick(FPS)
