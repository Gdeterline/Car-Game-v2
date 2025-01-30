import pygame
import math
from Track import Track

CAR_PATH = "./Genetic_Algorithm_Car/assets/cars/car.png"

class Car():

    CAR_WIDTH = 30
    CAR_HEIGHT = 15

    def __init__(self, starting_position: list):
        pygame.sprite.Sprite.__init__(self)
        car_image = pygame.image.load(CAR_PATH)
        self.sprite = pygame.transform.scale(car_image, (Car.CAR_WIDTH, Car.CAR_HEIGHT))        
        ###### Car's properties ######
        # Car's position vector
        self.position = starting_position
        # Car's velocity
        self.velocity = 0
        # Car's angle
        self.angle = 0

        self.sensors = []
        self.alive = True
        self.driven_distance = 0

    def update_car_position_test(self):
        return [self.position[0]+300, self.position[1]+300] 
    
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


