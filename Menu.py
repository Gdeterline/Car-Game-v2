## Class Menu

import pygame
import os
from car import Car
from Player import Player
from CollisionManager import CollisionManager

pygame.init()
pygame.font.init()




## This class creates a menu that is used to select the racetrack and the number of laps to be played
class Menu():
    RACETRACK1 = pygame.image.load(os.path.join(os.getcwd(), "./images/circuit.jpeg"))
    RACETRACK1 = pygame.transform.rotate(RACETRACK1, 180)
    RACETRACK1 = pygame.transform.scale(RACETRACK1, (1000, 700))
    RACETRACK2 = pygame.image.load(os.path.join(os.getcwd(), "./images/circuit2.png"))
    RACETRACK2 = pygame.transform.scale(RACETRACK2, (1000, 600))
    RACETRACK3 = pygame.image.load(os.path.join(os.getcwd(), "./images/rect_racetrack.jpg"))
    RACETRACK3 = pygame.transform.scale(RACETRACK3, (1000, 600))
    
    def __init__(self, screen):
        pygame.init()
        pygame.font.init()
        self.screen = screen
        self.background = pygame.image.load(os.path.join(os.getcwd(), "./images/menu_background.webp"))
        self.scaled_background = pygame.transform.scale(self.background, (1000, 600))
        self.selected_circuit = None
        self.laps = None
        self.initial_position = (0, 0)
        
        
    def display_menu(self):
        # Display the scaled background image
        self.screen.blit(self.scaled_background, (0, 0))

        # Display menu options and selected circuit
        font = pygame.font.Font(None, 36)
        text = font.render("Menu:", True, (255, 255, 255))
        self.scaled_background.blit(text, (50, 50))

        text = font.render("a. Circuit A - Easy", True, (255, 255, 255))
        self.scaled_background.blit(text, (50, 100))

        text = font.render("b. Circuit B - Medium", True, (255, 255, 255))
        self.scaled_background.blit(text, (50, 150))

        text = font.render("c. Circuit C - Hard", True, (255, 255, 255))
        self.scaled_background.blit(text, (50, 200))
        
        text = font.render("Select number of laps (1-5)", True, (255, 255, 255))
        self.scaled_background.blit(text, (50, 350))

        if self.selected_circuit is not None:
            if self.selected_circuit == self.RACETRACK1:
                text = font.render("Selected Circuit: A (Easy)", True, (255, 255, 255))
                self.scaled_background.blit(text, (50, 250))
                
            elif self.selected_circuit == self.RACETRACK3:
                text = font.render("Selected Circuit: B - (Medium)", True, (255, 255, 255))
                self.scaled_background.blit(text, (50, 250))
                
            elif self.selected_circuit == self.RACETRACK2:
                text = font.render("Selected Circuit: C - (Hard)", True, (255, 255, 255))
                self.scaled_background.blit(text, (50, 250))
                
        if self.laps is not None:
            text = font.render("Number of laps selected: " +  str(self.laps), True, (255, 255, 255))
            self.scaled_background.blit(text, (50, 400))

        pygame.display.flip()
        pygame.time.wait(500)


    def racetrack_input(self):
        # Handle user input to select a circuit
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.selected_circuit = self.RACETRACK1
                    self.initial_position = (454, 134) # Initial position for the lower car in circuit A
                    #print("Selected circuit: ", self.selected_circuit)
                    return self.selected_circuit
                elif event.key == pygame.K_c:
                    self.selected_circuit = self.RACETRACK2
                    self.initial_position = (624, 235) # Initial position for the lower car in circuit C
                    return self.selected_circuit
                elif event.key == pygame.K_b:
                    self.selected_circuit = self.RACETRACK3
                    self.initial_position = (502, 91) # Initial position for the lower car in circuit B
                    return self.selected_circuit
                
                    
    def select_laps(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:                
                if pygame.K_1 <= event.key <= pygame.K_5:
                    self.laps = int(pygame.key.name(event.key))
                    #print("Laps: ", self.laps)
                    return self.laps   