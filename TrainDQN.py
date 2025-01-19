from DQNAgent import DQNAgent
from DRLEnvironment import DRLEnvironment
import pygame
import os

steps = 1000
state_size = 3
action_size = 5

CAR = pygame.image.load(os.path.join(os.getcwd(), "./images/car.png"))


class TrainDQN():
    def __init__(self):
        self.agent = DQNAgent(3, 5)
        self.env = DRLEnvironment(454, 134, CAR)