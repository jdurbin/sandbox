Tried to precompile a sysimage from Gadfly instructions, but when I tried to run it like: 

julia --sysimage $HOME/JuliaGadflySysImage/GadFlySysimage.so hello.jl 

it laboriously downloaded MKL and then complained about failing to precompile Rdatasets

Obviously I somehow have to add RDataset and other stuff to the precompiled image. 


Attempt1: 

Just run julia like: 

julia --sysimage $HOME/JuliaGadflySysImage/GadFlySysimage.so

Then at the REPL just add the RDatasets package.   Then see if running script as above works:

This resulted in more dependency issues. 

