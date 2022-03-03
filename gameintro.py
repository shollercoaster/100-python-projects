import pygame
pygame.init()

screen = pygame.display.set_mode([500, 500]) #setting up drawing window (width, length)

running = True
while running:
    
    #in case close button pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill((255, 255, 255)) #white bg specified as (r,g,b) values
    
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75) #blue circle first tuple: rgb values; second tuple: centre coordinates; radius
    
    pygame.display.flip()  #display
    
pygame.quit()
 
    