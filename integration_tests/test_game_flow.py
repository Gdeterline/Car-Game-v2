import unittest
import pygame
from MainGame import MainGame
from Menu import Menu
from car import Car
from Player import Player
from CollisionManager import CollisionManager

class TestGameFlow(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.game = MainGame()
        self.game.screen = pygame.display.set_mode((1000, 600))
        
        # Manually set up the components to avoid user input
        self.game.selected_circuit = pygame.Surface((1000, 600))
        self.game.selected_circuit.fill((255, 255, 255))  # White surface
        self.game.initial_position = [100, 100]
        
        self.game.car1 = Car(100, 100)
        self.game.car2 = Car(150, 100)
        
        self.game.player1 = Player(self.game.car1, {'left': pygame.K_LEFT, 'right': pygame.K_RIGHT, 'up': pygame.K_UP, 'down': pygame.K_DOWN, 'brake': pygame.K_SPACE})
        self.game.player2 = Player(self.game.car2, {'left': pygame.K_a, 'right': pygame.K_d, 'up': pygame.K_w, 'down': pygame.K_s, 'brake': pygame.K_x})
        
        self.game.collision_manager1 = CollisionManager(self.game.car1, self.game.selected_circuit)
        self.game.collision_manager2 = CollisionManager(self.game.car2, self.game.selected_circuit)
        
        self.game.laps = 3
        self.game.lapsP1 = 0
        self.game.lapsP2 = 0

    def test_car_movement_and_collision(self):
        # Simulate key presses for car movements
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_UP))
        self.game.player1.ingame_inputs()
        self.game.car1.update()
        
        pygame.event.post(pygame.event.Event(pygame.KEYDOWN, key=pygame.K_w))
        self.game.player2.ingame_inputs()
        self.game.car2.update()
        
        # Ensure the cars moved
        self.assertNotEqual(self.game.car1.position, [100, 100])
        self.assertNotEqual(self.game.car2.position, [150, 100])
        
        # Check boundary collision (should be false as the track is white)
        self.assertFalse(self.game.collision_manager1.check_boundary_collision())
        self.assertFalse(self.game.collision_manager2.check_boundary_collision())
        
        # Place cars in collision course
        self.game.car1.position = [200, 200]
        self.game.car2.position = [200, 200]
        
        # Check car-to-car collision
        self.assertTrue(self.game.collision_manager1.check_car_collisions(self.game.car2))
    
    def test_lap_counting(self):
        # Simulate a lap completion for player 1
        self.game.car1.position = [self.game.initial_position[0] - 10, self.game.initial_position[1]]
        self.game.run_game()  # Run a single iteration of the game loop
        
        # Check if laps are counted
        self.assertEqual(self.game.lapsP1, 1)
        self.assertEqual(self.game.lapsP2, 0)

if __name__ == '__main__':
    unittest.main()
