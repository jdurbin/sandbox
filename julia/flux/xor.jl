#!/usr/bin/env julia 

# Example from:
# https://fluxml.ai/Flux.jl/stable/models/quickstart/

using Flux, Statistics, ProgressMeter

# Generate some data for the XOR problem: vectors of length 2, as columns of a matrix:
noisy = rand(Float32, 2, 1000)                                    # 2×1000 Matrix{Float32}
truth = [xor(col[1]>0.5, col[2]>0.5) for col in eachcol(noisy)];   # 1000-element Vector{Bool}

# Define our model, a multi-layer perceptron with one hidden layer of size 3:
model = Chain(
    Dense(2 => 3, tanh),   # activation function inside layer
    BatchNorm(3),
    Dense(3 => 2),
    softmax) |> gpu 
	
# The model encapsulates parameters, randomly initialised. Its initial output is:
out1 = model(noisy |> gpu) |> cpu                                 # 2×1000 Matrix{Float32}

# To train the model, we use batches of 64 samples, and one-hot encoding:
target = Flux.onehotbatch(truth, [true, false])                   # 2×1000 OneHotMatrix
loader = Flux.DataLoader((noisy, target) |> gpu, batchsize=64, shuffle=true);
# 16-element DataLoader with first element: (2×64 Matrix{Float32}, 2×64 OneHotMatrix)

optim = Flux.setup(Flux.Adam(0.01), model)  # will store optimiser momentum, etc.

# Training loop, using the whole data set 1000 times:
losses = []
@showprogress for epoch in 1:1_000
    for (x, y) in loader
        # The do block creates an anonymous function, as the first argument of gradient. Anything executed within this is differentiated.
        loss, grads = Flux.withgradient(model) do m
            # Evaluate model and loss inside gradient context:
            y_hat = m(x)
            Flux.crossentropy(y_hat, y)
        end
        Flux.update!(optim, model, grads[1])
        push!(losses, loss)  # logging, outside gradient context
    end
end


#optim # parameters, momenta and output have all changed
#out2 = model(noisy |> gpu) |> cpu  # first row is prob. of true, second row p(false)

performance = mean((out2[1,:] .> 0.5) .== truth)  # accuracy > 94% so far!

println("performance: $performance")



# All with julia 1.8.5
# MBP: 
# ./xor.jl  55.28s user 1.45s system 98% cpu 57.321 total 
# ./xor.jl  59.60s user 1.71s system 98% cpu 1:02.30 total (progress bar time: Time: 0:00:41)

# RND (no GPU)
# real	1m15.063s  (progress bar time:  Time: 0:00:57)

# P2 w/ gpu.   Abysmal. 
# real	2m34.151s (progress bar time: Time: 0:01:34)

# c5.2xlarge
# real	0m52.203s (progress bar time: Time: 0:00:37)

# p3.2x no gpu
# real	1m12.934s (Time: 0:00:51)

# p3.2x NVIDIA DL AMI w/ gpu.   Also abysmal. 
# real	2m30.119s (Time: 0:01:35)




