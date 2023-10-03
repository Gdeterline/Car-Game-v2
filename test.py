import pygame
import sys

clock = pygame.time.Clock()

LARGEUR = 1000 #dimension de l'image circuit
HAUTEUR = 600
ECRAN = pygame.display.set_mode((LARGEUR, HAUTEUR)) #Afficher l'ecran de jeu

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    