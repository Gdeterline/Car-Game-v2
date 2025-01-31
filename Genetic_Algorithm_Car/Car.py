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
        self.center = starting_position
        # Car's velocity
        self.velocity = 0
        # Car's angle
        self.angle = 0

        self.sensors = []

        self.alive = True
        self.driven_distance = 0

    def draw_sensor(self, screen):
        for radar in self.sensors:
            position = radar[0]
            pygame.draw.line(screen, (0, 255, 0), self.position, position, 1)
            pygame.draw.circle(screen, (0, 255, 0), position, 2)

    def check_sensor(self, degree, screen: pygame.surface.Surface, OUTBOUND_COLOR):
        length = 0
        x = int(self.position[0] + math.cos(math.radians(360 - (self.angle + degree))) * length)
        y = int(self.position[1] + math.sin(math.radians(360 - (self.angle + degree))) * length)

        while not screen.get_at((x, y)) == OUTBOUND_COLOR and length < 300: # Sensor length = max(outbound dist, 300)
            length += 1
            x = int(self.position[0] + math.cos(math.radians(360 - (self.angle + degree))) * length)
            y = int(self.position[1] + math.sin(math.radians(360 - (self.angle + degree))) * length)

        distance = int(math.sqrt(math.pow(x - self.position[0], 2) + math.pow(y - self.position[1], 2)))
        self.sensors.append([(x, y), distance])

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


