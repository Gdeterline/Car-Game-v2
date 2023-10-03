import pygame
import os

LARGEUR = 1000 #dimension de l'image circuit
HAUTEUR = 600
ECRAN = pygame.display.set_mode((LARGEUR, HAUTEUR)) #Afficher l'ecran de jeu

CIRCUIT = pygame.image.load("circuit.jpeg")
CAR = pygame.image.load("car.png")

class Car(pygame.sprite.Sprite): #Utilisation de la classe "Sprite" du module "sprite"
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path("car.png"))