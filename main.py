import pygame
import os

LARGEUR = 1500 #dimension de l'image circuit
HAUTEUR = 1000

ECRAN = pygame.display.set_mode((LARGEUR, HAUTEUR)) # Afficher l'ecran de jeu


CIRCUIT = pygame.image.load("circuit.png")
CAR = pygame.image.load("car.png")
