import torch
import torch.nn as nn
import pandas as pd
import numpy as np
from torch.utils.data import Dataset, DataLoader
from sklearn.preprocessing import StandardScaler
import os

class PowerConsumptionDataset(Dataset):
    def __init__(self, data, target_col_idx, seq_length=10):
        """
        Args:
            data (numpy.ndarray): The scaled numeric data.
            target_col_idx (int): The index of the target column (e.g., consumption).
            seq_length (int): Number of previous time steps to use as input.
        """
        self.data = data
        self.target_col_idx = target_col_idx
        self.seq_length = seq_length
        
    def __len__(self):
        return len(self.data) - self.seq_length
        
    def __getitem__(self, idx):
        # Input sequence: shape (seq_length, num_features)
        x = self.data[idx : idx + self.seq_length, :]
        # Target: the power consumption at the next time step
        y = self.data[idx + self.seq_length, self.target_col_idx]
        return torch.tensor(x, dtype=torch.float32), torch.tensor(y, dtype=torch.float32)

class RNNModel(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, output_size=1):
        super(RNNModel, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        
        # We use an LSTM which generally mitigates vanishing gradient issues of standard RNNs
        self.rnn = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)
        
    def forward(self, x):
        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(x.device)
        c0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(x.device)
        
        out, _ = self.rnn(x, (h0, c0))
        # Take the output of the final time step
        out = self.fc(out[:, -1, :])
        return out

def train_rnn():
    # 1. Load data
    data_path = 'Data/merged_nord_with_power.csv'
    # Fallback in case script is run from a nested directory
    if not os.path.exists(data_path):
        data_path = '../Data/merged_nord_with_power.csv'
        
    print(f"Loading data from {data_path}...")
    df = pd.read_csv(data_path)
    
    # 2. Preprocess data
    print("Preprocessing data...")
    # Drop datetime and non-numeric columns
    cols_to_drop = ['Date and Time', 'Horodatage_Début', 'Horodatage_Fin']
    cols_to_drop = [c for c in cols_to_drop if c in df.columns]
    
    df_numeric = df.drop(columns=cols_to_drop)
    # Handle missing values (forward fill and then backward fill)
    df_numeric = df_numeric.ffill().bfill()
    
    # Identify target column: Prefer 'Consommation', fallback to 'Valeur'
    target_col_name = 'Consommation'
    if target_col_name not in df_numeric.columns:
        if 'Valeur' in df_numeric.columns:
            target_col_name = 'Valeur'
        else:
            raise ValueError("Target column not found purely! Ensure the CSV contains power targets.")
            
    target_idx = df_numeric.columns.get_loc(target_col_name)
    
    # Scale data for better neural network training
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(df_numeric.values)
    
    # 3. Create Dataset and DataLoader
    seq_length = 12 # Represents e.g., the last 2 hours if data is 10min intervals
    dataset = PowerConsumptionDataset(data_scaled, target_col_idx=target_idx, seq_length=seq_length)
    
    # Time-series aware split (using Subsets avoids random shuffling across time boundaries)
    train_size = int(0.8 * len(dataset))
    val_size = len(dataset) - train_size
    train_dataset = torch.utils.data.Subset(dataset, range(0, train_size))
    val_dataset = torch.utils.data.Subset(dataset, range(train_size, len(dataset)))
    
    batch_size = 64
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True) # Shuffle train batches is fine
    val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)
    
    # 4. Initialize Model, Loss Function, Optimizer
    input_size = data_scaled.shape[1]
    hidden_size = 64
    num_layers = 2
    
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = RNNModel(input_size, hidden_size, num_layers).to(device)
    
    criterion = nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
    
    # 5. Training loop
    num_epochs = 20
    print(f"Starting training on {device}...")
    
    for epoch in range(num_epochs):
        model.train()
        train_loss = 0.0
        
        for X_batch, y_batch in train_loader:
            X_batch, y_batch = X_batch.to(device), y_batch.to(device)
            
            optimizer.zero_grad()
            outputs = model(X_batch)
            loss = criterion(outputs.squeeze(), y_batch)
            loss.backward()
            optimizer.step()
            
            train_loss += loss.item() * X_batch.size(0)
            
        train_loss /= train_size
        
        # Validation
        model.eval()
        val_loss = 0.0
        with torch.no_grad():
            for X_batch, y_batch in val_loader:
                X_batch, y_batch = X_batch.to(device), y_batch.to(device)
                
                outputs = model(X_batch)
                loss = criterion(outputs.squeeze(), y_batch)
                val_loss += loss.item() * X_batch.size(0)
                
        val_loss /= val_size
        
        if (epoch + 1) % 5 == 0 or epoch == 0:
            print(f'Epoch [{epoch+1:02d}/{num_epochs}], Train Loss (MSE): {train_loss:.4f}, Val Loss (MSE): {val_loss:.4f}')
            
    # Save the model ensuring directory exists
    os.makedirs('saved_models', exist_ok=True)
    save_path = 'saved_models/rnn_power_consumption.pth'
    torch.save(model.state_dict(), save_path)
    print(f"Training complete! Model saved perfectly to {save_path}")

if __name__ == '__main__':
    train_rnn()
