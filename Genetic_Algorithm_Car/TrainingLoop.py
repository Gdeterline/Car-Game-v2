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
population_size = 35

class TrainingLoop():

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

        self.cars = [Car(self.AIMainLoop.get_starting_position()) for _ in range(population_size)]
        i = 0
        for car in self.cars:
            i += 1
            car.center = [car.position[0] + car.CAR_WIDTH/2 + i/(population_size), car.position[1] + car.CAR_HEIGHT/2+ i/(population_size)]
            car.position = [car.position[0] + i/(population_size), car.position[1] + i/(population_size)]

        self.generation = 0
        self.genetic_algorithm = GeneticAlgorithm(population_size)
        
        self.weights_saved_timer = 0


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
                    
    def save_car(self):
        # Save the weights of the car's neural network
        # We want to save the weights of the best car - the one that has driven the longest distance
        # We can do this by sorting the cars by driven distance and saving the weights of the first car
        sorted_cars = sorted(self.cars, key=lambda car: car.driven_distance, reverse=True)
        best_car = sorted_cars[0]
        np.save(f"./Genetic_Algorithm_Car/buffer/pretrained_car_weights.npy", best_car.nn.get_weights())
        print("Car weights saved")
        self.weights_saved_timer = pygame.time.get_ticks()
        pygame.display.set_caption("Car weights saved")

    def start(self):
        self.begin = True
        while self.begin:
            pygame.display.set_caption("Press 'a' to load pretrained weights. Press 'z' no to load pretrained weights. Press enter to begin simulation.")    
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
                    elif event.key == pygame.K_a:
                        for car in self.cars:
                            car.nn.set_pretrained_weights(np.load("./Genetic_Algorithm_Car/buffer/pretrained_car_weights.npy"))
                        print("Pretrained weights loaded")
                    elif event.key == pygame.K_z:
                        print("Pretrained weights not loaded")
                    elif event.key == pygame.K_RETURN:
                        self.running = True
                        self.begin = False
                        pygame.display.set_caption("Simulation")
                        break

    def TrainingLoop(self):
        """
        TrainingLoop function is in charge of the Self Driving Car simulation
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
                    elif event.key==pygame.K_s:
                        self.save_car()

            if self.weights_saved_timer != 0:
                if pygame.time.get_ticks() - self.weights_saved_timer > 2000:  # 2 seconds
                    pygame.display.set_caption("Simulation")
                    pygame.display.flip()
                    self.weights_saved_timer = 0  # Reset timer


            self.screen.fill((0, 0, 0))
            self.sensor_surface.fill((0, 0, 0, 0))  # Clear sensor surface
            self.screen.blit((self.selected_circuit), (0, 0))

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
                    
                    # add a if statement to check if the car has done a full lap. If so, set car.alive to False and it's NN weights is saved to a file
                    # to check if the car has done a full lap, check if the car is at the starting position again
                    if car.crossed_starting_line(self.screen, Color.RED) == True:
                        #np.save(f"./Genetic_Algorithm_Car/Pretrained_Models/pretrained_car_weights.npy", car.nn.get_weights())
                        print(f"Car {car} has done a full lap")
                        car.alive = False
                        all_cars_dead = True
                        print(all_cars_dead)
                        break
            
            self.screen.blit(self.sensor_surface, (0, 0))
             
             
            dead, alive = 0, 0
            if all_cars_dead == False:
                for car in self.cars:
                    if car.alive:
                        alive += 1
                    else:
                        dead += 1
            else:
                dead = population_size
                alive = 0
            
            if all_cars_dead == True:
                
                self.genetic_algorithm.avg_fitness.append(self.genetic_algorithm.average_fitness(self.cars))
                # print(self.genetic_algorithm.avg_fitness)
                
                if len(self.genetic_algorithm.avg_fitness) > self.genetic_algorithm.fitness_history_size:
                    self.genetic_algorithm.avg_fitness.pop(0)
                
                print(f"Generation {self.generation} average fitness score: {self.genetic_algorithm.avg_fitness[-1]}")
                
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



loop = TrainingLoop()
loop.TrainingLoop()