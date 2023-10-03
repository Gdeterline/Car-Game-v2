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
                
    # display image on the screen with .blit()
    screen.blit(CIRCUIT, (0, 0))
    pygame.display.flip()
    

# Quit pygame when done playing
pygame.quit()
