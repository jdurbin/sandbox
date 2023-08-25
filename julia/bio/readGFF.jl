#!/usr/bin/env julia

# Import the GFF3 module.
using GenomicFeatures
using GFF3

gff_file = "/mnt/ebs/james/ref/GRCh38/tracks/gencode.v42.annotation.gff3"

# Open a GFF3 file.
reader = open(GFF3.Reader,gff_file)

# Iterate over records.
for record in reader
	gene_name = GFF3.attributes(record,"gene_name")
	if occursin("HLA-",gene_name[1]) && (GFF3.featuretype(record) == "gene")				
		chrom = GFF3.seqid(record)
		start = GFF3.seqstart(record)
		send = GFF3.seqend(record)		
		println("$chrom\t$start\t$send\t$gene_name")
	end
end

# Finally, close the reader
close(reader)


# real	0m6.307s
# Much faster than doing it with pyranges, which takes 1m 47sec to read the db before doing 
# any operations at all. 
