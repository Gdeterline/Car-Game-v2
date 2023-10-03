import pygame
import os

LARGEUR = 1000 #dimension de l'image circuit
HAUTEUR = 600
ECRAN = pygame.display.set_mode((LARGEUR, HAUTEUR)) #Afficher l'ecran de jeu

CIRCUIT = pygame.image.load("circuit.jpeg")
CAR = pygame.image.load("car.png")

