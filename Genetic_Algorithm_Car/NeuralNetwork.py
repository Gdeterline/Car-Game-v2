import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim

class NeuralNetwork(nn.Module):
    def __init__(self, input_layer, hidden_layer, output_layer):
        super(NeuralNetwork, self).__init__()
        # We will use 2 hidden layers - the NN should beas follows [14, 128, 64, 1]
        self.layer1 = nn.Linear(input_layer, hidden_layer)
        self.layer2 = nn.Linear(hidden_layer, output_layer)

    def forward(self, x):
        x = self.layer1(x)
        x = torch.sigmoid(x)
        x = self.layer2(x)
        x = torch.sigmoid(x)
        return x

    def get_weights(self):
        pass

    def set_weights(self, weights):
        pass