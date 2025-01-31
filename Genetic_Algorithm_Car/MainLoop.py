import os
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

        # Test to ensure car moves correctly
        self.car.velocity = 1


    def MainLoop(self):
        """
        MainLoop function is in charge of the Self Driving Car simulation
        """
        running = False
        # Press enter to begin simulation
        begin = True
        while begin:
            pygame.display.set_caption("Press enter to begin simulation")
            for event in pygame.event.get():    
                if event.type == pygame.QUIT:
                    begin = False
                    running = False
                    break
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        begin = False
                        running = True
                        pygame.display.set_caption("Simulation")
                        break

        while running:

            pause = False
            
            for event in pygame.event.get():    
                if event.type == pygame.QUIT:
                    running = False
                    break
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        break
                    elif event.key==pygame.K_p:
                        pygame.time.delay(3000)


            self.screen.fill((0, 0, 0))
            self.screen.blit((self.selected_circuit), (0, 0))

            """
            Driving actions to add here!
            """
            
            if self.car.alive:
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

