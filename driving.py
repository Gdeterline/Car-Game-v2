import pygame
from car import Car
import math
import os

CAR = pygame.image.load(os.path.join(os.getcwd(), "./car.png"))

w = CAR.get_width()
h = CAR.get_height()

class Driving():
    def __init__(self):
        self.car = Car()
    
    
    def drive(self, dt):
        drive_keys = pygame.key.get_pressed()
        
        if drive_keys[pygame.K_UP]:
            self.car.acc += 1 * dt
            self.car.vel.x += self.car.acc * dt 
            #print(self.car.vel) # Value changes rightfully. As expected.
            
        elif drive_keys[pygame.K_DOWN]:
            self.car.acc -= 1 * dt
            self.car.vel.x += self.car.acc * dt 
            
        else:
            self.car.acc = 0
            
        self.car.pos += self.car.vel
        self.car.rect.center = self.car.pos
        #print(self.car.pos) # Value changes rightfully. As expected.
        
        
############################### steer() function needs to be tested. Easier when the image will be able to move. ########################################
        
        
    def steer(self, dt):
        drive_keys = pygame.key.get_pressed()
        if drive_keys[pygame.K_RIGHT]:
            self.car.steering -= 30 * dt
            print(self.car.steering)
            
            ### self.car.steering changes value. Good news. Need to debug what comes after and check the display ###
            
            turning_radius = h / math.sin(math.radians(self.car.steering))
            angular_velocity = self.car.vel.x / turning_radius
        elif drive_keys[pygame.K_LEFT]:
            self.car.steering += 30 * dt
            turning_radius = h / math.sin(math.radians(self.car.steering))
            angular_velocity = self.car.vel.x / turning_radius
        else:
            self.car.steering = 0
            angular_velocity = 0
        self.car.steering = max(-30, min(30, self.car.steering))
        
        self.car.pos += self.car.vel.rotate(-self.car.angle) * dt
        self.car.angle += math.degrees(angular_velocity) * dt
            
        self.car.rotated = pygame.transform.rotate(self.car.image, self.car.angle)