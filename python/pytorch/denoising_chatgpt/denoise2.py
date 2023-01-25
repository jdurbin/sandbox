
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

# Define the noise function
def add_noise_to_string(string, noise_level=0.1):
    noise = "".join(np.random.choice(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"], 
                                      int(len(string) * noise_level))
                   )
    noised_string = "".join([noise[i] if np.random.rand() < noise_level else string[i] for i in range(len(string))])
    return noised_string

# Convert string to numerical representation 
def str_to_tensor(string):
    string_encoded = [ord(c) for c in string]
    return torch.tensor(string_encoded, dtype=torch.float)

# Convert numerical representation back to string
def tensor_to_str(tensor):
    string_decoded = [chr(int(x)) for x in tensor.tolist()]
    return "".join(string_decoded)

input_size = 100
hidden_size = 32
model = DenoisingAutoencoder(input_size, hidden_size)
criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters())

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

# test the model
with torch.no_grad():
    test_string = "This is a test sentence"
    test_tensor = str_to_tensor(test_string)
    noisy_test_string = add_noise_to_string(test_string)
    noisy_test_tensor = str_to_tensor(noisy_test_string)
    output_tensor = model(noisy_test_tensor)
    output_string = tensor_to_str(output_tensor)
    print("Original string: {}".format(test_string))
    print("Noised string: {}".format(noisy_test_string))
    print("Output string: {}".format(output_string))

