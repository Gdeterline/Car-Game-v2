import unittest
import pygame
import os
from car import Car
from Player import Player
from CollisionManager import CollisionManager
from MainGame import MainGame

class TestCar(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.car = Car(454, 134)

    def test_init(self):
        self.assertEqual(self.car.position, [454, 134])
        self.assertEqual(self.car.velocity, 0)
        self.assertEqual(self.car.angle, 0)

class TestPlayer(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.car = Car(454, 134)
        self.player = Player(self.car, {'left': pygame.K_LEFT, 'right': pygame.K_RIGHT, 'up': pygame.K_UP, 'down': pygame.K_DOWN, 'brake': pygame.K_SPACE})

    def test_init(self):
        self.assertEqual(self.player.car, self.car)
        self.assertEqual(self.player.controls['left'], pygame.K_LEFT)
        self.assertEqual(self.player.controls['right'], pygame.K_RIGHT)

class TestCollisionManager(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.car = Car(454, 134)
        self.collision_manager = CollisionManager(self.car, None)

    def test_init(self):
        self.assertEqual(self.collision_manager.car, self.car)
        self.assertEqual(self.collision_manager.racetrack_image, None)

class TestMainGame(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.maingame = MainGame()

    def test_init(self):
        self.assertEqual(self.maingame.selected_circuit, None)
        self.assertEqual(self.maingame.laps, None)

if __name__ == '__main__':
    unittest.main()