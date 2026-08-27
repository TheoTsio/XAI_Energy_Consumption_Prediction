import torch
import torch.nn as nn

class CNNModel(nn.Module):
    def __init__(self, input_size, num_filters=128, kernel_size=9, output_size=1):
        super(CNNModel, self).__init__()
        self.conv1 = nn.Conv1d(in_channels=input_size, out_channels=num_filters,
                                kernel_size=kernel_size, padding=kernel_size // 2)
        self.conv2 = nn.Conv1d(in_channels=num_filters, out_channels=num_filters * 2,
                                kernel_size=kernel_size, padding=kernel_size // 2)
        self.relu = nn.ReLU()
        self.pool = nn.AdaptiveAvgPool1d(1)   # collapse time dimension -> works for any seq_length
        self.fc = nn.Linear(num_filters * 2, output_size)

    def forward(self, x):
        # x: (batch, seq_length, n_features) -> (batch, n_features, seq_length)
        x = x.permute(0, 2, 1).contiguous()
        x = self.relu(self.conv1(x))
        x = self.relu(self.conv2(x))
        x = self.pool(x).squeeze(-1)   # (batch, num_filters*2)
        out = self.fc(x)
        return out