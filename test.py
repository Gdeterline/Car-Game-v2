import pygame
import os

pygame.init

WIDTH = 1000
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

BG = (255,255,255)
BLACK = (0,0,0)

car_original = pygame.image.load("car.png").convert()
w = car_original.get_width()
h = car_original.get_height()
car_original = pygame.transform.scale(car_original, (w * 0.1, h * 0.1))
x = 400
y = 200

angle = 0

run = True
while run:
    screen.fill(BG)
    angle +=1
    car = pygame.transform.rotate(car_original, angle)
    car_rect = car.get_rect(center = (x,y))
    screen.blit(car, car_rect)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.flip()
    
pygame.quit()