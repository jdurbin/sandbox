module Cooler

using HDF5
function matrix(coolName,startCoord,endCoord,resolution)
	attrs = h5readattr(coolName,resolution)
	binsize = attrs["bin-size"]

	binStart = startCoord/binsize
	binEnd = endCoord/binsize
	matwidth = floor(Int,binEnd-binStart+1)

	matrix = zeros(1,1)
	h5open(coolName) do cin
		onek=cin[resolution]
		pixels = onek["pixels"]
		bin1_id = read(pixels,"bin1_id")
		bin2_id = read(pixels,"bin2_id")
		count = read(pixels,"count")
	
		matrix = zeros(matwidth,matwidth)
		nnv = length(count)
		for binIdx in 1:nnv
			row = bin1_id[binIdx]+1
			col = bin2_id[binIdx]+1				
			if (row <= matwidth) && (col <= matwidth)
				matrix[row,col] = count[binIdx]		
			end
		end
	end
	return matrix
end



end