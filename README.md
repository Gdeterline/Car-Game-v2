# Car Game V2 Documentation

## Device Setup

\[To Complete\] (import...)

## 1. Car Game V2 Introduction

This project will be divided into three parts.

- [I. Multiplayer Game](#Multiplayer_Game)
- [II. Self Driving Car - Genetic Algorithm Method](#GA)
- [III. Self Driving Car - Reinforcement Learning Method](#RL)

# I. Multiplayer Game <a name="Multiplayer_Game"></a>

## 1. Introduction

This documentation provides an overview of the code structure, classes, functions, and their functionalities. The code consists of several modules/classes responsible for creating a simple racing game using the Pygame library in Python.

### Game Overview:

- Number of Players: The game supports two players competing against each other.

- Objective: Players race against each other to complete a set number of laps around the racetrack.

- Controls: Each player controls their respective car using a set of keys on the keyboard.

#### Player Controls:
- Player 1 (Car 1):
    - Left: Arrow Key Left
    - Right: Arrow Key Right
    - Up: Arrow Key Up
    - Down: Arrow Key Down
    - Brake: Spacebar

- Player 2 (Car 2):
    - Left: Key Q
    - Right: Key D
    - Up: Key Z
    - Down: Key S
    - Brake: Key X

#### Control Functions:
- Left/Right: Steer the car left or right respectively.
- Up: Accelerate the car forward.
- Down: Decelerate or move the car backward.
- Brake: Apply brakes to stop the car.


### Code Structure:

Here's a breakdown of the code structure:

1. **MainGame Class**: Handles the main game loop, including menu display, racetrack selection, gameplay, and collision detection.
2. **Menu Class**: Displays the menu to select the racetrack and number of laps.
3. **Car Class**: Represents the car object with methods for movement based on physics laws.
4. **Player Class**: Controls the player inputs for car movement.
5. **CollisionManager Class**: Manages collision detection between cars and boundaries.

## 2. MainGame Class:

### Attributes:
- **screen**: Pygame display surface.
- **menu**: Menu instance for displaying and managing menu operations.
- **selected_circuit**: Stores the selected racetrack image.
- **laps**: Stores the number of laps selected for the game.
- **initial_position**: Stores the initial position for player cars.
- **car1, car2**: Car instances for player 1 and player 2.
- **player1, player2**: Player instances controlling car movements for player 1 and player 2.
- **collision_manager1, collision_manager2**: CollisionManager instances for player 1 and player 2.
- **lapsP1, lapsP2**: Counters for the laps completed by player 1 and player 2.
- **x1, x2**: Flags to track laps completed by player 1 and player 2.

### Methods:
- **run_menu()**: Displays the menu, handles user input for racetrack and laps selection, and initiates the game loop.
- **run_game()**: Manages the main game loop, including event handling, car movement updates, collision detection, and lap counting.

## 3. Menu Class:

### Attributes:
- **screen**: Pygame display surface.
- **background**: Background image for the menu.
- **scaled_background**: Scaled version of the background image.
- **selected_circuit**: Stores the selected racetrack image.
- **laps**: Stores the number of laps selected.

### Methods:
- **display_menu()**: Displays the menu options, selected circuit, and number of laps on the screen.
- **racetrack_input()**: Handles user input to select the racetrack.
- **select_laps()**: Handles user input to select the number of laps.

## 4. Car Class:

### Attributes:
- **image**: Image of the car.
- **crash**: Image of the crashed car.
- **rect**: Rectangular area of the car's image.
- **mask**: Mask for collision detection.
- **position**: Position vector of the car.
- **velocity**: Velocity of the car.
- **angle**: Angle of the car.

### Methods:
- **move()**: Updates the car's position based on velocity and angle.
- **turn_left()**, **turn_right()**: Rotates the car left or right.
- **accelerate()**, **decelerate()**: Increases or decreases the car's velocity.
- **brake()**: Applies brakes to the car.
- **update()**: Updates the car's position and mask.

## 5. Player Class:

### Attributes:
- **car**: Car instance controlled by the player.
- **controls**: Dictionary mapping player controls to keyboard keys.

### Methods:
- **ingame_inputs()**: Handles player inputs for car movement.

## 6. CollisionManager Class:

### Attributes:
- **racetrack_image**: Image of the racetrack.
- **car**: Car instance.

### Methods:
- **check_boundary_collision()**: Checks if the car collides with the racetrack boundary.
- **check_car_collisions()**: Checks for collisions between two cars.


# **Have fun playing the game !**

# II. Self Driving Car - Genetic Algorithm Method <a name="GA"></a>

## 1. Introduction

Genetic Algorithms are part of what we call evolutionary algorithms. The concept of GAs comes from the observation over time - and especially of natural selection and genetics.
To quote Geeks for Geeks, genetic algorithms simulate the process of natural selection which means those species that can adapt to changes in their environment can survive and reproduce and go to the next generation. In simple words, they simulate “survival of the fittest”.

The aim of this subproject is to implement such an algorithm, in order to create a self driving car, against which the player can play.

## 2. Development phases

We will develop this functionnality in several steps.

- **GA V1**
    - Develop Track Drawing Functionnality (addition to the initial project - fun to do on the player side, good for practice on my side): Once we have one trakc, it should be slightly simpler to handle collisions, as at first, the track should be very simple (black track on a white screen)
    - Car - Prototyping stage
    - Develop some car features and functions (Accelerating, Turning, etc.)
    - Develop the Collision Detection functionnality
    - Develop, then draw, the distance sensors

- **GA V1.1**
    - Develop the genetic aspect of the project - genomes, NEAT, etc.

- **GA V2** -
    - Add extra functionnalities/functionnalities

# III. Self Driving Car - Reinforcement Learning Method <a name="RL"></a>

Deep reinforcement learning consists in the fusion of two major components : 
- Deep learning - DL consists in making predictions from large amounts of data, using neural networks.
- Reinforcement learning - RL consists in learning through experience. The idea is to associate rewards/penalties to actions, and seek to maximise cumulative rewards.

\[To Complete\]

### Component 1 - Deep Learning

To implement the neural networks we will use in this project, we will use the Keras framework.