import pygame
import math
from Car import Car


# Mask color range
COLOR_RANGE_START = (0, 100, 0)  # Start color of the range (dark green)
COLOR_RANGE_END = (100, 255, 100)  # End color of the range (light green)


########## Collision Manager class ##########
########## NEEDS TO BE WORKED ON ##########

class CollisionManager():
    def __init__(self, car, racetrack_image):
        self.racetrack_image = racetrack_image
        self.car = car
        

    def check_boundary_collision(self, car):
        # Get the color of the pixel at the car's position in the track image
        track_color = self.racetrack_image.get_at((int(car.position[0]), int(car.position[1])))

        # Check if the pixel color is within the green color range indicating the boundary
        return COLOR_RANGE_START[0] <= track_color[0] <= COLOR_RANGE_END[0] and COLOR_RANGE_START[1] <= track_color[1] <= COLOR_RANGE_END[1] and COLOR_RANGE_START[2] <= track_color[2] <= COLOR_RANGE_END[2]

