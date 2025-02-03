import os
import sys
import pygame
from Track import Track
from Colors import Color
from Car import Car

pygame.init()

font = pygame.font.SysFont("Calibri", 18)

#######################   Testing Racetrack drawing functionnality   #######################
#######################   Works just as expected - Good news!   ############################

class RaceTrackLoop():

    def __init__(self):
        self.track = Track(width=1200, height=800, brush_size=40, background_color=Color.BLACK, track_color=Color.WHITE)
        self.track.surface = pygame.display.set_mode((self.track.width, self.track.height))
        self.instruction_bar = pygame.Rect(0, 0, self.track.width, 80)
        self.car = Car(self.track.starting_position)
        self.track_running = False
        self.running = False


    def TrackLoop(self):
        """
        TrackLoop function is in charge of the track generation
        """
        self.track_running = True
        while self.track_running:

            clock = pygame.time.Clock()

            self.track.separation_line()
            self.track.blit_text_track_drawing()
            self.track.user_track_drawing()
            pygame.display.flip()

            for event in pygame.event.get():    
                if event.type == pygame.QUIT:
                    self.track_running = False
                    self.running = False
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.track_running = False
                        self.running = False
                        sys.exit(0)
                    elif event.key == pygame.K_RETURN:
                        self.track_running = False
                        pygame.display.set_caption("Placing Starting Line")
                        self.track.surface.fill(Color.BLACK, self.instruction_bar)
                        break


            clock.tick(120) # Higher fps to be able to draw a clean track

    def StartingPosLoop(self):
        """
        StartingPosLoop function is in charge of setting the starting line (and the starting point, at the middle of the starting line)
        """
        self.running = True
        while self.running:

            clock = pygame.time.Clock()

            self.track.separation_line()
            self.track.blit_starting_line_instructions()
            
            for event in pygame.event.get():    
                if event.type == pygame.QUIT:
                    self.running = False
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                        sys.exit(0)

            pygame.display.flip()
            

            if self.track.user_track_starting_line() == True:
                running = False
                self.track.surface.fill(Color.BLACK, self.instruction_bar)
                pygame.image.save(self.track.surface, "./Genetic_Algorithm_Car/assets/racetracks/Racetrack.png")
                pygame.display.set_caption("Track Saved")
                pygame.display.flip()
                break
            
            clock.tick(60)


    def get_starting_position(self):
        return self.track.user_starting_position()
    
    def get_screen(self) -> pygame.surface.Surface:
        return self.track.surface
    
    def get_track_background_color(self):
        return self.track.track_color, self.track.background_color