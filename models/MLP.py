import torch
import torch.nn as nn

class MLPModel(nn.Module):
    def __init__(self, input_size, seq_length, hidden_sizes=(256, 256, 158), output_size=1, dropout=0.2):
        super(MLPModel, self).__init__()
        in_features = input_size * seq_length  # flattened window size

        layers = []
        prev_size = in_features
        for h in hidden_sizes:
            layers.append(nn.Linear(prev_size, h))
            layers.append(nn.ReLU())
            layers.append(nn.Dropout(dropout))
            prev_size = h
        layers.append(nn.Linear(prev_size, output_size))

        self.net = nn.Sequential(*layers)

    def forward(self, x):
        # x: (batch, seq_length, n_features) -> (batch, seq_length * n_features)
        x = x.reshape(x.size(0), -1)
        out = self.net(x)
        return out