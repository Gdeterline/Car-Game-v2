import unittest
import pygame
from Menu import Menu

class TestMenu(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1000, 600))
        self.menu = Menu(self.screen)

    def test_initial_settings(self):
        self.assertIsNone(self.menu.selected_circuit)
        self.assertIsNone(self.menu.laps)
        self.assertEqual(self.menu.initial_position, (0, 0))

    def test_display_menu(self):
        self.menu.display_menu()
        # Cannot easily test visual output, but we can ensure no errors occur

    def test_racetrack_input(self):
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_a))
        self.assertEqual(self.menu.racetrack_input(), self.menu.RACETRACK1)
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_b))
        self.assertEqual(self.menu.racetrack_input(), self.menu.RACETRACK3)

    def test_select_laps(self):
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_3))
        self.assertEqual(self.menu.select_laps(), 3)

if __name__ == '__main__':
    unittest.main()
