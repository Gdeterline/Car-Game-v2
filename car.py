import pygame
import os
import sys
import numpy as np

CAR = pygame.image.load(os.path.join(os.getcwd(), "./car.png"))
class Car(pygame.sprite.Sprite): #Utilisation de la classe "Sprite" du module "sprite". Car defined by extending Sprite
    def __init__(self):
        super().__init__() #initialiser la classe
        self.image = pygame.transform.scale(CAR, (90, 50))
        #genere rectangle de coordonnees (x, y) de la taille de self.image
        self.rect = self.image.get_rect(center=(200, 200)) 
        #vecteur à dimensions de coordonnees (x, y) ; variable vitesse
        self.vel = pygame.math.Vector2(1, 0) 
        #variable pour l'angle
        self.angle = 0
        #vitesse de rotation
        self.angle_vel = 1.01
        
    # driving function
    def drive(self):
        drive_keys = pygame.key.get_pressed()
        if drive_keys[pygame.K_UP]:
            self.rect.x += self.vel[0] * 2
        elif drive_keys[pygame.K_DOWN]:
            self.rect.x -= self.vel[0] * 2    
            
    # steering function
    def steer(self):
        steer_keys = pygame.key.get_pressed()
        if steer_keys[pygame.K_RIGHT]:
            self.angle += self.angle_vel
            self.vel[1] = self.vel[1] + np.log(self.angle_vel)
            self.rect.y += self.vel[1] * 2
        elif steer_keys[pygame.K_LEFT]:
            self.angle += self.angle_vel
            self.vel[1] = self.vel[1] + np.log(self.angle_vel)
            self.rect.y -= self.vel[1] * 2
            
        #self.rect.center += self.vel * 2
        #self.rect.center = pygame.transform.rotate(self.image, self.angle)
        #self.image = pygame.transform.rotozoom(self.image, self.angle, 0.1)
        
    # update driving and steering (which will depend on the user inputs)
    def update(self):
        self.drive()
        self.steer()
    