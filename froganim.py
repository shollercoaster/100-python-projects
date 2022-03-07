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
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400

class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        self.sprites.append(pygame.image.load('attack_1.png'))
        self.sprites.append(pygame.image.load('attack_2.png'))
        self.sprites.append(pygame.image.load('attack_3.png'))
        self.sprites.append(pygame.image.load('attack_4.png'))
        self.sprites.append(pygame.image.load('attack_5.png'))
        self.sprites.append(pygame.image.load('attack_6.png'))
        self.sprites.append(pygame.image.load('attack_7.png'))
        self.sprites.append(pygame.image.load('attack_8.png'))
        self.sprites.append(pygame.image.load('attack_9.png'))
        self.sprites.append(pygame.image.load('attack_10.png'))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
        
    def animate(self):
        self.is_animating = True
    
    def update(self):
        if self.is_animating == True:
            self.current_sprite += 1

            #creating condition to end loop
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False

            self.image = self.sprites[int(self.current_sprite)]
        

        


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT]) 
pygame.display.set_caption("Sprite Animation")

moving_sprites = pygame.sprite.Group()
player = Player (100,100)
moving_sprites.add(player)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            player.animate()
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
            pygame.quit()
            sys.exit()
            
        screen.fill((255,255,155))
        moving_sprites.draw(screen)
#        moving_sprites.animate()
        moving_sprites.update()
        
        pygame.display.flip()
        clock.tick(60)
