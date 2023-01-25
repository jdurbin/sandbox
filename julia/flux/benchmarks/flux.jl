#!/usr/bin/env julia 

# From: 
# https://discourse.julialang.org/t/flux-vs-pytorch-cpu-performance/42667
#
# Note that had to rebuild PyCall to use python where pytorch was installed. 
# 
# Specifically: 
# ENV["PYTHON"]=/Users/james/miniconda3/envs/pytorch/bin/python
# 

using PyCall
using Flux
using BenchmarkTools
using CUDA

cudaFunctional = CUDA.functional()
println("CUDA Functional: $cudaFunctional")

#Flux_nn = Chain(Dense(8,64,tanh),
#                Dense(64,32,tanh),
#                Dense(32,2,tanh)) |> gpu

Flux_nn = Chain(Dense(8,64,tanh),
                Dense(64,32,tanh),
                Dense(32,2,tanh)) 

for i in [20000000]
    println("Batch size: $i")
    flux_in = rand(Float32,8,i)
	#flux_in_gpu = CUDA.CuArray(flux_in)
    @btime Flux_nn($flux_in)
end


# With GPU: 
#Batch size: 1
#flux   :  99.232 μs (144 allocations: 7.08 KiB)
#Batch size: 10
#flux   :  97.395 μs (145 allocations: 7.09 KiB)
#Batch size: 100
#flux   :  92.560 μs (146 allocations: 7.11 KiB)
#Batch size: 1000
#flux   :  95.001 μs (153 allocations: 7.22 KiB)
#real	1m24.922s
#user	1m18.993s
#sys	0m4.907s


# Without GPU: 
# Batch size: 1
# flux   :  3.585 μs (6 allocations: 1.16 KiB)
# Batch size: 10
# flux   :  7.328 μs (6 allocations: 8.19 KiB)
# Batch size: 100
# flux   :  31.234 μs (8 allocations: 77.09 KiB)
# Batch size: 1000
# flux   :  288.609 μs (10 allocations: 766.06 KiB)
# real	0m50.486s
# user	1m3.605s
# sys	0m15.367s


# Let's look at something that might make a difference: 
# 50M, no GPU 
# Batch size: 50000000
# 32.110 s (12 allocations: 36.51 GiB)
# real	2m36.551s


# So 50 million runs out of GPU memory: 
# ERROR: LoadError: Out of GPU memory trying to allocate 11.921 GiB
# Effective GPU memory usage: 99.85% (15.758 GiB/15.782 GiB)
# Memory pool usage: 13.411 GiB (15.281 GiB reserved)

# CUDA Functional: true. GPU 
# Batch size: 20000000
#   30.437 ms (224 allocations: 10.67 KiB)
# 
# real	1m3.751s
# user	0m52.712s
# sys	0m4.237s


# No GPU 
# Batch size: 20000000
#   12.710 s (12 allocations: 14.60 GiB)
# 
# real	1m17.492s
# user	1m25.838s
# sys	1m5.394s


# So, rough comparisons, in principle: 
# datapoints		cpu 			gpu 
#    20,000,000		12sec			330ms
#   200,000,000		120sec (2min)	3.30s
# 2,000,000,000 	1200sec (20min)	30.3s

# 