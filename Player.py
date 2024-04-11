import pygame
import numpy as np
import os
from car import Car


class Player():
    
    def __init__(self, car, controls):
        self.car = car
        self.controls = controls
        
    def ingame_inputs(self):
        keys = pygame.key.get_pressed()
        if keys[self.controls['left']]:
            self.car.turn_left()
        if keys[self.controls['right']]:
            self.car.turn_right()
        if keys[self.controls['up']]:
            self.car.accelerate()
        if keys[self.controls['down']]:
            self.car.decelerate()
        if keys[self.controls['brake']]:
            self.car.brake()
        
        