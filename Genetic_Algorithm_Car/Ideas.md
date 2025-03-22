# Improving the training of the car using genetic algorithms

This file contains ideas for improving the training of the car using genetic algorithms.

## Ideas

<ins>Must have:</ins>

1. **Need to check how to tune the hyperparameters**: Need to check how to tune the hyperparameters of the genetic algorithm to improve the performance of the car. The hyperparameters include the population size, the mutation rate, the crossover rate, and the size of the hidden layer of the neural network. The hyperparameters could also include the sensor range, the sensor angle, and the sensor noise.

2. **Add noise to the model**: Add noise to the model to make the training more robust. The noise could be added to the sensor readings, the neural network weights, and the car's movements. The noise should be added to the model during the training and testing phases.

3. **Implement an adaptive mutation rate**: Implement an adaptive mutation rate that changes based on the performance of the car. The mutation rate should increase if the car is not performing well and decrease if the car is performing well. 
Also, the mutation rate should be high at the beginning of the training and decrease over time. If the fitness of the population is not improving, the mutation rate should increase.

<ins>Nice to have:</ins>

4. **Select the best individuals for the next generation**: Select the best individuals for the next generation based on their fitness. The best individuals should be selected based on their fitness, and the worst individuals should be removed.
This should be done especially if there is a big difference in the fitness of the individuals in the population.
-> The parent selection process should be adaptive.

5. **Need to implement a functionnality to load a pretrained model for the genetic algorithm**: Need to implement a functionnality to load a pretrained model for the genetic algorithm. That way, the genetic algorithm can start from a pretrained model and improve it further.

6. **Implement a structure for the fitness function**: Implement a structure for the fitness function that evaluates the performance of the car based on the distance traveled, the time taken to complete a lap. That way, the fitness function measures the distance traveled by the car and its speed.


