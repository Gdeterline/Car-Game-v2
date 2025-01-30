import pygame
from Colors import Color

pygame.init()
font = pygame.font.SysFont("Calibri", 18)


class Track():
    def __init__(self, width, height, brush_size, background_color, track_color):
            self.width = width
            self.height = height
            self.surface = pygame.Surface((width, height))
            self.surface.fill(background_color)
            self.track_color = track_color
            self.brush_size = brush_size
            self.pos1 = tuple
            self.pos2 = tuple
            self.starting_position = tuple
            self.spos1 = 0
            self.spos2 = 0

    def separation_line(self):
        pygame.draw.line(self.surface, Color.GREY, start_pos=(0, 80), end_pos=(self.width, 80))

    def blit_text_track_drawing(self):
        txtsurf1 = font.render("Left click to draw the track in white", True, Color.WHITE)
        txtsurf2 = font.render("Right click to erase track marks", True, Color.WHITE)
        txtsurf4 = font.render("PRESS RETURN TO PLACE STARTING LINE", True, Color.WHITE)
        self.surface.blit(txtsurf1,(10, txtsurf1.get_height() // 2))
        self.surface.blit(txtsurf2,(10, txtsurf1.get_height() // 2 + 20))
        self.surface.blit(txtsurf4,(self.width - txtsurf4.get_width() // 2 - 150, txtsurf4.get_height() // 2))

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

    def blit_test_starting_line(self):
        txtsurf5 = font.render("Left click to place first point of the starting line", True, Color.WHITE)
        txtsurf6 = font.render("Right click to place second point of the starting line", True, Color.WHITE)
        txtsurf4 = font.render("PRESS RETURN TO SAVE TRACK AND BEGIN SIMULATION", True, Color.WHITE)
        self.surface.blit(txtsurf5,(10, txtsurf5.get_height() // 2))
        self.surface.blit(txtsurf6,(10, txtsurf5.get_height() // 2 + 20))
        self.surface.blit(txtsurf4,(self.width - txtsurf4.get_width() // 2 - 220, txtsurf4.get_height() // 2))

    def user_track_starting_line(self):
        if pygame.mouse.get_pressed()[0]:
            pygame.draw.circle(self.surface, Color.RED, pygame.mouse.get_pos(), 2)
            self.pos1 = pygame.mouse.get_pos()
        elif pygame.mouse.get_pressed()[2]:
            pygame.draw.circle(self.surface, Color.RED, pygame.mouse.get_pos(), 2)
            self.pos2 = pygame.mouse.get_pos()
            pygame.draw.line(self.surface, Color.RED, start_pos=self.pos1, end_pos=self.pos2, width=2)
            return True

    def user_starting_position(self):
        self.starting_position = (self.spos1, self.spos2)
        self.spos1 = (self.pos1[0] + self.pos2[0])/2
        self.spos2 = (self.pos1[1] + self.pos2[1])/2
        pygame.draw.circle(self.surface, Color.BLUE, self.starting_position, 2)



            