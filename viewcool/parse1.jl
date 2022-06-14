#!/usr/bin/env julia

using HDF5

coolName = "MB286.mcool"

# Read data from a cool file: 
#h5open(coolName) do cin
#	data2 = read(cin,"/resolutions/1000/pixels/bin1_id")
#	println(length(data2))
#end

# You can create objects for different levels of the hdf5
# like so: 
h5open(coolName) do cin
	onek=cin["resolutions/1000"]
	pixels = onek["pixels"]
	data3 = read(pixels,"bin1_id")
	println(length(data3))
end


h5open(coolName) do cin
	onek=cin["resolutions/1000"]
	keyexists = haskey(attributes(onek),"bin-size")
	binsize=read(attributes(onek)["bin-size"])
	println(binsize)
end

attrs = h5readattr(coolName,"resolutions/1000")
println(attrs)

#data1 = h5read(coolName,"/resolutions/1000/pixels/bin1_id")
#println(length(data1))

#println(cin["resolutions"])

# bin_size=h5.getIntArrayAttribute("/","bin-size")[0]
# binsizename=attributes(cin["resolutions"]["1000"])["bin-size"]
