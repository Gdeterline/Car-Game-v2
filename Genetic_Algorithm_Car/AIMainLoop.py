import pygame
from Track import Track
from Colors import Color

pygame.init()

#######################   Testing Racetrack drawing functionnality   #######################
#######################   Works just as expected - Good news!   ############################

class AIMainLoop():

    def __init__(self):
        self.track = Track(width=1200, height=800, brush_size=40, background_color=Color.BLACK, track_color=Color.WHITE)
        self.track.surface = pygame.display.set_mode((self.track.width, self.track.height))

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
                    elif event.key == pygame.K_s:
                        pygame.image.save(self.track.surface, "./Genetic_Algorithm_Car/assets/racetracks/Racetrack.png")
                        print("Track Saved")

            self.track.user_track_drawing()
            pygame.display.flip()

            clock.tick(60)

    def MainLoop(self):
        """
        MainLoop function is in charge of the driving simulation itself
        """
        pass



loop = AIMainLoop()
loop.TrackLoop()
