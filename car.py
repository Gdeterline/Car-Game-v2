import pygame
import os
import sys
import numpy as np

CAR = pygame.image.load(os.path.join(os.getcwd(), "./car.png"))
# permet de réduire l'image unifomement plus tard
w = CAR.get_width()
h = CAR.get_height()

class Car(pygame.sprite.Sprite): #Utilisation de la classe "Sprite" du module "sprite". Car defined by extending Sprite
    def __init__(self):
        super().__init__() #initialiser la classe
        self.image = pygame.transform.scale(CAR, (w * 0.1, h * 0.1))
        #genere rectangle de coordonnees (x, y) de la taille de self.image
        self.rect = self.image.get_rect(center=(200, 200)) 
        #vecteur à dimensions de coordonnees (x, y) ; variable vitesse = direction de la voiture
        self.vel = pygame.math.Vector2(1, 0) 
        #variable pour l'angle
        self.angle = 0
        #vitesse de rotation
        self.angle_vel = 1
        
        
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
        
 # test déplacement / rotation avec K_RIGHT       
        if steer_keys[pygame.K_RIGHT]:
            self.angle += self.angle_vel
            
            self.image2 = pygame.transform.rotate(self.image, -self.angle/10)
            
            #self.rect.y += self.vel[0] * 2
            #self.vel[1] = self.vel[1] + self.angle_vel
            #self.vel.rotate_ip(self.angle_vel)
            
# test vitesse / vecteur avec K_LEFT
        elif steer_keys[pygame.K_LEFT]:
            self.angle -= self.angle_vel
            
            self.rect.y -= self.vel[0] * 2
            
            #self.image = pygame.transform.rotate(self.image, +self.angle/3)
            #self.vel[1] = self.vel[1] + self.angle_vel
            #self.vel.rotate_ip(-self.angle_vel)
            
        #self.image = pygame.transform.rotozoom(self.image, self.angle, 0.1)
        #self.rect = self.image.get_rect(center = self.rect.center)
        
    # update driving and steering (which will depend on the user inputs)
    def update(self):
        self.drive()
        self.steer()
    