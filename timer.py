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
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT]) 

current_time = 0
button_press_time = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            button_press_time = pygame.time.get_ticks()
            screen.fill((255,255,255))
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
            pygame.quit()
            sys.exit()
    
    current_time = pygame.time.get_ticks()
    
    if current_time - button_press_time > 2000:
        screen.fill((0,0,0))
    
    print(f"current time: {current_time} button press time: {button_press_time}")
    pygame.display.flip()
    clock.tick(60)