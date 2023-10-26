import pygame
import os
import car
from driving import Driving
import math

# Initialising all pygame modules
pygame.init()

CAR = pygame.image.load(os.path.join(os.getcwd(), "./car.png"))


LARGEUR = 1000 #dimension de l'image circuit
HAUTEUR = 600

screen = pygame.display.set_mode((LARGEUR, HAUTEUR)) #Afficher l'ecran de jeu
CIRCUIT = pygame.image.load("./circuit.jpeg")

# Resising image so it fits right
CIRCUIT = pygame.transform.scale(CIRCUIT, (1000, 600))

clock = pygame.time.Clock()

car = car.Car()
driving = Driving()

# Run until user quits window
running = True
while running:
    dt = clock.tick(60) / 1000 
    
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

    w = CAR.get_width()
    h = CAR.get_height()
    
    
    driving.drive(dt)
    driving.steer(dt)
    
    
    # displays the car on the track
    
    new_image = pygame.transform.rotate(driving.car.image, driving.car.angle)
    rect = new_image.get_rect(center=driving.car.pos)
    screen.blit(new_image, rect)
    
    
    # update the display
    pygame.display.update()
    pygame.display.flip()
        
# Quit pygame when done playing
pygame.quit()
