import pygame, sys
import random
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Player(pygame.sprite.Sprite):
    def __init__(self, picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
    def shoot(self):
        pygame.sprite.spritecollide(player, target_group, True)
    def update(self):
        self.rect.center = pygame.mouse.get_pos()
        
class Target(pygame.sprite.Sprite):
    def __init__(self, picture_path, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x,pos_y]
        
pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT]) 
background = pygame.image.load("bg.png")
pygame.mouse.set_visible(False)

#player
player = Player("crosshair_red_large.png")
player_group = pygame.sprite.Group()
player_group.add(player)

#target
target_group = pygame.sprite.Group()
for target in range(20):
    new_target = Target("target_colored.png", random.randrange(0, SCREEN_WIDTH), random.randrange(0, SCREEN_HEIGHT))
    target_group.add(new_target)

running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            player.shoot()
        elif event.type == QUIT:
            running = False
    #order of drawing matters; python draws neeche wala stuff on top   
    pygame.display.flip()
    screen.blit(background, (0,0))
    target_group.draw(screen)
    player_group.draw(screen)
    player_group.update()
    
    
    #specifies how fast the flip() command is to be run; aka controlling the framerate
    clock.tick(60) 

