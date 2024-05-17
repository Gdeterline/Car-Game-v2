import unittest
import pygame
import os 
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from CollisionManager import CollisionManager
from car import Car

class TestCollisionManager(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.car = Car(100, 100)
        self.racetrack_image = pygame.Surface((200, 200))
        self.collision_manager = CollisionManager(self.car, self.racetrack_image)
    
    def test_boundary_collision(self):
        self.racetrack_image.fill((0, 255, 0))
        self.assertTrue(self.collision_manager.check_boundary_collision(self.car, self.racetrack_image))

        self.racetrack_image.fill((255, 0, 0))
        self.assertFalse(self.collision_manager.check_boundary_collision(self.car, self.racetrack_image))
    
    def test_car_collisions(self):
        car2 = Car(100, 100)
        self.assertTrue(self.collision_manager.check_car_collisions(self.car, car2))
        
        car2.position = [100, 100]
        self.assertTrue(self.collision_manager.check_car_collisions(self.car, car2))

if __name__ == '__main__':
    unittest.main()
