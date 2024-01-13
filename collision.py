import pygame
import numpy as np
import cv2
from car import Car

def collide(car_instance):
    car_mask = car_instance.mask
    CIRCUIT = pygame.transform.scale(pygame.image.load("./rect_racetrack.jpg"), (1000, 600))
    circuit_img = cv2.imread("./rect_racetrack.jpg")
    circuit_hsv = cv2.cvtColor(circuit_img, cv2.COLOR_BGR2HSV)
    BRIGHT_GREEN = np.array([0, 0, 200])
    DARK_GREY = np.array([255, 50, 255])
    racetrack_mask = cv2.inRange(circuit_hsv, BRIGHT_GREEN, DARK_GREY)
    racetrack_mask_pygame = pygame.mask.from_surface(pygame.surfarray.make_surface(racetrack_mask))
    collision = car_mask.overlap(racetrack_mask_pygame, (int(car_instance.pos.x), int(car_instance.pos.y)))

    if collision:
        print("Collision detected")
        return True

    return False