import pygame
from Track import Track
from Colors import Color

pygame.init()

font = pygame.font.SysFont("Calibri", 18)
txtsurf1 = font.render("Left click to draw the track in white", True, Color.WHITE)
txtsurf2 = font.render("Right click to erase track marks", True, Color.WHITE)
txtsurf3 = font.render("Press s key to save the track", True, Color.WHITE)
txtsurf4 = font.render("Press Return to place Car Starting Point", True, Color.WHITE)
txtsurf5 = font.render("Left click to draw the track in white", True, Color.WHITE)

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
                        pygame.display.set_caption("Track Saved")
                    elif event.key == pygame.K_RETURN:
                        track_running = False
                        self.MainLoop()


            self.track.surface.blit(txtsurf1,(10, txtsurf1.get_height() // 2))
            self.track.surface.blit(txtsurf2,(10, txtsurf1.get_height() // 2 + 20))
            self.track.surface.blit(txtsurf3,(10, txtsurf1.get_height() // 2 + 40))
            self.track.surface.blit(txtsurf4,(self.track.width - txtsurf4.get_width() // 2 - 150, txtsurf4.get_height() // 2))


            self.track.user_track_drawing()
            pygame.display.flip()

            clock.tick(60)

    def MainLoop(self):
        """
        MainLoop function is in charge of the driving simulation itself
        """
        running = True
        while running:

            clock = pygame.time.Clock()

            for event in pygame.event.get():    
                if event.type == pygame.QUIT:
                    track_running = False
                    break
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        track_running = False
                        break

            self.track.surface.blit(txtsurf5,(10, txtsurf5.get_height() // 2))



            
            """
            To debug starting position - works just fine

            if self.track.starting_position != []:
                print(self.track.starting_position)
            """
            """
            Need to debug starting line - three clicks then bugs
            self.track.user_track_starting_line()
            """


            pygame.display.flip()

            clock.tick(60)


loop = AIMainLoop()
loop.TrackLoop()
