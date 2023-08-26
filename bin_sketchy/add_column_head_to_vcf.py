#!/usr/bin/env python3
import sys,argparse



def main(argv):
    
    if len(argv) < 2 or argv[1] == "-h":
        print("""
        
        add_column_head_to_vcf.py my.vcf
        
        HAPCUT2 doesn't leave the column descriptions in the VCF file, but some tools
        like IGV will not use the VCF file without one.  This is a simple script to 
        add the column header line to a vcf file in-place (i.e. file is overwritten). 
        
        """)
        sys.exit()
   
    vcf_name = argv[1]
    
    # Read entire vcf into a list. 
    with open(vcf_name) as fin:
        vcf_lines = fin.readlines()
        
    # Write out vcf file inserting header before the first line that doesn't contain a # character. 
    first_time = True 
    with open(vcf_name,"w") as fout: 
        for line in vcf_lines:
            if first_time and "#" not in line:
                fout.write("#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\tFORMAT\tsample1\n")
                fout.write(line)
                first_time = False 
            else:
                fout.write(line)



if __name__ == "__main__":
    main(sys.argv)