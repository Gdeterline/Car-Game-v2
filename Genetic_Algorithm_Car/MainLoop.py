import os
import sys
import pygame
from Colors import Color
from Car import Car
from TrackLoop import RaceTrackLoop

pygame.init()

font = pygame.font.SysFont("Calibri", 18)

class MainLoop():

    def __init__(self):
        self.AIMainLoop = RaceTrackLoop()
        self.AIMainLoop.TrackLoop()
        self.AIMainLoop.StartingPosLoop()
        self.startpos = self.AIMainLoop.get_starting_position()
        self.screen = self.AIMainLoop.get_screen()
        self.track_color, self.background_color = self.AIMainLoop.get_track_background_color()
        self.car = Car(self.startpos)
        self.car.center = [self.car.position[0] + self.car.CAR_WIDTH/2, self.car.position[1] + self.car.CAR_HEIGHT/2]
        self.selected_circuit = pygame.image.load("./Genetic_Algorithm_Car/assets/racetracks/Racetrack.png")
        self.begin = True
        self.pause = False
        self.running = False

        self.car.velocity = 0.3

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
            self.screen.blit((self.selected_circuit), (0, 0))
            
            if self.car.alive:
                
                """
                Driving actions to add here!
                """
                
                self.car.update(self.screen, self.background_color)
                self.car._sprite = pygame.transform.rotate(self.car.sprite, self.car.angle)
                rect = self.car.sprite.get_rect(center=self.car.center)
                self.screen.blit(self.car._sprite, rect)
                self.car.clear_sensors()
                for degree in range(-90, 120, 45):
                    self.car.check_sensor(degree, self.screen, self.background_color)
                self.car.draw_sensor(self.screen)

            

            pygame.display.flip()



loop = MainLoop()
loop.MainLoop()

