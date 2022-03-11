import pygame, sys
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()
clock = pygame.time.Clock()
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT]) 

moving_rect = pygame.Rect(350,350,100,100)
x_speed, y_speed = 5, 4

other_rect= pygame.Rect (300, 550, 150, 50)
other_speed = 2

def bouncing_rect():
    global x_speed, y_speed, other_speed
    moving_rect.x += x_speed
    moving_rect.y += y_speed
#    other_rect.x += other_speed
    
    #collision with screen borders
    if moving_rect.right >= SCREEN_WIDTH or moving_rect.left <= 0:
        x_speed *= -1
    if moving_rect.bottom >= SCREEN_HEIGHT or moving_rect.top <= 0:
        y_speed *= -1
#    if other_rect.right >= SCREEN_WIDTH or other_rect.left <= 0:
#        other_speed *= -1
        
    #collision with rect
    collision_tolerance = 10
    if moving_rect.colliderect(other_rect):
        if abs(other_rect.top - moving_rect.bottom) <= collision_tolerance and y_speed > 0:
            y_speed *= -1
        if abs(other_rect.right - moving_rect.left) <= collision_tolerance and x_speed < 0:
            x_speed *= -1
        if abs(other_rect.bottom - moving_rect.top) <= collision_tolerance and y_speed < 0:
            y_speed *= -1
        if abs(other_rect.left - moving_rect.right) <= collision_tolerance and x_speed > 0:
            x_speed *= -1
        
    
    pygame.draw.rect(screen, (255,255,255), moving_rect)
    pygame.draw.rect(screen, (155,200,55), other_rect)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                other_rect.left += -50
            if event.key == pygame.K_RIGHT:
                other_rect.right += 50
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
            pygame.quit()
            sys.exit()
    
    screen.fill((30,30,30))
    bouncing_rect()
    pygame.display.flip()
    clock.tick(60)