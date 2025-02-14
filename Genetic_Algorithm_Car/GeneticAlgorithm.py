import numpy as np
from NeuralNetwork import NeuralNetwork
from Car import Car

class GeneticAlgorithm():
    def __init__(self, population_size, mutation_rate=0.1):
        self.population_size = population_size
        self.mutation_rate = mutation_rate

    def select_parents(self, cars):
        pass

    def crossover(self, parent1, parent2):
        pass

    def mutate(self, nn):
        pass

    def create_next_generation(self, cars):
        pass