import unittest
import pygame
from MainGame import MainGame

class TestMainGame(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.game = MainGame()

    def test_initial_setup(self):
        self.assertIsNotNone(self.game.screen)
        self.assertIsNotNone(self.game.menu)
        self.assertIsNone(self.game.selected_circuit)
        self.assertIsNone(self.game.laps)
        self.assertEqual(self.game.initial_position, [0, 0])

    def test_run_menu(self):
        self.game.menu.selected_circuit = self.game.menu.RACETRACK1
        self.game.menu.laps = 3
        self.assertEqual(self.game.selected_circuit, self.game.menu.RACETRACK1)
        self.assertEqual(self.game.laps, 3)

if __name__ == '__main__':
    unittest.main()
