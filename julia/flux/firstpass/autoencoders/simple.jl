
# https://discourse.julialang.org/t/why-does-binarycrossentropy-needs-an-index-in-a-denoising-autoencoder/41013

using Flux, Random

data = rand(2000, 100)
data_corrupted = copy(data)

# Corrupt data
for sample_index in 1:size(data)[2]
    # Create random indices
    rng = MersenneTwister(1234)
    indices = findall(bitrand(rng, 2000) .> 0)

    # Change values at indices to 0
    for i in 1:size(indices)[1]
        data_corrupted[indices[i], sample_index] = 0
    end
end

# Partition into batches of 10
data = [data[:, i:min(i + 10 - 1, size(data, 2))] for i in 1:10:size(data, 2)]
data_corrupted = [data_corrupted[:, i:min(i + 10 - 1, size(data_corrupted, 2))] for i in 1:10:size(data_corrupted, 2)]

# Define model
encoder = Dense(2000, 50, σ)
decoder = Dense(50, 2000, σ)
m = Chain(encoder, decoder)

# Defining the loss function
#loss(x, y) = Flux.crossentropy(m(x), y)
loss(x, y) = Flux.binarycrossentropy(m(x), y)

# Defining the optimiser
opt = ADAM()

# Train

ps = Flux.params(m)
Flux.train!(loss,ps, zip(data_corrupted, data), opt)