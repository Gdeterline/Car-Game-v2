import pygame
import math
import random as rd
from Track import Track

CAR_PATH = "./Genetic_Algorithm_Car/assets/cars/car.png"

class Car():

    CAR_WIDTH = 30
    CAR_HEIGHT = 15

    def __init__(self, starting_position: list):
        pygame.sprite.Sprite.__init__(self)
        car_image = pygame.image.load(CAR_PATH)
        self.sprite = pygame.transform.scale(car_image, (Car.CAR_WIDTH, Car.CAR_HEIGHT))  
        self._sprite = self.sprite  

        self.position = starting_position
        self.center = starting_position
        self.velocity = 0
        self.angle = 0

        self.sensors = []
        self.alive = True

        self.driven_distance = 0

    ############# Collision Management + Sensors ##############

    def draw_sensor(self, screen):
        for radar in self.sensors:
            center = radar[0]
            pygame.draw.line(screen, (0, 255, 0), self.center, center, 1)
            pygame.draw.circle(screen, (0, 255, 0), center, 2)

    def check_sensor(self, degree, screen: pygame.surface.Surface, OUTBOUND_COLOR):
        length = 0
        x = int(self.center[0] + math.cos(math.radians(360 - (self.angle + degree))) * length)
        y = int(self.center[1] + math.sin(math.radians(360 - (self.angle + degree))) * length)

        while not screen.get_at((x, y)) == OUTBOUND_COLOR and length < 100: # Sensor length = max(outbound dist, 300)
            length += 1
            x = int(self.center[0] + math.cos(math.radians(360 - (self.angle + degree))) * length)
            y = int(self.center[1] + math.sin(math.radians(360 - (self.angle + degree))) * length)

        distance = int(math.sqrt(math.pow(x - self.center[0], 2) + math.pow(y - self.center[1], 2)))
        self.sensors.append([(x, y), distance])

    def clear_sensors(self):
        self.sensors.clear()

    def collision(self, screen: pygame.surface.Surface, OUTBOUND_COLOR):
        if screen.get_at((int(self.center[0]), int(self.center[1]))) == OUTBOUND_COLOR:
            self.alive = False

    ############# Car Physics ############
    
    def decide_action(self):
        n = rd.randint(0, 1)
        if n == 0:
            self.accelerate()
        elif n == 1:
            self.decelerate()

    
    def move(self):
        self.decide_action()
        self.position[0] += self.velocity * math.cos(math.radians(self.angle))
        self.position[1] -= self.velocity * math.sin(math.radians(self.angle)) 
        self.center = [self.position[0], self.position[1]]

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
        if self.velocity >= 0.1:
            self.velocity -= 0.1  

    def update(self, screen: pygame.surface.Surface, OUTBOUND_COLOR):
        self.move()
        self.collision(screen, OUTBOUND_COLOR)
        self.driven_distance += self.velocity
        self.rect = self.sprite.get_rect(center=(self.position[0], self.position[1]))

    def reset(self):
        self.angle = 0
        self.velocity = 0
        self.alive = True
        self.driven_distance = 0
        self.sensors.clear()
        self.position = Track.get_starting_position()