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

vehicule = car.Car()

# Run until user quits window
running = True
while running:
    # check if user quits
    for event in pygame.event.get():
        # player quits the window
        if event.type == pygame.QUIT:
            running = False
        # does he click on a key ?
        elif event.type == pygame.KEYDOWN:
            # he clicks on the escape key
            if event.key == pygame.K_ESCAPE:
                running = False
    
    # Clear the screen to erase the drag of the car 
    screen.fill((0, 0, 0))

    # display race track on the screen with .blit()
    screen.blit(CIRCUIT, (0, 0))

    # check if driver starts driving the car (=vehicule)
    keys = pygame.key.get_pressed()   # use of pygame.key.get_pressed() because "listens" continuosly to keyboard
    if keys[pygame.K_UP]:
        # start driving
        vehicule.drive_state = True
    else:
        vehicule.drive_state = False
        
    # updating the position of the car
    vehicule.update()
    
    # displays the car on the track
    screen.blit(vehicule.image, vehicule.rect)
    
    # update the display
    pygame.display.update()
        
 
# Quit pygame when done playing
pygame.quit()
