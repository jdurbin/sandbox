import torch
from torch import nn
from sklearn.model_selection import train_test_split

train_features, test_features, train_labels, test_labels = train_test_split(
    input_features, input_labels, test_size=0.25, random_state=42)

class MyModel(nn.Module):
    def __init__(self):
        super(MyModel, self).__init__()
        self.conv = nn.Conv1d(in_channels=4, out_channels=32, kernel_size=12)
        self.pool = nn.MaxPool1d(kernel_size=4)
        self.flatten = nn.Flatten()
        self.fc1 = nn.Linear(in_features=32*25, out_features=16)
        self.fc2 = nn.Linear(in_features=16, out_features=2)
        self.relu = nn.ReLU()
        self.softmax = nn.Softmax(dim=1)

    def forward(self, x):
        x = self.conv(x)
        x = self.pool(x)
        x = self.flatten(x)
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        x = self.softmax(x)
        return x

model = MyModel()

criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters())

train_features = torch.tensor(train_features, dtype=torch.float32)
train_labels = torch.tensor(train_labels, dtype=torch.long)

for epoch in range(50):
    optimizer.zero_grad()
    outputs = model(train_features)
    loss = criterion(outputs, train_labels)
    loss.backward()
    optimizer.step()
    
    if epoch % 5 == 0:
        print("Epoch: %d, Loss: %.5f" % (epoch, loss.item()))
