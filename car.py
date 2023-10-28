import pygame
import os
import sys
import numpy as np
import math

CAR = pygame.image.load(os.path.join(os.getcwd(), "./car.png"))

# permet de réduire l'image unifomement plus tard
w = CAR.get_width()
h = CAR.get_height()

x = 200
y = 200
class Car(pygame.sprite.Sprite): #Utilisation de la classe "Sprite" du module "sprite". Car defined by extending Sprite
    def __init__(self):
        super().__init__() #initialiser la classe
        self.image = pygame.transform.scale(CAR, (w * 0.05, h * 0.05))
        #genere rectangle de coordonnees (x, y) de la taille de self.image
        self.rect = self.image.get_rect(center=(x, y)) 
        #vecteur à dimensions de coordonnees (x, y) ; variable vitesse (= direction de la voiture)
        self.vel = pygame.math.Vector2(0, 0) 
        self.pos = pygame.math.Vector2(x, y)
        #variable pour l'angle
        self.steering = 0.0
        # variable pour l'accélération
        self.acc = 0.0
        # variable pour le freinage
        self.brake_deceleration = 5.0
        # variable pour la décélération
        self.free_deceleration = 2.0
        # variable pour l'angle
        self.angle = 0.0
        # rotating the image
        self.rotated = pygame.transform.rotate(self.image, self.angle)
        

        
        
        
