import pygame
from car import Car
import math
import os

CAR = pygame.image.load(os.path.join(os.getcwd(), "./car.png"))

w = CAR.get_width()
h = CAR.get_height()


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
            
        elif drive_keys[pygame.K_DOWN]:
            self.car.acc -= 1 * dt
            self.car.vel.x += self.car.acc * dt 
            
        else:
            self.car.acc = 0
         
        # Physics managing moving direction   
        self.car.pos.x += self.car.vel.x * math.cos(math.radians(self.car.angle)) * dt * acc_offset
        self.car.pos.y -= self.car.vel.x * math.sin(math.radians(self.car.angle)) * dt * acc_offset
        self.car.rect.center = self.car.pos
        #print(self.car.pos) # Value changes rightfully. As expected.
                
        
    def steer(self, dt):
        drive_keys = pygame.key.get_pressed()
        if drive_keys[pygame.K_RIGHT]:
            self.car.steering -= 30 * dt
            #print(self.car.steering)
            turning_radius = h / math.sin(math.radians(self.car.steering))
            #print(turning_radius)
            angular_velocity = self.car.vel.x / turning_radius
            #print(angular_velocity)
            self.car.angle += math.degrees(angular_velocity) * dt * 100
        elif drive_keys[pygame.K_LEFT]:
            self.car.steering += 30 * dt
            turning_radius = h / math.sin(math.radians(self.car.steering))
            angular_velocity = self.car.vel.x / turning_radius
            self.car.angle += math.degrees(angular_velocity) * dt * 100 # *100 to make the car turn faster
        else:
            self.car.steering = 0
            angular_velocity = 0
            
            
            
        ########################################## Tryouts #################################################################################    
            
        #self.car.steering = max(-30, min(30, self.car.steering))
        #self.car.pos += self.car.vel.rotate(-self.car.angle) * dt
        #print(self.car.pos)
        #print(self.car.angle) # Value changes rightfully. As expected.
        #self.car.image = pygame.transform.rotate(self.car.image, self.car.angle)