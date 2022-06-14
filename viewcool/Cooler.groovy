import ch.systemsx.cisd.hdf5.HDF5DataSetInformation;
import ch.systemsx.cisd.hdf5.HDF5Factory;
import ch.systemsx.cisd.hdf5.HDF5LinkInformation;
import ch.systemsx.cisd.hdf5.IHDF5Reader;
import ch.systemsx.cisd.hdf5.IHDF5Writer;
import static ch.systemsx.cisd.hdf5.HDF5ObjectType.*;

// https://mvnrepository.com/artifact/ch.systems.cisd/jhdf5



/***********************************************
*
* Methods to manipulate cool files. 
* 
*/
class Cooler{
	
	def err = System.err
	IHDF5Reader h5
	def bin_size
	
	def Cooler(hdf5File){
		err.print "Obtain h5 for $hdf5File..."
		h5 = HDF5Factory.openForReading(hdf5File)
		err.println "done."
	}
	
	def max(matrix){
		def maxVal = -999
		(0..<matrix.length).each{row->
			(0..<matrix[0].length).each{col->
				if(matrix[row][col] > maxVal) maxVal = matrix[row][col]
			}
		}
		return(maxVal)
	}
	
	/****
	* matrix from cool file
	*/ 
	def matFromCool(startCoord,endCoord){
		bin_size=h5.getIntArrayAttribute("/","bin-size")[0]

		def binStart = startCoord/bin_size as int
		def binEnd = endCoord/bin_size as int
		def matwidth = binEnd-binStart +1

		// Read the compressed form of the data
		def bin1_id = h5.readIntArray("/pixels/bin1_id")
		def bin2_id = h5.readIntArray("/pixels/bin2_id")
		def count = h5.readIntArray("/pixels/count")
		//def bin1_offset = h5.readIntArray("/indexes/bin1_offset")
		//def chrom_offset = h5.readIntArray("/indexes/chrom_offset")	
	
		// Copy the nnv values into a dense matrix
		def matrix = new int[matwidth][matwidth]	
		def nnv = count.length
		(0..<nnv).each{binIdx->
			def row = bin1_id[binIdx]
			if ((row < binStart) || (row > binEnd)) return;
			def col = bin2_id[binIdx]
			if ((col < binStart) || (col > binEnd)) return;
	
			matrix[row][col] = count[binIdx]
		}
		return(matrix)
	}
	
	def genomeFromMatIdx(row,col){		
		def startCoord = bin_size*row
		def endCoord = bin_size*col
		return([startCoord,endCoord])
	}
	
	/****
	* matrix from cool file
	*/ 
	def matFromCool(startCoord,endCoord,resolution){
		bin_size=resolution

		def binStart = startCoord/bin_size as int
		def binEnd = endCoord/bin_size as int
		def matwidth = binEnd-binStart +1

		// Read the compressed form of the data
		def bin1_id = h5.readIntArray("resolutions/${resolution}/pixels/bin1_id")
		def bin2_id = h5.readIntArray("resolutions/${resolution}/pixels/bin2_id")
		def count = h5.readIntArray("resolutions/${resolution}/pixels/count")
		//def bin1_offset = h5.readIntArray("/indexes/bin1_offset")
		//def chrom_offset = h5.readIntArray("/indexes/chrom_offset")	
	
		// Copy the nnv values into a dense matrix
		def matrix = new int[matwidth][matwidth]	
		def nnv = count.length
		(0..<nnv).each{binIdx->
			def row = bin1_id[binIdx]
			if ((row < binStart) || (row > binEnd)) return;
			def col = bin2_id[binIdx]
			if ((col < binStart) || (col > binEnd)) return;
	
			matrix[row][col] = count[binIdx]
		}
		return(matrix)
	}


	/****
	* print matrix as tsv
	*/ 
	def printMatrix(matrix){	
		def colnames = []
		colnames << "rowNum"
		0.upto(matrix.length){i-> 
			colnames << "col${i}"
		}
		println colnames.join("\t")
	
		(0..<matrix.length).each{row->
			def rowVals = []
			(0..<matrix[0].length).each{col->
				rowVals<<matrix[row][col]
			}
			println "row"+row+"\t"+rowVals.join("\t")
		}
	}


}