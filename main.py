import pygame
import os
import car
from car import Car
#from collision import collide
from driving import Driving
import cv2
import numpy as np
#import math
#import tkinter as tk
#from tkinter import messagebox

# Initialising all pygame modules
pygame.init()
pygame.mixer.init()

CAR = pygame.image.load(os.path.join(os.getcwd(), "./car.png"))


LARGEUR = 1000
HAUTEUR = 600

screen = pygame.display.set_mode((LARGEUR, HAUTEUR)) #Afficher l'ecran de jeu

#CIRCUIT = pygame.image.load("./circuit.jpeg")
#CIRCUIT = pygame.image.load("./circuit2.jpeg")
#CIRCUIT = pygame.image.load("./circuit3.jpeg")
CIRCUIT = pygame.image.load("./rect_racetrack.jpg")

# Circuit interior borders (top, right, bottom, left) : (140, 755, 460, 245)
# Circuit exterior borders (top, right, bottom, left) : (65, 895, 535, 105)


# Resising image so it fits right
CIRCUIT = pygame.transform.scale(CIRCUIT, (1000, 600))

# Read CIRCUIT image
circuit_img = cv2.imread("./rect_racetrack.jpg")

# Convert BGR to HSV for better color detection
circuit_hsv = cv2.cvtColor(circuit_img, cv2.COLOR_BGR2HSV)

# Detect the color of the circuit track (lower and upper bounds of grey)
BRIGHT_GREEN = np.array([0, 0, 200])
DARK_GREY = np.array([255, 50, 255])

# Creating a mask of the racetrack and resizing it
racetrack_mask= cv2.inRange(circuit_hsv, BRIGHT_GREEN, DARK_GREY)

# Ensure the mask has the correct data type and size
racetrack_mask = racetrack_mask.astype(np.uint8)

# Make sure the mask has the same size as the circuit_img
racetrack_mask = cv2.resize(racetrack_mask, (circuit_img.shape[1], circuit_img.shape[0]))

# Apply the bitwise_and operation
res = cv2.bitwise_and(circuit_img, circuit_img, mask=racetrack_mask)

# Checking if the mask is correct
#cv2.imshow("res", res)

#other idea for the mask :
circuit_mask = pygame.mask.from_surface(CIRCUIT)


# Defining inner racetrack rect
# INNER_CIRCUIT_RECT = pygame.rect.Rect(245, 140, 510, 320) 

accelerate_sound = pygame.mixer.Sound("./car_acc_sound.mp3")
breaking_sound = pygame.mixer.Sound("./car_break_sound.mp3")
reverse_sound = pygame.mixer.Sound("./car_rev_sound.mp3")

clock = pygame.time.Clock()

car = Car()
driving = Driving()

'''
def collision_detection():
    collision = driving.car.mask.overlap(circuit_mask, (int(driving.car.pos.x), int(driving.car.pos.y)))
    
    if collision:
        print("Collision detected")
        running = False
'''

# Run until user quits window
running = True
while running:
    dt = clock.tick(60) / 1000 
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_ESCAPE:
                running = False
    
    # Clear the screen to erase the drag of the car 
    screen.fill((0, 0, 0))

    # display race track on the screen with .blit()
    screen.blit(CIRCUIT, (0, 0))

    w = CAR.get_width()
    h = CAR.get_height()
    
    driving.drive(dt)
    driving.steer(dt)
    
    if driving.collide():
        running = False
    
    #print(driving.car.pos)
    accelerate_sound.stop()
    breaking_sound.stop()
    reverse_sound.stop()
    
    
    # displays the car on the track
    
    new_image = pygame.transform.rotate(driving.car.image, driving.car.angle)
    rect = new_image.get_rect(center=driving.car.pos)
    screen.blit(new_image, rect)
    
    #collision_detection()
    
    # update the display
    pygame.display.update()
    pygame.display.flip()
        
# Quit pygame when done playing
pygame.mixer.quit()
pygame.quit()
