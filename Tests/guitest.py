import pygame

pygame.init()

w, h = 900, 550
DISPLAYSURF = pygame.display.set_mode((w, h))


health = 100
heat = 100

#colors
red = (255, 0, 0)
green = (0, 255, 0)

def healthy():
    #displays 'health'
    Font1 = pygame.font.SysFont('monaco', 24)
    healthSurface = Font1.render('Health: {0}%'.format(health), True, green)
    healthRect = healthSurface.get_rect()
    healthRect.midtop = (200, 20)
    DISPLAYSURF.blit(healthSurface,healthRect)
def heated():
    #displays 'heat'
    Font2 = pygame.font.SysFont('monaco', 24)
    heatSurface = Font2.render('Heat: {0}%'.format(heat), True, green)
    heatRect = heatSurface.get_rect()
    heatRect.midtop = (192, 45)
    DISPLAYSURF.blit(heatSurface,heatRect)

while True:
    DISPLAYSURF.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # This relies on the previous line being called, or else it won't update,
    key_pressed = pygame.key.get_pressed()
    #checks what key is pressed to change health-- which then decides the size of the rectangle and color
    if key_pressed[pygame.K_x] and health > 0:
        health -= 0.1
    if key_pressed[pygame.K_z] and health < 100:
        health += 0.1
    #checks what key is pressed to change heat-- which then decides the size of the rectangle and color

    if key_pressed[pygame.K_v] and heat > 0:
        heat -= 0.1
    if key_pressed[pygame.K_c] and heat < 100:
        heat += 0.1

    # *2.55 because it ranges from 0-100, and 255 is color max
    tint = 255 - (health * 2.55)
    pygame.draw.rect(DISPLAYSURF, (tint, 255 - tint, 0), pygame.Rect(20, 20, health, 20))

    tint1 = 255 - (heat * 2.55)
    pygame.draw.rect(DISPLAYSURF, (255 - tint1, tint1, 0), pygame.Rect(20, 45, heat, 20))
    
 
 
    healthy()
    heated()
    pygame.display.flip()

