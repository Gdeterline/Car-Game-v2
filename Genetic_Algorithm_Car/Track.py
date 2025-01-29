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


    def user_track_drawing(self):
        if pygame.mouse.get_pressed()[0]:
            pygame.draw.circle(self.surface, self.track_color, pygame.mouse.get_pos(), self.brush_size)
            pygame.display.set_caption("")
        elif pygame.mouse.get_pressed()[2]:
            pygame.draw.circle(self.surface, Color.BLACK, pygame.mouse.get_pos(), self.brush_size)
            pygame.display.set_caption("")


