import numpy as np
import random as rd
from NeuralNetwork import NeuralNetwork
from Car import Car

class GeneticAlgorithm():
    def __init__(self, population_size, mutation_rate=0.3):
        self.population_size = population_size
        self.mutation_rate = mutation_rate

    def select_parents(self, cars):
        # Select parents based on driven distance (we keep the best 1/4 of the population)
        sorted_cars = sorted(cars, key=lambda car: car.driven_distance, reverse=True)
        parents = sorted_cars[:self.population_size // 4]
        return parents

    def crossover(self, parent1, parent2):
        # Perform crossover (combine weights from parents to create child weights)
        child_weights = []
        parent1_weights = parent1.nn.get_weights()
        parent2_weights = parent2.nn.get_weights()
        for i in range(len(parent1_weights)):
            if rd.random() < 0.5:
                child_weights.append(parent1_weights[i])
            else:
                child_weights.append(parent2_weights[i])
        return np.array(child_weights)

    def mutate(self, weights):
        # Perform mutation (randomly alter weights)
        for i in range(len(weights)):
            if rd.random() < self.mutation_rate:
                weights[i] += np.random.normal(0, 0.1)
        return weights

    def create_next_generation(self, cars, starting_position):
        # Select parents
        parents = self.select_parents(cars)
        next_generation = []
        for i in range(self.population_size):
            if i < len(parents):
                # Keep the best parents
                new_car = Car(starting_position)
                new_car.nn.set_weights(parents[i].nn.get_weights())
                next_generation.append(new_car)
            else:
                # Create children
                parent1 = rd.choice(parents)
                parent2 = rd.choice(parents)
                child_weights = self.crossover(parent1, parent2)
                child_weights = self.mutate(child_weights)
                new_car = Car(starting_position)
                new_car.nn.set_weights(child_weights)
                next_generation.append(new_car)
        return next_generation