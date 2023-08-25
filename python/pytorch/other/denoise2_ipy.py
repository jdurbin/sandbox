# %% 
import torch
import torch.nn as nn
import numpy as np
# %%
class DenoisingAutoencoder(nn.Module):
    def __init__(self, input_size, hidden_size):
        super(DenoisingAutoencoder, self).__init__()
        self.encoder = nn.Linear(input_size, hidden_size)
        self.decoder = nn.Linear(hidden_size, input_size)

    def forward(self, x):
        x = self.encoder(x)
        x = self.decoder(x)
        return x

# %%
# Define a training set of 10 strings
training_strings = ["This is a random sentence",
                    "Another sentence for the training set",
                    "Neural networks are powerful",
                    "Denoising autoencoders are useful",
                    "Training data is important",
                    "Deep learning is the future",
                    "PyTorch is a popular framework",
                    "Natural language processing is complex",
                    "Generative models are exciting",
                    "Machine learning is changing the world"]
# %%
# Define the noise function
def add_noise_to_string(string, noise_level=0.1):
    string = list(string)
    max_noise_length = int(len(string) * noise_level)
    noise = np.random.choice(list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "), 
                              size=max_noise_length, replace=True)
    noise_indices = np.random.choice(range(len(string)), size=max_noise_length, replace=False)
    for i, idx in enumerate(noise_indices):
        string[idx] = noise[i]
    return "".join(string)


# %%
# Convert string to numerical representation 
import torch.nn.functional as F
def str_to_tensor(string):
    one_hot_encoding = F.one_hot(torch.tensor([ord(c) for c in string]), num_classes=256).float()
    return one_hot_encoding.view(1, -1)

# Convert numerical representation back to string
def tensor_to_str(tensor):
    string_decoded = [chr(int(x)) for x in tensor.tolist()]
    return "".join(string_decoded)

# %%
input_size = 100
hidden_size = 32
model = DenoisingAutoencoder(input_size, hidden_size)
criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters())
# %%
input_string = training_strings[0]
input_string

#%%
one_hot_encoding = F.one_hot(torch.tensor([ord(c) for c in input_string]), num_classes=256).float()
one_hot_encoding 

# %%
num_epochs = 10
for epoch in range(num_epochs):
    for input_string in training_strings:
        input_tensor = str_to_tensor(input_string)
        noisy_string = add_noise_to_string(input_string)
        noisy_tensor = str_to_tensor(noisy_string)
        output_tensor = model(noisy_tensor)
        loss = criterion(output_tensor, input_tensor)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    print("Epoch: {}/{}  Loss: {:.4f}".format(epoch+1, num_epochs, loss.item()))
# %%
