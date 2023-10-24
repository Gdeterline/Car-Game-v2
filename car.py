import pygame
import os
import sys
import numpy as np
import math

CAR = pygame.image.load(os.path.join(os.getcwd(), "./car.png"))

# permet de réduire l'image unifomement plus tard
w = CAR.get_width()
h = CAR.get_height()

x = 200
y = 200
class Car(pygame.sprite.Sprite): #Utilisation de la classe "Sprite" du module "sprite". Car defined by extending Sprite
    def __init__(self):
        super().__init__() #initialiser la classe
        self.image = pygame.transform.scale(CAR, (w * 0.1, h * 0.1))
        #genere rectangle de coordonnees (x, y) de la taille de self.image
        self.rect = self.image.get_rect(center=(x, y)) 
        #vecteur à dimensions de coordonnees (x, y) ; variable vitesse (= direction de la voiture)
        self.vel = pygame.math.Vector2(0, 0) 
        self.pos = pygame.math.Vector2(x, y)
        #variable pour l'angle
        self.steering = 0.0
        # variable pour l'accélération
        self.acc = 0.0
        # variable pour l'angle
        self.angle = 0.0
        
        self.rotated = pygame.transform.rotate(self.image, self.angle)
        
    # driving function
    def drive(self, dt):
        drive_keys = pygame.key.get_pressed()
        
        
        if drive_keys[pygame.K_UP]:
            self.acc += 1 * dt
            self.vel.x += self.acc * dt 
            print(self.vel) # Print keeps on displaying [0, 0]. Shouldn't. Should at least be [dt, 0] with value of dt instead.
            
            
        elif drive_keys[pygame.K_DOWN]:
            self.acc -= 1 * dt
            self.vel.x += self.acc * dt 
            
        else:
            self.acc = 0
            
        self.pos += self.vel
        self.rect.center = self.pos

        
        
            
    # steering function
    def steer(self, dt):
        steer_keys = pygame.key.get_pressed()
                
        if steer_keys[pygame.K_RIGHT] and self.steering:
            self.steering -= 30 * dt
            turning_radius = h / math.sin(math.radians(self.steering))
            angular_velocity = self.vel.x / turning_radius
        elif steer_keys[pygame.K_LEFT] and self.steering:
            self.steering += 30 * dt
            turning_radius = h / math.sin(math.radians(self.steering))
            angular_velocity = self.vel.x / turning_radius
        else:
            self.steering = 0
            angular_velocity = 0
        self.steering = max(-30, min(30, self.steering))
        
        self.pos += self.vel.rotate(-self.angle) * dt
        self.angle += math.degrees(angular_velocity) * dt
        
        self.rotated = pygame.transform.rotate(self.image, self.angle)
            
    # update driving and steering (which will depend on the user inputs)
    def update(self, dt):
        self.drive(dt)
        self.steer(dt)
        