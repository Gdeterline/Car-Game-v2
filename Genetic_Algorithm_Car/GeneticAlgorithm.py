import numpy as np
import random as rd
from NeuralNetwork import NeuralNetwork
from Car import Car

class GeneticAlgorithm():
    def __init__(self, population_size, mutation_rate=0.7, crossover_rate=0.5):
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.avg_fitness = []  # Store average fitness scores
        self.fitness_history_size = 5
        self.stagnation_counter = 0  # Count generations with steady fitness
        self.delta_fitness_buffer = 10  # Adjust as needed
        self.fitness_buffer = 5 # Adjust as needed
        self.delta_max_fitness = 100    # Need to assess what driven distance represents a significant improvement - let's start with 100

    def select_parents(self, cars):
        # Select parents based on driven distance (we keep the best 1/4 of the population)
        sorted_cars = sorted(cars, key=lambda car: car.driven_distance, reverse=True)
        parents = sorted_cars[:self.population_size // 4]
        return parents
    
    def average_fitness(self, cars):
        """Calculates the average fitness of the given cars."""
        return sum([car.driven_distance for car in cars]) / len(cars)
    
    def select_max_fitness_cars(self, cars):
        sorted_cars = sorted(cars, key=lambda car: car.driven_distance, reverse=True)
        average_fitness = average_fitness(cars)
        ###### Need to work on selecting the highest fitness score cars (with a driven distance > 100 compared to the next one)
        ###### Need to define if we take a given number of cars, or if it is adaptive
        pass

    def crossover(self, parent1, parent2):
        # Perform crossover (combine weights from parents to create child weights)
        child_weights = []
        parent1_weights = parent1.nn.get_weights()
        parent2_weights = parent2.nn.get_weights()
        for i in range(len(parent1_weights)):
            if rd.random() < self.crossover_rate:
                child_weights.append(parent1_weights[i])
            else:
                child_weights.append(parent2_weights[i])
        return np.array(child_weights)

    def mutate(self, weights):
        # Perform mutation (randomly alter weights)
        for i in range(len(weights)):
            if rd.random() < self.mutation_rate:
                weights[i] += np.random.normal(0, 0.2)
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