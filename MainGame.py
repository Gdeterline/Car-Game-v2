import pygame
import numpy as np
import math
import os
from Car import Car
from Player import Player
from CollisionManager import CollisionManager

## Set up the screen ##
LARGEUR = 1000
HAUTEUR = 600
screen = pygame.display.set_mode((LARGEUR, HAUTEUR))


## Load the car and the racetrack images ##
CAR = pygame.image.load(os.path.join(os.getcwd(), "./car.png"))
w = CAR.get_width()
h = CAR.get_height()

RACETRACK = pygame.image.load(os.path.join(os.getcwd(), "circuit2.jpeg"))
RACETRACK = pygame.transform.scale(RACETRACK, (1000, 600))


## Main game class

class MainGame():
    def __init__(self):
        self.car1 = Car()
        self.car2 = Car()
        self.player1 = Player(self.car1, {'left': pygame.K_LEFT, 'right': pygame.K_RIGHT, 'up': pygame.K_UP, 'down': pygame.K_DOWN, 'brake': pygame.K_SPACE})
        self.player2 = Player(self.car2, {'left': pygame.K_q, 'right': pygame.K_d, 'up': pygame.K_z, 'down': pygame.K_s, 'brake': pygame.K_x})
        self.collision_manager1 = CollisionManager(self.car1, RACETRACK)
        self.collision_manager2 = CollisionManager(self.car2, RACETRACK)
    
    def run(self):
        pygame.init()
        clock = pygame.time.Clock()
        running = True
        while running:
            
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                
                elif event.type == pygame.KEYDOWN:
                    
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        pygame.quit()
                
            self.player1.ingame_inputs()
            self.player1.car.update()
            
            """ print("Velocity P1: ", self.player1.car.velocity)
            print()
            print("Position vector P1: ", self.player1.car.position)
            print()
            print("Angle P1: ", self.player1.car.angle) """
            
            self.player2.ingame_inputs()
            self.player2.car.update()
            
            """ print("Velocity P2: ", self.player2.car.velocity)
            print()
            print("Position vector P2: ", self.player2.car.position)
            print()
            print("Angle P2: ", self.player2.car.angle) """
            
            # Check for collisions
            if self.collision_manager1.check_boundary_collision(car=self.player1.car):
                print("Collision P1")
                # Raise an exception to stop the game
                raise Exception("Player 1 has collided with the boundary")

                
            if self.collision_manager2.check_boundary_collision(car=self.player2.car):  
                print("Collision P2")
                # Raise an exception to stop the game
                raise Exception("Player 2 has collided with the boundary")
                    
            
            
            clock.tick(60)
                    
            # Clear the screen to erase the drag of the car 
            screen.fill((0, 0, 0))

            # display race track on the screen with .blit()
            screen.blit((RACETRACK), (0, 0))
            
            # displays the car on the track
            new_image = pygame.transform.rotate(self.player1.car.image, self.player1.car.angle)
            rect = new_image.get_rect(center=self.player1.car.position)
            screen.blit(new_image, rect)
            
            new_image = pygame.transform.rotate(self.player2.car.image, self.player2.car.angle)
            rect = new_image.get_rect(center=self.player2.car.position)
            screen.blit(new_image, rect)
            
            # update the display
            pygame.display.flip()
            

            
game = MainGame()
game.run()
pygame.quit()