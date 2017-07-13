from Object import *

class InteractableObject(Object):
    def __init__(self, images, offset_x, offset_y, collision_type, obj):
        Object.__init__(self, offset_x, offset_y, collision_type)

        interactable_group.add(self)

        # image of the object
        self.images = []
        for image in images:
            self.images.append(pygame.image.load('../Resources/InteractableObjects/' + image +'.png'))

        self.displacement = 0

        if obj == "DOOR":
            offset = TILESIZE


        self.collision_type = collision_type

        self.index = 0
        self.current_image = self.images[self.index]

        # Position of the image
        self.rect = self.current_image.get_rect()
        self.rect.x = offset_x
        self.rect.y = offset_y


    def perform_action(self, player):
        if self.index == 1:
            self.index = 0
            self.collision_type = BLOCKING
        else:
            self.index = 1
            self.collision_type = OVERLAPPING
        self.current_image = self.images[self.index]

    def render(self, DISPLAYSURF):
        DISPLAYSURF.blit(self.current_image, (self.rect.x, self.rect.y))
