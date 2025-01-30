import os
import pygame
from Track import Track
from Colors import Color
from Car import Car

pygame.init()

font = pygame.font.SysFont("Calibri", 18)

#######################   Testing Racetrack drawing functionnality   #######################
#######################   Works just as expected - Good news!   ############################

class AIMainLoop():

    def __init__(self):
        self.track = Track(width=1200, height=800, brush_size=40, background_color=Color.BLACK, track_color=Color.WHITE)
        self.track.surface = pygame.display.set_mode((self.track.width, self.track.height))
        self.instruction_bar = pygame.Rect(0, 0, self.track.width, 80)
        self.car = Car(self.track.starting_position)

    def TrackLoop(self):
        """
        TrackLoop function is in charge of the track generation
        """
        track_running = True
        while track_running:

            clock = pygame.time.Clock()

            for event in pygame.event.get():    
                if event.type == pygame.QUIT:
                    track_running = False
                    break
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        track_running = False
                        break
                    elif event.key == pygame.K_RETURN:
                        track_running = False
                        pygame.display.set_caption("Placing Starting Line")
                        self.track.surface.fill(Color.BLACK, self.instruction_bar)
                        self.StartingPosLoop()

            self.track.separation_line()
            self.track.blit_text_track_drawing()
            self.track.user_track_drawing()
            pygame.display.flip()
            clock.tick(100)

    def StartingPosLoop(self):
        """
        StartingPosLoop function is in charge of setting the starting line (and the starting point, at the middle of the starting line)
        """
        running = True
        while running:

            clock = pygame.time.Clock()

            for event in pygame.event.get():    
                if event.type == pygame.QUIT:
                    running = False
                    break
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        break

            self.track.separation_line()
            self.track.blit_test_starting_line()
            
            if self.track.user_track_starting_line() == True:
                running = False
                self.track.surface.fill(Color.BLACK, self.instruction_bar)
                pygame.image.save(self.track.surface, "./Genetic_Algorithm_Car/assets/racetracks/Racetrack.png")
                pygame.display.set_caption("Track Saved")
                pygame.display.flip()
                self.MainLoop()

            pygame.display.flip()
            clock.tick(60)


    def MainLoop(self):
        """
        MainLoop function is in charge of the Self Driving Car simulation
        """

        self.selected_circuit = pygame.image.load("./Genetic_Algorithm_Car/assets/racetracks/Racetrack.png")
        self.car.position = [self.track.user_starting_position()[0] - self.car.CAR_WIDTH/2, self.track.user_starting_position()[1] - self.car.CAR_HEIGHT/2]
        self.track.surface.fill((0, 0, 0))
        self.track.surface.blit((self.selected_circuit), (0, 0))
        self.track.surface.blit(self.car.sprite, self.car.position)


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
            
            for event in pygame.event.get():    
                if event.type == pygame.QUIT:
                    running = False
                    break
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        break
                    """
                    Debugging purposes - check if car position is well adjusted - OK
                    elif event.key == pygame.K_RETURN:
                        self.car.position = self.car.update_car_position_test()
                    """


            # Test to ensure car moves correctly
            self.car.velocity = 1
            self.car.angle = 1
            self.car.move()

            self.track.surface.fill((0, 0, 0))
            self.track.surface.blit((self.selected_circuit), (0, 0))

            if self.car.alive:
                self.track.surface.blit(self.car.sprite, self.car.position)

            

            pygame.display.flip()



loop = AIMainLoop()
loop.TrackLoop() # To avoid having to build the track every time ^^

