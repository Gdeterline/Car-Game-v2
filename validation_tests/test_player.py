import unittest
import pygame
from car import Car
from Player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.car = Car(100, 100)
        self.controls = {'left': pygame.K_LEFT, 'right': pygame.K_RIGHT, 'up': pygame.K_UP, 'down': pygame.K_DOWN, 'brake': pygame.K_SPACE}
        self.player = Player(self.car, self.controls)

    def test_controls(self):
        self.assertEqual(self.player.controls, self.controls)
        
    def test_ingame_inputs(self):
        pygame.key.set_mods(0)  # Reset all keys
        pygame.key.set_pressed((pygame.K_LEFT, pygame.K_UP))  # Simulate pressing left and up keys
        self.player.ingame_inputs()
        self.assertEqual(self.car.angle, 2)
        self.assertEqual(self.car.velocity, 0.1)

if __name__ == '__main__':
    unittest.main()
