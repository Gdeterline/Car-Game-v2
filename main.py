import pygame
import os
import car
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


LARGEUR = 1000 #dimension de l'image circuit
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

# Creating a mask of the racetrack
racetrack_mask = cv2.inRange(circuit_hsv, BRIGHT_GREEN, DARK_GREY)

# Bitwise-AND mask and original image
res = cv2.bitwise_and(circuit_img, circuit_img, mask=racetrack_mask)

# Checking if the mask is correct
#cv2.imshow("res", res)

'''
def collision_detection():
    collision = pygame.mask.Mask.overlap(driving.car.mask, (driving.car.pos.x, driving.car.pos.y))      ##### Error with mask. Maybe use pygame mask for the racetrack too - would make sense
                                                                                                        ##### Offset needs to be checked (top left corners of each maks used as reference)
    if collision:
        print("Collision detected")
        running = False
'''
# Defining inner racetrack rect
#INNER_CIRCUIT_RECT = pygame.rect.Rect(245, 140, 510, 320) 

accelerate_sound = pygame.mixer.Sound("./car_acc_sound.mp3")
breaking_sound = pygame.mixer.Sound("./car_break_sound.mp3")
reverse_sound = pygame.mixer.Sound("./car_rev_sound.mp3")

clock = pygame.time.Clock()

car = car.Car()
driving = Driving()

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
    
    #running = driving.collide()
    
    
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
