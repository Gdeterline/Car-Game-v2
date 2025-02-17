import numpy as np

class NeuralNetwork():

    def __init__(self, input_size, hidden_size, output_size):
        self.weights1 = np.random.randn(input_size, hidden_size)
        self.bias1 = np.zeros((1, hidden_size))
        self.weights2 = np.random.randn(hidden_size, output_size)
        self.bias2 = np.zeros((1, output_size))

    def forward(self, inputs):
        x = np.dot(inputs, self.weights1) + self.bias1
        x = np.maximum(0, x) # ReLU activation
        x = np.dot(x, self.weights2) + self.bias2
        return np.tanh(x)

    def get_weights(self):
        return np.concatenate([self.weights1.flatten(), self.bias1.flatten(), 
                                self.weights2.flatten(), self.bias2.flatten()])

    def set_weights(self, weights):
        split1 = self.weights1.size
        split2 = split1 + self.bias1.size
        split3 = split2 + self.weights2.size

        self.weights1 = weights[:split1].reshape(self.weights1.shape)
        self.bias1 = weights[split1:split2].reshape(self.bias1.shape)
        self.weights2 = weights[split2:split3].reshape(self.weights2.shape)
        self.bias2 = weights[split3:].reshape(self.bias2.shape)