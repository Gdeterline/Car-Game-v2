import pygame
from copy import copy
from Track import Track

CAR_PATH = "./Genetic_Algorithm_Car/assets/cars/car.png"

class Car():

    CAR_WIDTH = 15
    CAR_HEIGHT = 15

    def __init__(self, starting_position):
        pygame.sprite.Sprite.__init__(self)
        car_image = pygame.image.load(CAR_PATH)
        self.sprite = pygame.transform.scale(car_image, (Car.CAR_WIDTH, Car.CAR_HEIGHT))        
        ###### Car's properties ######
        # Car's position vector
        # self.position = starting_position + ()  # Create a copy
        # Car's velocity
        self.velocity = 0
        # Car's angle
        self.angle = 0

        self.sensors = []
        self.alive = True
        self.driven_distance = 0


