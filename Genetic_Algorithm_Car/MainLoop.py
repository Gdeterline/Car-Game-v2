import os
import sys
import numpy as np
import pygame
import time
from Colors import Color
from Car import Car
from TrackLoop import RaceTrackLoop
from GeneticAlgorithm import GeneticAlgorithm

pygame.init()

font = pygame.font.SysFont("Calibri", 18)
population_size = 30    # Need to check sensor issue: when cars are in the exact same position, sensors seem not to overlap

class MainLoop():

    def __init__(self):
        self.AIMainLoop = RaceTrackLoop()
        self.AIMainLoop.TrackLoop()
        self.AIMainLoop.StartingPosLoop()
        self.screen = self.AIMainLoop.get_screen()
        self.sensor_surface = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)  # Create a transparent surface for the sensors
        self.track_color, self.background_color = self.AIMainLoop.get_track_background_color()
        self.selected_circuit = pygame.image.load("./Genetic_Algorithm_Car/assets/racetracks/Racetrack.png")
        self.begin = True
        self.pause = False
        self.running = False
        """
        self.car1 = Car(self.startpos)
        self.car2 = Car([self.startpos[0] + 30, self.startpos[1] + 10])
        self.car1.center = [self.car1.position[0] + self.car1.CAR_WIDTH/2, self.car1.position[1] + self.car1.CAR_HEIGHT/2]
        self.car2.center = [self.car2.position[0] + self.car2.CAR_WIDTH/2 + 30, self.car2.position[1] + self.car2.CAR_HEIGHT/2 + 10]
        """
        self.cars = [Car(self.AIMainLoop.get_starting_position()) for _ in range(population_size)]
        i = 0
        for car in self.cars:
            i += 1
            car.center = [car.position[0] + car.CAR_WIDTH/2 + i/(population_size), car.position[1] + car.CAR_HEIGHT/2+ i/(population_size)]
            car.position = [car.position[0] + i/(population_size), car.position[1] + i/(population_size)]
        self.generation = 0
        self.genetic_algorithm = GeneticAlgorithm(population_size)


    def pause_game(self):
        self.pause = True
        self.running = False
        while self.pause:
            pygame.display.set_caption("Game Paused")
            for event in pygame.event.get():    
                if event.type == pygame.QUIT:
                    self.pause = False
                    self.running = False
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.pause = False
                        self.running = False
                        sys.exit(0)
                    if event.key == pygame.K_p:
                        self.pause = False
                        self.running = True
                        break

    def start(self):
        self.begin = True
        while self.begin:
            pygame.display.set_caption("Press enter to begin simulation")
            for event in pygame.event.get():    
                if event.type == pygame.QUIT:
                    self.begin = False
                    self.running = False
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.begin = False
                        self.running = False
                        sys.exit(0)
                    elif event.key == pygame.K_RETURN:
                        self.running = True
                        self.begin = False
                        pygame.display.set_caption("Simulation")
                        break

    def MainLoop(self):
        """
        MainLoop function is in charge of the Self Driving Car simulation
        """
        running = False

        # Press enter to begin simulation
        self.start()

        while self.running:

            self.pause = False
            
            for event in pygame.event.get():    
                if event.type == pygame.QUIT:
                    self.running = False
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                        sys.exit(0)
                    elif event.key==pygame.K_p:
                        self.pause_game()


            self.screen.fill((0, 0, 0))
            self.sensor_surface.fill((0, 0, 0, 0))  # Clear sensor surface
            self.screen.blit((self.selected_circuit), (0, 0))

            """
            print(self.car1.position, self.car1.center)
            if self.car1.alive:
                self.car1.clear_sensors()
                for degree in range(-90, 120, 45):
                    self.car1.check_sensor(degree, self.screen, self.background_color)
                self.car1.draw_sensor(self.screen)
                self.car1.update(self.screen, self.background_color)
                self.car1._sprite = pygame.transform.rotate(self.car1.sprite, self.car1.angle)
                rect1 = self.car1.sprite.get_rect(center=self.car1.center)
                self.screen.blit(self.car1._sprite, rect1)
            
            print(self.car2.position, self.car2.center)  
            if self.car2.alive:
                self.car2.clear_sensors()
                for degree in range(-90, 120, 45):
                    self.car2.check_sensor(degree, self.screen, self.background_color)
                self.car2.draw_sensor(self.screen)
                self.car2.update(self.screen, self.background_color)
                self.car2._sprite = pygame.transform.rotate(self.car2.sprite, self.car2.angle)
                rect2 = self.car2.sprite.get_rect(center=self.car2.center)
                self.screen.blit(self.car2._sprite, rect2)
            """
            
            all_cars_dead = True
            
            for car in self.cars:
                if car.alive:
                    all_cars_dead = False
                    # print(f"Car {car} alive: {car.alive}")
                    car.clear_sensors()
                    for degree in range(-90, 120, 45):  # 5 sensors - if changed, need to change the input size of the NN in Car.py
                        car.check_sensor(degree, self.screen, self.background_color)
                    car.draw_sensor(self.sensor_surface)
                    
                    car.update(self.screen, self.background_color)
                    # print(car.driven_distance)    # Check if the car fitness score is well updated

                    car._sprite = pygame.transform.rotate(car.sprite, car.angle)
                    rect = car.sprite.get_rect(center=car.center)
                    self.screen.blit(car._sprite, rect)
            
            self.screen.blit(self.sensor_surface, (0, 0))
             
             
            dead, alive = 0, 0
            for car in self.cars:
                if car.alive:
                    alive += 1
                else:
                    dead += 1
            
            if all_cars_dead == True:
                #print("All cars dead")
                self.generation += 1
                #print(f"Generation: {self.generation}")
                self.cars = self.genetic_algorithm.create_next_generation(self.cars, self.AIMainLoop.get_starting_position())
                i = 0
                for car in self.cars:
                    i += 1
                    car.center = [car.position[0] + car.CAR_WIDTH/2 + i/(population_size), car.position[1] + car.CAR_HEIGHT/2 + i/(population_size)]
                    car.position = [car.position[0] + i/(population_size), car.position[1] + i/(population_size)]
            
            self.screen.blit(font.render(f"Generation: {self.generation}", True, Color.WHITE), (10, 10))
            self.screen.blit(font.render(f"Alive: {alive}", True, Color.WHITE), (10, 30))
            self.screen.blit(font.render(f"Dead: {dead}", True, Color.WHITE), (10, 50))    
                
            # print(all_cars_dead)
            
            pygame.display.flip()



loop = MainLoop()
loop.MainLoop()