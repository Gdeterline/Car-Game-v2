import pygame
import os
import sys

CAR = pygame.image.load(os.path.join(os.getcwd(), "car.png"))

class Car(pygame.sprite.Sprite): #Utilisation de la classe "Sprite" du module "sprite". Car defined by extending Sprite
    def __init__(self):
        super().__init__() #initialiser la classe
        self.image = pygame.transform.scale(CAR, (200, 100))
        #genere rectangle de coordonnees (x, y) de la taille de self.image
        self.rect = self.image.get_rect(center=(200, 200)) 
        #vecteur à dimensions de coordonnees (x, y) ; variable vitesse
        self.vel = pygame.math.Vector2(1, 0) 
        #initialisation d'une variable d'état pour l'état de la partie/voiture
        self.drive_state = False 
        #variable pour l'angle
        self.angle = 0
        
    # driving function
    def drive(self):
        if self.drive_state == True :
            self.rect.center += self.vel * 2
            
    # steering function - for now we only added the rotozoom function which moves the image properly -
    def steer(self):
        self.image = pygame.transform.rotozoom(self.image, self.angle, 0.1)
        
    # update driving and steering (which will depend on the user inputs)
    def update(self):
        self.drive()
        #self.steer()
    