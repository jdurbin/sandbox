#!/usr/bin/env julia 

# From: 
# https://discourse.julialang.org/t/flux-vs-pytorch-cpu-performance/42667
#
# Note that had to rebuild PyCall to use python where pytorch was installed. 
# 
# Specifically: 
# ENV["PYTHON"]=/Users/james/miniconda3/envs/pytorch/bin/python
# Pkg.build("PyCall")

using PyCall
using Flux
using BenchmarkTools
using CUDA
    
println("CUDA Functional: $(CUDA.functional())")	
	
torch = pyimport("torch")

NN = torch.nn.Sequential(
    torch.nn.Linear(8, 64),
    torch.nn.Tanh(),
    torch.nn.Linear(64, 32),
    torch.nn.Tanh(),
    torch.nn.Linear(32, 2),
    torch.nn.Tanh()
)

torch_nn(in) = NN(in)

Flux_nn = Chain(Dense(8,64,tanh),
                Dense(64,32,tanh),
                Dense(32,2,tanh))

for i in [1, 10, 100, 1000]
    println("Batch size: $i")
    torch_in = torch.rand(i,8)
    flux_in = rand(Float32,8,i)
    print("pytorch:")
    @btime torch_nn($torch_in)
    print("flux   :")
    @btime Flux_nn($flux_in)
end

# MBP
# ./flux_vs_pytorch.jl  133.58s
# Batch size: 1
# pytorch:  45.987 μs (5 allocations: 176 bytes)
# flux   :  1.166 μs (6 allocations: 1.16 KiB)
# Batch size: 10
# pytorch:  54.759 μs (5 allocations: 176 bytes)
# flux   :  3.060 μs (6 allocations: 8.19 KiB)
# Batch size: 100
# pytorch:  95.484 μs (5 allocations: 176 bytes)
# flux   :  19.894 μs (8 allocations: 77.09 KiB)
# Batch size: 1000
# pytorch:  430.860 μs (5 allocations: 176 bytes)
# flux   :  314.271 μs (10 allocations: 766.06 KiB)

# P3 instance (not known if gpu is used, but assume not)
# Batch size: 1
# pytorch:  108.706 μs (5 allocations: 176 bytes)
# flux   :  3.604 μs (6 allocations: 1.16 KiB)
# Batch size: 10
# pytorch:  127.944 μs (5 allocations: 176 bytes)
# flux   :  7.380 μs (6 allocations: 8.19 KiB)
# Batch size: 100
# pytorch:  185.100 μs (5 allocations: 176 bytes)
# flux   :  37.521 μs (8 allocations: 77.09 KiB)
# Batch size: 1000
# pytorch:  407.048 μs (5 allocations: 176 bytes)
# flux   :  221.666 μs (10 allocations: 766.06 KiB)
# 




# nvcc: NVIDIA (R) Cuda compiler driver
# Copyright (c) 2005-2019 NVIDIA Corporation
# Built on Sun_Jul_28_19:07:16_PDT_2019
# Cuda compilation tools, release 10.1, V10.1.243
