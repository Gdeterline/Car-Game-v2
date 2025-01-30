import pygame
from copy import deepcopy
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


