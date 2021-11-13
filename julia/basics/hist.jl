#!/usr/bin/env julia

using Plots; plotlyjs()

h1=histogram(randn(1000))

gui(h1)

readline()