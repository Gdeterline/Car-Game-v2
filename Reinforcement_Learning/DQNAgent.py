import numpy as np
import random
from collections import deque
from keras import models
from keras import layers
from keras import optimizers

class DQNAgent():
    def __init__(self, state_size, action_size, batch_size=64, gamma=0.95, learning_rate=0.001, epsilon=1.0, epsilon_decay=0.99, epsilon_min=0.01):
        self.state_size = state_size
        self.action_size = action_size
        self.batch_size = batch_size
        self.memory = deque(maxlen=2000)
        self.gamma = gamma    # discount
        self.epsilon = epsilon
        self.epsilon_decay = epsilon_decay
        self.epsilon_min = epsilon_min
        self.learning_rate = learning_rate
        self.model = self._build_model()
        

    def _build_model(self):
        model = models.Sequential()
        model.add(layers.Dense(64, input_dim=self.state_size, activation='relu'))
        model.add(layers.Dense(32, activation='relu'))
        model.add(layers.Dense(self.action_size, activation='linear'))
        model.compile(loss='mse', optimizer=optimizers.Adam(learning_rate=self.learning_rate))
        return model
    
    def remember(self, state, action, reward, next_state, over):
        self.memory.append((state, action, reward, next_state, over))
            
    def act(self, state):
            # Epsilon-greedy policy
            if np.random.rand() <= self.epsilon:
                return random.randrange(self.action_size)
            q_values = self.model.predict(state)
            return np.argmax(q_values[0])
        
    def replay(self):
        # Train model with random batch from memory - minibatch
        if len(self.memory) < self.batch_size:
            return
        minibatch = random.sample(self.memory, self.batch_size)
        for state, action, reward, next_state, over in minibatch:
            target = reward
            if not over:
                target += self.gamma * np.amax(self.model.predict(next_state)[0])
            target_f = self.model.predict(state)
            target_f[0][action] = target
            self.model.fit(state, target_f, epochs=1, verbose=0)
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay