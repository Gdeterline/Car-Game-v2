import pygame
import os
import numpy as np
import math

CAR1 = pygame.image.load(os.path.join(os.getcwd(), "./images/car.png"))
CRASH = pygame.image.load(os.path.join(os.getcwd(), "./images/crash.png"))

# permet de réduire l'image unifomement plus tard
w1 = CAR1.get_width()
h1 = CAR1.get_height()


class Car(pygame.sprite.Sprite): #Utilisation de la classe "Sprite" du module "sprite". Car defined by extending Sprite
    
    def __init__(self, x, y, car_image):
        pygame.sprite.Sprite.__init__(self)
        
        ###### Car's image and mask ######
        self.image = pygame.transform.scale(car_image, (w1 * 0.05, h1 * 0.05))
        
        self.crash = pygame.transform.scale(CRASH, (w1 * 0.1, h1 * 0.1))
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
        
        self.state = [self.position, self.velocity, self.angle]
        
        
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
        if self.velocity <= 5:
            self.velocity += 0.1
        
    def decelerate(self):
        if self.velocity >= -2:
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
        #print("Position vector: ", self.position)
    
    def set_state(self, x, y, velocity, angle):
        self.state = [[x, y], velocity, angle]
        
    def get_state(self):
        return self.state
    
    def apply_action(self, action):
        # The values attributed to each action are arbitrary - the model just learns and goes on with the values
        if action == '0':   # accelerate
            self.accelerate()
        elif action == '1': # decelerate
            self.decelerate
        elif action == '2': # brake
            self.brake
        elif action == '3': # turn left
            self.turn_left
        elif action == '4': # turn right
            self.turn_right
        else:
            return False
            
            
        
        
