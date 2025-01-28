from DQNAgent import DQNAgent
from DRLEnvironment import DRLEnvironment
import pygame
import os
import time

steps = 1000
state_size = 3
action_size = 5

RACETRACK = pygame.image.load(os.path.join(os.getcwd(), "./images/circuit.jpeg"))
RACETRACK = pygame.transform.rotate(RACETRACK, 180)
RACETRACK = pygame.transform.scale(RACETRACK, (1000, 700))
CAR = pygame.image.load(os.path.join(os.getcwd(), "./images/car.png"))


class TrainDQN():
    def __init__(self):
        self.agent = DQNAgent(3, 5)
        self.env = DRLEnvironment(454, 134, CAR, RACETRACK)
        
    def train(self, episodes=500, steps_per_episode=1000):
        for episode in range(episodes):
            # Reset environment at the start of each episode and get the initial state
            state = self.env.reset()
            total_reward = 0
            over = False

            for step in range(steps_per_episode):
                # Agent selects an action
                action = self.agent.act(state)

                # Environment processes the action and returns the next state, reward, and over flag
                next_state, reward, over = self.env.step(action)

                # Store the experience in memory
                self.agent.remember(state, action, reward, next_state, over)

                # Update the current state
                state = next_state

                # Accumulate the reward
                total_reward += reward

                # Train the agent with a replay if the memory has enough samples
                if len(self.agent.memory) > self.agent.batch_size:
                    self.agent.replay()

                if over:
                    break

            # Log the progress
            print(f"Episode: {episode + 1}/{episodes}, Total Reward: {total_reward}, Epsilon: {self.agent.epsilon:.2f}")

            # Save the model periodically
#            if (episode + 1) % 50 == 0:
#                self.agent.save_model(f"dqn_model_episode_{episode + 1}.h5")

# Initialize pygame and load car image
pygame.init()
CAR = pygame.image.load(os.path.join(os.getcwd(), "./images/car.png"))

if __name__ == "__main__":
    # Create the training instance and start training
    trainer = TrainDQN()
    start_time = time.time()
    trainer.train()
    print(f"Training time of {time.time()-start_time} seconds")