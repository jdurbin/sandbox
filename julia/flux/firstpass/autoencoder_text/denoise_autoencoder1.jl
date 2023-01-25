#!/usr/bin/env julia 

# based on starter code from chatGPT

using Flux
using Flux.Data: shuffleobs
using Flux: onehotbatch
using Flux: onehot
using Flux: throttle
using Flux: crossentropy
using Flux: train!
using Flux: mse
using Flux: ADAM
# using Flux: PaddedArray
# using Flux: @diff


# Define the maximum length of the input text strings
max_len = 120

# Define the number of unique characters in the text
n_chars = 128

# Define the number of neurons in the encoder and decoder layers
n_encoder = 128
n_decoder = 128

# Define the noise probability for the denoising process
noise_prob = 0.5


function softmax(x::AbstractVector)
    # Compute the exponential of each element in the input vector
    exp_x = exp.(x)

    # Normalize the exponential values by dividing by the sum of the exponentials
    norm_exp_x = exp_x ./ sum(exp_x)

    return norm_exp_x
end


function pad_array(arr::Array, final_length::Int, padval::Char, direction::Symbol)
    # Calculate the number of padding elements needed
    n_pad = final_length - length(arr)

    # Initialize the padded array
    padded_arr = copy(arr)

    # Add padding elements to the array
    if direction == :left
        for i in 1:n_pad
            pushfirst!(padded_arr, padval)
        end
    elseif direction == :right
        for i in 1:n_pad
            push!(padded_arr, padval)
        end
    end

    return padded_arr
end


# Define the autoencoder model
function autoencoder(max_len, n_chars, n_encoder, n_decoder, noise_prob)	
	
    # Define the encoder and decoder layers
    encoder = Chain(
        LSTM(n_chars, n_encoder),
        Dense(n_encoder, n_encoder)
    )

    decoder = Chain(
        Dense(n_encoder, n_decoder),
        LSTM(n_decoder, n_chars),
        softmax
    )

    # Define the autoencoder model by stacking the encoder and decoder layers
    model = Chain(encoder, decoder)

    # Define the loss function and optimization algorithm
    loss(x, y) = crossentropy(model(x), y)
    opt = ADAM()

    # Define the function for training the autoencoder
    ps = Flux.params(model)
    function train_autoencoder(data, epochs)
		for epoch in 1:2
		   Flux.train!(loss,ps, zip(data), opt)
		end				
    end

    # Define the function for denoising the input text
    function denoise_text(text)
        # Convert the input text to a one-hot encoded tensor
        text_oh = onehotbatch(text, 1:n_chars)

        # Add noise to the input tensor with probability `noise_prob`
        text_noisy = map(x -> x .* (rand(size(x)) .> noise_prob), text_oh)

        # Denoise the input text by passing it through the autoencoder model
        text_denoised = model(text_noisy)

        # Convert the denoised tensor back to text
        return String(argmax(text_denoised, dims=2))
    end

    return model, train_autoencoder, denoise_text
end


# Define a test text string
test_text = "This is a test text string to be denoised by the autoencoder."

# Pad the test text string to the maximum length
test_arr = collect(test_text)
test_text_padded = pad_array(test_arr,n_chars,'0',:right)

# Initialize the autoencoder model
model, train_autoencoder, denoise_text = 
	autoencoder(max_len, n_chars, n_encoder, n_decoder, noise_prob)

# Train the autoencoder model on the test text
train_autoencoder(test_text_padded, 1)

# Denoise the test text using the trained autoencoder model
denoised_text = denoise_text(test_text_padded)

# Print the original and denoised test text
println("Original text:")
println(test_text)
println("Denoised text:")
println(denoised_text)

