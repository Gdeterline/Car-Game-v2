import pygame
import os

CAR = pygame.image.load("car.png")

class Car(pygame.sprite.Sprite): #Utilisation de la classe "Sprite" du module "sprite". Car defined by extending Sprite
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path("car.png"))