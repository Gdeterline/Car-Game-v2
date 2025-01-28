import pygame
import numpy as np
import math
import os
import sys
current_directory = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current_directory)
sys.path.append(parent_directory)

from car import Car
from CollisionManager import CollisionManager


pygame.init()

## Set up the screen ##
LARGEUR = 1000
HAUTEUR = 600

## Load the car and the racetrack images ##
CAR1 = pygame.image.load(os.path.join(os.getcwd(), "./images/car.png"))
w = CAR1.get_width()
h = CAR1.get_height()

fontlapsP1P2 = pygame.font.Font(None, 20)

offset_initial_position = 30

class AIGameLoop():
    def __init__(self):
        pygame.init()
        
        self.selected_circuit = pygame.image.load(os.path.join(os.getcwd(), "./images/circuit.jpeg"))
        self.selected_circuit = pygame.transform.rotate(self.selected_circuit, 180)
        self.selected_circuit = pygame.transform.scale(self.selected_circuit, (1000, 700))
        
        # Starting line
        self.xinit = 454
        self.yinit = 134
        
        # Flag to determine number of laps
        self.x1 = 0
        
        self.lapsP1 = 0
        self.laps = 3
        
        self.screen = pygame.display.set_mode((LARGEUR, HAUTEUR))
        self.car1 = Car(self.xinit, self.xinit, CAR1)   # Probably don't need the x and y at first if we have the set_state method
        
        #self.car1.set_state(self.xinit, self.yinit, 0, 0)
        
        self.collision_manager1 = CollisionManager(self.car1, self.selected_circuit)
        
    def reset_car_state(self):
        self.car1.position = [self.xinit, self.yinit, 0, 0]
        
    def run_game(self):
        pygame.init()
        clock = pygame.time.Clock()
        running = True
        while running:
            
            # FPS limit
            clock.tick(60)
            
            ## Update car accordingly to the player 1 inputs ## 
            action = None
            self.car1.apply_action(action)
            self.car1.update()
            
            if self.lapsP1 == self.laps:
                print("Player 1 wins")
                
            if self.car1.position[0] < self.xinit - offset_initial_position :
                self.x1 = 1
                
            if self.car1.position[0] > self.xinit and self.x1 == 1:
                self.lapsP1 += 1
                self.x1 = 0
                
            self.screen.fill((0, 0, 0))

            # display race track on the screen with .blit()
            self.screen.blit((self.selected_circuit), (0, 0))
            
            # displays the car on the track
            new_image = pygame.transform.rotate(self.car1.image, self.car1.angle)
            rect = new_image.get_rect(center=self.car1.position)
            self.screen.blit(new_image, rect)
            
            lapsP1txt = fontlapsP1P2.render("Laps P1 : " + str(self.lapsP1), True, (255, 255, 255))
            
            self.screen.blit(lapsP1txt, (5, 5))

            pygame.display.flip()
            
            ## Check for quiting events ##
            for event in pygame.event.get():
                    
                if event.type == pygame.QUIT:
                    running = False
                    break
                
                elif event.type == pygame.KEYDOWN:
                    
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        break
                    
                    
game = AIGameLoop()
game.run_game()
pygame.quit()