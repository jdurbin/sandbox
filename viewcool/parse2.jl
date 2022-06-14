#!/usr/bin/env julia

using HDF5
using Cooler

coolName = "MB286.mcool"

startCoord=1000
endCoord = 10000000
resolution = "resolutions/1000"
#resolution = "resolutions/2000"
resolution = "resolutions/16000"


attrs = h5readattr(coolName,resolution)
binsize = attrs["bin-size"]

binStart = startCoord/binsize
binEnd = endCoord/binsize
matwidth = floor(Int,binEnd-binStart+1)

println("binStart: ",binStart,"\tbinEnd: ",binEnd,"\tmatwidth: ",matwidth)


h5open(coolName) do cin
	onek=cin[resolution]
	pixels = onek["pixels"]
	bin1_id = read(pixels,"bin1_id")
	bin2_id = read(pixels,"bin2_id")
	count = read(pixels,"count")
	
	println("countlen:",length(count))
	
	matrix = zeros(matwidth,matwidth)
	println("matrix len:",length(matrix))
	nnv = length(count)
	for binIdx in 1:nnv
#	for binIdx in 1:100  
		row = bin1_id[binIdx]+1
		col = bin2_id[binIdx]+1		
		
		#println("binIdx:",binIdx,"\trow:",row,"\tcol:",col,"\tcount:",count[binIdx])
		
		if (row <= matwidth) && (col <= matwidth)
			matrix[row,col] = count[binIdx]		
		end
	end
end


#resolution/2000
#binStart: 0.5	binEnd: 5000.0	matwidth: 5000
#countlen:10,350,414
#matrix len:25,000,000

# resolution/1000
# binStart: 1.0	binEnd: 10000.0	matwidth: 10000
# countlen:13,754,067
# matrix len:100,000,000
