import pygame
from Colors import Color



class Track():
    def __init__(self, width, height, brush_size, background_color, track_color):
            self.width = width
            self.height = height
            self.surface = pygame.Surface((width, height))
            self.surface.fill(background_color)
            self.track_color = track_color
            self.brush_size = brush_size
            self.starting_position = []
            self.starting_line = []
            self.click = 0

    def user_track_drawing(self):
        if pygame.mouse.get_pressed()[0]:
            pygame.draw.circle(self.surface, self.track_color, pygame.mouse.get_pos(), self.brush_size)
            pygame.display.set_caption("")
        elif pygame.mouse.get_pressed()[2]:
            pygame.draw.circle(self.surface, Color.BLACK, pygame.mouse.get_pos(), self.brush_size)
            pygame.display.set_caption("")


    """
    To add a starting line (which needs to be perpendicular), we can add a deque/list with the 4 or 5 first 
    """

    def user_track_starting_position(self):
         if pygame.mouse.get_pressed()[0]:
            self.starting_position = pygame.mouse.get_pos()
            pygame.display.set_caption("Starting Position Set")



    def user_track_starting_line(self):
        while self.click < 2 :
            if pygame.mouse.get_pressed()[0]:
                self.starting_line.append(pygame.mouse.get_pos())
                self.click += 1
        pygame.draw.line(self.surface, Color.RED, start_pos=self.starting_line[0], end_pos=self.starting_line[1])

            