import pygame
import os
import sys

CAR = pygame.image.load("car.png")

class Car(pygame.sprite.Sprite): #Utilisation de la classe "Sprite" du module "sprite". Car defined by extending Sprite
    def __init__(self):
        super().__init__() #initialiser la classe
        self.image = pygame.image.load(os.path("car.png"))
        #genere rectangle de coordonnees (x, y) de la taille de self.image
        self.rect = self.image.get_rect(center=(100, 100)) 
        #vecteur à dimensions de coordonnees (x, y) ; variable vitesse
        self.vel = pygame.math.Vector2(0, 0) 
        #initialisation d'une variable d'état
        self.drive_state = False 
        #variable pour l'angle
        self.angle = 0
        