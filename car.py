import pygame
import os
import numpy as np
import math

CAR = pygame.image.load(os.path.join(os.getcwd(), "./images/car.png"))
CRASH = pygame.image.load(os.path.join(os.getcwd(), "./images/crash.png"))

# permet de réduire l'image unifomement plus tard
w = CAR.get_width()
h = CAR.get_height()



class Car(pygame.sprite.Sprite): #Utilisation de la classe "Sprite" du module "sprite". Car defined by extending Sprite
    
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        ###### Car's image and mask ######
        self.image = pygame.transform.scale(CAR, (w * 0.05, h * 0.05))
        self.crash = pygame.transform.scale(CRASH, (w * 0.1, h * 0.1))
        self.rect = self.image.get_rect(center=(x, y)) 
        # Creating the mask of the car. Useful for collision detection
        self.mask = pygame.mask.from_surface(self.image)
        
        ###### Car's properties ######
        # Car's position vector
        self.position = [x, y]
        # Car's velocity
        self.velocity = 0
        # Car's angle
        self.angle = 0
        
        
    ####### Car's methods - Car Physics #######
        
    def move(self):
        self.position[0] += self.velocity * math.cos(math.radians(self.angle))
        self.position[1] -= self.velocity * math.sin(math.radians(self.angle))   

    def turn_left(self):
        # If the car is moving forward, the angle increases by 5 degrees
        if self.velocity >= 0:
            self.angle += 2  
            # If the car is moving backward, the angle decreases by 5 degrees
        else:
            self.angle -= 2
    
    def turn_right(self):
        # Same here, but in the opposite direction
        if self.velocity >= 0:
            self.angle -= 2
        else:
            self.angle += 2
        
    def accelerate(self):
        self.velocity += 0.1
        
    def decelerate(self):
        self.velocity -= 0.1  
        
    def brake(self):
        if self.velocity >= 0.2:
            self.velocity -= 0.2
        elif self.velocity <= -0.2:
            self.velocity += 0.2    
        else:
            self.velocity = 0
        
        
        
    ####### Car's methods - Updating the car's position and mask #######
        
    def update(self):
        self.move()
        self.rect = self.image.get_rect(center=(self.position[0], self.position[1]))
        self.mask = pygame.mask.from_surface(self.image)
        
        
        
