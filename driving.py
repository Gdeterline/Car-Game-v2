import pygame
from car import Car
from math import cos, sin, radians, degrees, copysign
import os
import tkinter as tk
from tkinter import messagebox

CAR = pygame.image.load(os.path.join(os.getcwd(), "./car.png"))

w = CAR.get_width()
h = CAR.get_height()

pygame.mixer.init()
accelerate_sound = pygame.mixer.Sound("./car_acc_sound.mp3")
breaking_sound = pygame.mixer.Sound("./car_break_sound.mp3")
reverse_sound = pygame.mixer.Sound("./car_rev_sound.mp3")


################################## All #prints(.) were tests. All functional #####################################################################


class Driving():
    def __init__(self):
        self.car = Car()
            
    
    def drive(self, dt):
        acc_offset = 10 # Useful to make the car move faster (too slow otherwise)
        drive_keys = pygame.key.get_pressed()
        
        if drive_keys[pygame.K_UP]:
            self.car.acc += 1 * dt
            self.car.vel.x += self.car.acc * dt 
            #print(self.car.vel) # Value changes rightfully. As expected.
            reverse_sound.stop()
            accelerate_sound.play()

            
        elif drive_keys[pygame.K_DOWN]:
            self.car.acc -= 1 * dt
            self.car.vel.x += self.car.acc * dt
            accelerate_sound.stop()
            reverse_sound.play()
            
            
        elif drive_keys[pygame.K_SPACE]: 
            #tant que la voiture dépasse une vitesse trop importante, elle décélère selon la valeur de brake_deceleration
            if abs(self.car.vel.x) > self.car.brake_deceleration * dt:
                #appel de la fonction copysign pour gèrer le signe de la deceleration
                self.car.acc = -copysign(self.car.brake_deceleration, self.car.vel.x) # check if going rear bug comes from here
                self.car.vel.x += self.car.acc * dt * 5 # *5 to make the car brake faster
                
            #sinon, elle décélère proportionnellement à sa vitesse jusqu'à s'arrêter
            else:
                self.car.acc = -self.car.vel.x / dt
                self.car.vel.x += self.car.acc * dt 
            accelerate_sound.stop()
            reverse_sound.stop()
            breaking_sound.play()
        
        #simuler les frottements de l'air / frottements mécaniques / pertes d'energie quelconques 
        #meme méthode que pour le freinage avec un coefficient de décélération différent
        else:
            if abs(self.car.vel.x) > self.car.free_deceleration * dt:
                self.car.acc = -copysign(self.car.free_deceleration, self.car.vel.x)
                self.car.vel.x += self.car.acc * dt
            else:
                self.car.acc = -self.car.vel.x / dt
                self.car.vel.x += self.car.acc * dt
                
        # Physics managing moving direction   
        self.car.pos.x += self.car.vel.x * cos(radians(self.car.angle)) * dt * acc_offset
        self.car.pos.y -= self.car.vel.x * sin(radians(self.car.angle)) * dt * acc_offset
        self.car.rect.center = self.car.pos
        print(self.car.pos)
        #print(self.car.pos) # Value changes rightfully. As expected.
                
        
    def steer(self, dt):
        drive_keys = pygame.key.get_pressed()
        if drive_keys[pygame.K_RIGHT]:
            self.car.steering -= 30 * dt
            #print(self.car.steering)
            turning_radius = h / sin(radians(self.car.steering))
            #print(turning_radius)
            angular_velocity = self.car.vel.x / turning_radius
            #print(angular_velocity)
            self.car.angle += degrees(angular_velocity) * dt * 100
        elif drive_keys[pygame.K_LEFT]:
            self.car.steering += 30 * dt
            turning_radius = h / sin(radians(self.car.steering))
            angular_velocity = self.car.vel.x / turning_radius
            self.car.angle += degrees(angular_velocity) * dt * 100 # *100 to make the car turn faster
        else:
            self.car.steering = 0
            angular_velocity = 0
            
    
           
           
    def collide(self):
        if self.car.pos.x > 245 and self.car.pos.x < 755 and self.car.pos.y > 140 and self.car.pos.y < 460 :
            return False
        elif self.car.pos.x > 895 and self.car.pos.x < 105 and self.car.pos.y > 535 and self.car.pos.y < 65 :
            return False
        return True
    
        
        
            
            
        ########################################## Tryouts #################################################################################    
            
        #self.car.steering = max(-30, min(30, self.car.steering))
        #self.car.pos += self.car.vel.rotate(-self.car.angle) * dt
        #print(self.car.pos)
        #print(self.car.angle) # Value changes rightfully. As expected.
        #self.car.image = pygame.transform.rotate(self.car.image, self.car.angle)