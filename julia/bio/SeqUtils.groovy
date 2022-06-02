/*******
* Some syntatic sugar so that we can do simple sequence manipulation without having to 
* deal with all of the boilerplate stuff. 
*/ 

@Grab(group='openchart', module='openchart', version='1.4.2')
@Grab(group='org.biojava', module='biojava-core', version='6.0.5')
@Grab(group='org.biojava', module='biojava-alignment', version='6.0.5')
@Grab(group='org.biojava.thirdparty', module='forester', version='1.039')
@Grab(group='org.biojava', module='biojava-phylo', version='5.0.0-alpha6')


import java.io.*
import java.util.*
import org.biojava.nbio.core.sequence.*
import org.biojava.nbio.core.sequence.compound.*
import org.biojava.nbio.core.sequence.io.*
import org.biojava.nbio.core.util.*
import org.biojava.nbio.core.sequence.template.Compound
import org.biojava.nbio.core.exceptions.*
import org.biojava.nbio.core.sequence.*
import org.biojava.nbio.core.sequence.compound.*
import org.biojava.nbio.core.sequence.io.template.*
import org.biojava.nbio.core.sequence.io.template.SequenceHeaderParserInterface
import org.biojava.nbio.core.sequence.template.AbstractSequence.AnnotationType
import org.biojava.nbio.core.sequence.template.AbstractSequence
import org.slf4j.Logger
import org.slf4j.LoggerFactory
import java.util.ArrayList

import org.biojava.nbio.alignment.*
import org.biojava.nbio.alignment.Alignments.PairwiseSequenceAlignerType
import org.biojava.nbio.alignment.template.*
import org.biojava.nbio.alignment.SimpleGapPenalty
import org.biojava.nbio.core.alignment.matrices.SubstitutionMatrixHelper


/*******
* Some syntatic sugar so we don't have to think about all of this plumbing
* for common use cases.  
*/ 
public class SeqUtils{	

	// Replace header parser with one of my own creation...	
	static class MyFastaHeaderParser<S extends AbstractSequence<C>, C extends Compound>
		implements SequenceHeaderParserInterface<S, C> {

		@Override
		public void parseHeader(String header, S sequence) {
			sequence.setOriginalHeader(header);
			def name = header.split(" ")[0]
			sequence.setAccession(new AccessionID(name));
		}
	}
	
	/***
	* Reads in sequences from a fasta file and returns a map from sequence names to 
	* sequence. 
	*/ 
	static def readFastaMap(InputStream inStream){
		def fastaReader = new FastaReader<DNASequence, NucleotideCompound>(inStream,
			new MyFastaHeaderParser(),
			new DNASequenceCreator(DNACompoundSet.getDNACompoundSet()))	  
			return fastaReader.process()
	}
	
	static def localAlignPair(seq1,seq2){
		def mat = SubstitutionMatrixHelper.getNuc4_4()
		GapPenalty penalty = new SimpleGapPenalty(5,1);		
		def pair = Alignments.getPairwiseAlignment(seq1,seq2,PairwiseSequenceAlignerType.LOCAL,penalty,mat)
		return(pair)
	}
}
	
	
	
			