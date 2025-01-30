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
            self.pos1 = tuple
            self.pos2 = tuple
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
        if pygame.mouse.get_pressed()[0]:
            pygame.draw.circle(self.surface, Color.RED, pygame.mouse.get_pos(), 2)
            self.pos1 = pygame.mouse.get_pos()
        elif pygame.mouse.get_pressed()[2]:
            pygame.draw.circle(self.surface, Color.RED, pygame.mouse.get_pos(), 2)
            self.pos2 = pygame.mouse.get_pos()
            pygame.draw.line(self.surface, Color.RED, start_pos=self.pos1, end_pos=self.pos2, width=2)
            self.starting_position = tuple((self.pos1[0] - self.pos2[0], self.pos1[1] - self.pos2[1]))
            print(self.starting_position)
            pygame.draw.circle(self.surface, Color.BLUE, self.starting_position, 2)
            return


            """
        if pygame.mouse.get_pressed()[0]:
            self.starting_line.append(pygame.mouse.get_pos())
            pygame.draw.circle(self.surface, Color.RED, pygame.mouse.get_pos(), 2)

        if len(self.starting_line) == 2:
            pygame.draw.line(self.surface, Color.RED, start_pos=self.starting_line[0], end_pos=self.starting_line[1], width=2)
            self.starting_position = tuple((self.starting_line[0][1] - self.starting_line[0][0], self.starting_line[1][1] - self.starting_line[1][0]))
            pygame.draw.circle(self.surface, Color.BLUE, self.starting_position, 2)
            print("Starting Line placed")
            """
            