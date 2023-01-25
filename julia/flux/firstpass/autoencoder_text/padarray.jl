#!/usr/bin/env julia


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


n_chars = 128

# Define a test text string
test_text = "This is a test text string to be denoised by the autoencoder."
test_arr = collect(test_text)

println(test_arr)

# Pad the test text string to the maximum length
test_text_padded = pad_array(test_arr,n_chars,'0',:right)