import torch
import torch.nn as nn
import torch.optim as optim

class DenoisingAutoencoder(nn.Module):
    def __init__(self):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Linear(100, 64),
            nn.ReLU(),
            nn.Linear(64, 32),
            nn.ReLU()
        )
        self.decoder = nn.Sequential(
            nn.Linear(32, 64),
            nn.ReLU(),
            nn.Linear(64, 100),
            nn.Sigmoid()
        )

    def forward(self, x):
        x = self.encoder(x)
        x = self.decoder(x)
        return x

# Create the network and the optimizer
net = DenoisingAutoencoder()
optimizer = optim.Adam(net.parameters())

# Define the loss function and the metric for evaluation
criterion = nn.MSELoss()

# Training loop
for i in range(1000):
    # Generate some random DNA sequences and add noise to them
    dna_sequences = torch.randint(0, 4, (100, 100))
    noisy_dna_sequences = dna_sequences + torch.randint(-1, 2, (100, 100))
    noisy_dna_sequences = noisy_dna_sequences.clamp(0, 4)

    # Convert the DNA sequences to one-hot encoded vectors
    dna_sequences = nn.functional.one_hot(dna_sequences, num_classes=5).float()
    noisy_dna_sequences = nn.functional.one_hot(noisy_dna_sequences, num_classes=5).float()

    # Forward pass
    output = net(noisy_dna_sequences)

    # Compute the loss and the metrics
    loss = criterion(output, dna_sequences)

    # Backward pass and optimization
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

# test the model on 10 input strings
test_dna = ["ACTG"*25, "ATAG"*25, "CGGT"*25, "TGAG"*25, "AGGT"*25, "AGAG"*25, "TGAG"*25, "GGTT"*25, "AGGC"*25, "ACTG"*25]
test_dna = [torch.tensor(list(dna), dtype=torch.int) for dna in test_dna]
test_dna_noised = [dna + torch.randint(-1, 2, (100,)) for dna in test_dna]
test_dna_noised = [dna.clamp(0, 4) for dna in test_dna_noised]
test_dna = nn.functional.one_hot(torch.stack(test_dna), num_classes=5).float()
test_dna_noised = nn.functional.one_hot(torch.stack(test_dna_noised), num_classes=5).float()
output = net(test_dna_noised)
for i in range(10):
    print("Original:",''.join([list("ACTGN")[i] for i in test_dna[i].argmax(1)]))
    print("Reconstructed:",''.join([list("ACTGN")[i] for i in output[i].argmax(1)]))

