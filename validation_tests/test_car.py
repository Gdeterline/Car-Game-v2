import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
import pygame
from car import Car


class TestCar(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.car = Car(100, 100)

    def test_initial_position(self):
        self.assertEqual(self.car.position, [100, 100])
        
    def test_initial_velocity(self):
        self.assertEqual(self.car.velocity, 0)
        
    def test_initial_angle(self):
        self.assertEqual(self.car.angle, 0)
        
    def test_accelerate(self):
        self.car.accelerate()
        self.assertEqual(self.car.velocity, 0.1)
        
    def test_decelerate(self):
        self.car.decelerate()
        self.assertEqual(self.car.velocity, -0.1)
        
    def test_brake(self):
        self.car.velocity = 1
        self.car.brake()
        self.assertEqual(self.car.velocity, 0.8)
        
        self.car.velocity = -1
        self.car.brake()
        self.assertEqual(self.car.velocity, -0.8)
        
    def test_turn_left(self):
        self.car.velocity = 1
        self.car.turn_left()
        self.assertEqual(self.car.angle, 2)
        
    def test_turn_right(self):
        self.car.velocity = 1
        self.car.turn_right()
        self.assertEqual(self.car.angle, -2)
        
    def test_move(self):
        self.car.velocity = 1
        self.car.angle = 0
        self.car.move()
        self.assertEqual(self.car.position, [101, 100])

if __name__ == '__main__':
    unittest.main()
