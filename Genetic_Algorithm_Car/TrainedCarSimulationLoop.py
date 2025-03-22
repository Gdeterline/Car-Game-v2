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

class TrainedCarSimulationLoop():

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
        
        self.trained_car = Car(self.AIMainLoop.get_starting_position())
        self.trained_car.nn.set_weights(np.load("./Genetic_Algorithm_Car/Pretrained_Models/pretrained_car_weights.npy"))
        self.trained_car.center = [self.trained_car.position[0] + self.trained_car.CAR_WIDTH/2, self.trained_car.position[1] + self.trained_car.CAR_HEIGHT/2]
        
        self.laps = 0
        self.lap_flag = False


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

    def TrainedCarSimulationLoop(self):
        """
        TrainedCarSimulationLoop is the loop in charge of running the simulation of the trained car over new racetracks
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

            if self.trained_car.alive == True:
                self.screen.fill((0, 0, 0))
                self.sensor_surface.fill((0, 0, 0, 0))  # Clear sensor surface
                self.screen.blit((self.selected_circuit), (0, 0))

                if self.lap_flag == True:
                    self.laps +=1
                    self.lap_flag = False

                self.trained_car.clear_sensors()
                for degree in range(-90, 120, 45):  
                    self.trained_car.check_sensor(degree, self.screen, self.background_color)
                self.trained_car.draw_sensor(self.sensor_surface)
                
                self.trained_car.update(self.screen, self.background_color)

                self.trained_car._sprite = pygame.transform.rotate(self.trained_car.sprite, self.trained_car.angle)
                rect = self.trained_car.sprite.get_rect(center=self.trained_car.center)
                self.screen.blit(self.trained_car._sprite, rect)
                
                # Add a if statement to check if the self.trained_car has done a full lap
                if self.trained_car.crossed_starting_line(self.screen, Color.RED) == True:
                    self.lap_flag = True
                    
            else:
                pygame.display.set_caption("The car collided with the boundaries, so the training was not optimal")
                
            self.screen.blit(font.render(f"Laps completed: {self.laps}", True, Color.WHITE), (10, 10))    # laps - 3 because buffer of 3
            self.screen.blit(self.sensor_surface, (0, 0))             
            pygame.display.flip()



loop = TrainedCarSimulationLoop()
loop.TrainedCarSimulationLoop()