## Class Menu

import pygame
import os
from Car import Car
from Player import Player
from CollisionManager import CollisionManager

## This class creates a menu that is used to select the racetrack and the number of laps to be played
class Menu():
    def __init__(self, screen):
        self.screen = screen
        self.background = pygame.image.load(os.path.join(os.getcwd(), "menu_background.webp"))
        self.scaled_background = pygame.transform.scale(self.background, (1000, 600))
        self.selected_circuit = None
        self.laps = None
        
        
    def display_menu(self):
        # Display the scaled background image
        self.screen.blit(self.scaled_background, (0, 0))

        # Display menu options and selected circuit
        font = pygame.font.Font(None, 36)
        text = font.render("Menu:", True, (255, 255, 255))
        self.scaled_background.blit(text, (50, 50))

        text = font.render("1. Circuit A", True, (255, 255, 255))
        self.scaled_background.blit(text, (50, 100))

        text = font.render("2. Circuit B", True, (255, 255, 255))
        self.scaled_background.blit(text, (50, 150))

        text = font.render("3. Circuit C", True, (255, 255, 255))
        self.scaled_background.blit(text, (50, 200))

        if self.selected_circuit is not None:
            text = font.render("Selected Circuit: " + self.selected_circuit, True, (255, 255, 255))
            self.scaled_background.blit(text, (50, 250))
            
        pygame.display.flip()

    def menu_input(self):
        # Handle user input to select a circuit
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    self.selected_circuit = "circuit.jpeg"
                elif event.key == pygame.K_2:
                    self.selected_circuit = "circuit2.jpeg"
                elif event.key == pygame.K_3:
                    self.selected_circuit = "rect_racetrack.jpg"
                    
    def select_laps(self):
        # Prompt the player to choose the number of laps
        font = pygame.font.Font(None, 36)
        text = font.render("Select number of laps (1-5):", True, (255, 255, 255))
        self.scaled_background.blit(text, (50, 300))
        pygame.display.flip()

        laps = None
        while laps is None:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if pygame.K_1 <= event.key <= pygame.K_5:
                        laps = int(pygame.key.name(event.key))
        return laps
            
            
            
        