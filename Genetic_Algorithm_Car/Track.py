import pygame
from Colors import Color

class Track():
    def __init__(self, width, height, brush_size):
            self.width = width
            self.height = height
            self.surface = pygame.Surface((width, height))
            self.surface.fill(Color.WHITE)
            self.track_color = Color.BLACK
            self.brush_size = brush_size


    def user_track_drawing(self):
        if pygame.mouse.get_pressed()[0]:
            pygame.draw.circle(self.surface, self.track_color, pygame.mouse.get_pos(), self.brush_size)
        elif pygame.mouse.get_pressed()[2]:
            pygame.draw.circle(self.surface, Color.WHITE, pygame.mouse.get_pos(), self.brush_size)

    def save_track(self):
        pygame.image.save(self.surface, "./Racetrack.png")

