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
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Player(pygame.sprite.Sprite):
    def __init__(self, width, height, pos_x, pos_y, color):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
        
pygame.init()
clock = pygame.time.Clock()

#called a display surface
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT]) 

second_surface = pygame.Surface((50, 50))
second_surface.fill((0, 0, 139))

#image gets imported on its own individual surface
cool_guy = pygame.image.load('Emraan-Hashmi.jpg') 

#encloses surface into rectangle and lets us get its attributes
rect = cool_guy.get_rect() 

print (rect.w)
print (rect.topleft) #gives (0,0) cause rect is relative to surface

#player
player = Player(50,50,100,100, (255, 255, 255))
player_group = pygame.sprite.Group()
player_group.add(player)

running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
        
    screen.fill((255, 87, 51))
    
    #puts this surface on top of the display surface
    screen.blit(second_surface, (SCREEN_WIDTH/10, SCREEN_HEIGHT/10)) 
    
    screen.blit(cool_guy, rect) #now moving rect means moving img
    
    rect.right += 5 #doesnt move image, only moves rectangle around it
    
    print (rect.right) #but coordinates keep increasing
    player_group.draw(screen)
    pygame.display.flip()
    
    #specifies how fast the flip() command is to be run; aka controlling the framerate
    clock.tick(60) 

