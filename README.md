# Car Game Documentation

## 1. Introduction:

This documentation provides an overview of the code structure, classes, functions, and their functionalities. The code consists of several modules/classes responsible for creating a simple racing game using the Pygame library in Python.

### Game Overview:
Number of Players: The game supports two players competing against each other.
Objective: Players race against each other to complete a set number of laps around the racetrack.
Controls: Each player controls their respective car using a set of keys on the keyboard.

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

This documentation provides an overview of the code's structure and functionality, making it easier for developers to understand and modify the code as needed.