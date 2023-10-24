import pygame
import os
import car

# Initialising all pygame modules
pygame.init()


LARGEUR = 1000 #dimension de l'image circuit
HAUTEUR = 600

screen = pygame.display.set_mode((LARGEUR, HAUTEUR)) #Afficher l'ecran de jeu
CIRCUIT = pygame.image.load("./circuit.jpeg")

# Resising image so it fits right
CIRCUIT = pygame.transform.scale(CIRCUIT, (1000, 600))

car = car.Car()

# Run until user quits window
running = True
while running:
    dt = pygame.time.Clock().get_time() / 1000 
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_ESCAPE:
                running = False
    
    # Clear the screen to erase the drag of the car 
    screen.fill((0, 0, 0))

    # display race track on the screen with .blit()
    screen.blit(CIRCUIT, (0, 0))

    # updating the position of the car
    car.update(dt)
    
    # displays the car on the track
    
    screen.blit(car.rotated, car.rect)
    
    # update the display
    pygame.display.update()
    pygame.display.flip()
        
# Quit pygame when done playing
pygame.quit()
