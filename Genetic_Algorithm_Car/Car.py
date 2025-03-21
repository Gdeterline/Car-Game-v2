import pygame
import math
import numpy as np
import random as rd
from Track import Track
from NeuralNetwork import NeuralNetwork

CAR_PATH = "./Genetic_Algorithm_Car/assets/cars/car1.png"

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
        self.max_velocity = 4
        self.min_velocity = 1.5
        self.velocity = 2
        self.angle = 0

        self.sensors = []
        self.sensdist = []
        self.alive = True
        self.started = False
        self.driven_distance = 0
        
        self.nn = NeuralNetwork(5, 6, 2)

    ############# Collision Management + Sensors ##############

    def draw_sensor(self, sensor_surface: pygame.surface.Surface):
        for radar in self.sensors:
            center = radar[0]
            pygame.draw.line(sensor_surface, (0, 255, 0), self.center, center, 1)
            pygame.draw.circle(sensor_surface, (0, 255, 0), center, 2)

    def check_sensor(self, degree, screen: pygame.surface.Surface, OUTBOUND_COLOR):
        length = 0
        x = int(self.center[0] + math.cos(math.radians(360 - (self.angle + degree))) * length)
        y = int(self.center[1] + math.sin(math.radians(360 - (self.angle + degree))) * length)

        while not screen.get_at((x, y)) == OUTBOUND_COLOR and length < 200: # Sensor length = max(outbound dist, 200)
            length += 1
            x = int(self.center[0] + math.cos(math.radians(360 - (self.angle + degree))) * length)
            y = int(self.center[1] + math.sin(math.radians(360 - (self.angle + degree))) * length)

        distance = int(math.sqrt(math.pow(x - self.center[0], 2) + math.pow(y - self.center[1], 2)))
        self.sensors.append([(x, y), distance])
        self.sensdist.append(distance)

    def clear_sensors(self):
        self.sensors.clear()
        self.sensdist.clear()
        
    """ 
    def collision(self, screen: pygame.surface.Surface, OUTBOUND_COLOR):
        if (self.center[0] < 0 or self.center[0] >= screen.get_width() or
            self.center[1] < 0 or self.center[1] >= screen.get_height()):
            self.alive = False  # Car is dead if it's off-screen
        elif screen.get_at((int(self.center[0]), int(self.center[1]))) == OUTBOUND_COLOR:
            self.alive = False # Car is dead if it hits the track boundaries """
            
    def collision(self, screen: pygame.surface.Surface, OUTBOUND_COLOR):
        #print(f"Car center: {self.center}")
        pixel_color = screen.get_at((int(self.center[0]), int(self.center[1])))
        #print(f"Pixel color: {pixel_color}, OUTBOUND_COLOR: {OUTBOUND_COLOR}")
        #print(f"Screen dimensions: {screen.get_width()}, {screen.get_height()}")
        if (self.center[0] < 0 or self.center[0] >= screen.get_width() or
            self.center[1] < 0 or self.center[1] >= screen.get_height()):
            #print("Off-screen collision")
            self.alive = False
        elif pixel_color == OUTBOUND_COLOR:
            #print("Color collision detected!")
            self.alive = False
            
            
    def crossed_starting_line(self, screen: pygame.surface.Surface, starting_line_color):
        pixel_color = screen.get_at((int(self.center[0]), int(self.center[1])))
        if pixel_color == starting_line_color and self.driven_distance > 100:   # 100 is arbitrary
            return True
        return False
    
    def crossed_starting_line(self, screen: pygame.surface.Surface, starting_line_color):
        if self.started:
            buffer = 10 # add a buffer of 4 pixels.
            for x in range(int(self.center[0]) - buffer, int(self.center[0]) + buffer):
                for y in range(int(self.center[1]) - buffer, int(self.center[1]) + buffer):
                    pixel_color = screen.get_at((x, y))
                    if pixel_color == starting_line_color:
                        return True
        return False
    
    ############# Car Physics ############
    
    def decide_action(self, input): # Expecting a [[1, 1]] shape array
        n = np.round(input)
        if n[0][0] == 1 and n[0][1] == 1:
            self.accelerate()
        elif n[0][0] == 0 and n[0][1] == 0:
            self.decelerate()
        elif n[0][0] == 1 and n[0][1] == 0:
            self.turn_left()
        elif n[0][0] == 0 and n[0][1] == 1:
            self.turn_right()
    
    def move(self, input):
        self.decide_action(input)
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
        if self.velocity <= self.max_velocity:
            self.velocity += 0.1
        
    def decelerate(self):
        if self.velocity >= self.min_velocity + 0.1:
            self.velocity -= 0.1  

    def update(self, screen: pygame.surface.Surface, OUTBOUND_COLOR):
        input_data = np.array([self.sensdist])
        nn_output = self.nn.forward(input_data)
        self.move(nn_output)
        self.collision(screen, OUTBOUND_COLOR)
        self.driven_distance += self.velocity
        if self.driven_distance > 50:
            self.started = True
        self.rect = self.sprite.get_rect(center=(self.position[0], self.position[1]))