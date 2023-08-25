// Java program to implement
// sequence alignment problem.
import java.io.*;
import java.util.*;
import java.lang.*;

// From: 
// https://www.geeksforgeeks.org/sequence-alignment-problem/

class NeedlemanWunsch{
	int dp[][];
	int xans[];
	int yans[];
	
	int pxy;
	int pgap;
	
	String x;
	String y;
	int m;
	int n;
	int l;
	int id;
		
	public NeedlemanWunsch(String xin,String yin,int pxin, int pgapin){	
		m = xin.length(); // length of seq1
		n = yin.length(); // length of seq2
		
		x = xin;
		y = yin;
		pxy =pxin;
		pgap = pgapin;
	
		// table for storing optimal substructure answers
		dp = new int[n + m + 1][n + m + 1];						
	}
		
	// function to find out the minimum penalty
	void findMinPenalty(){
		int i, j; // initialising variables
		
		System.err.println("CHECK0");
	
		System.err.println("dp:  "+dp);	
		for (int[] x1 : dp)
			Arrays.fill(x1, 0);

		// initialising the table
		for (i = 0; i <= (n + m); i++){
			dp[i][0] = i * pgap;
			dp[0][i] = i * pgap;
		}
		
		System.err.println("CHECK1");

		// calculating the minimum penalty
		for (i = 1; i <= m; i++){
			for (j = 1; j <= n; j++){
				if (x.charAt(i - 1) == y.charAt(j - 1)){
					dp[i][j] = dp[i - 1][j - 1];
				}else{
					dp[i][j] = Math.min(Math.min(dp[i - 1][j - 1] + pxy ,
						dp[i - 1][j] + pgap) ,
							dp[i][j - 1] + pgap );
				}
			}
		}				
	}
	
	int getMinPenalty(){
		return(dp[m][n]);
	}
	
	ArrayList getAlignment(){
		// Reconstructing the solution
		l = n + m; // maximum possible length
	
		int i = m; 
		int j = n;
		int xpos = l;
		int ypos = l;

		// Final answers for the respective strings
		xans = new int[l + 1];
		yans = new int[l + 1];
	
		while ( !(i == 0 || j == 0)){
			if (x.charAt(i - 1) == y.charAt(j - 1)){
				xans[xpos--] = (int)x.charAt(i - 1);
				yans[ypos--] = (int)y.charAt(j - 1);
				i--; j--;
			}else if (dp[i - 1][j - 1] + pxy == dp[i][j]){
				xans[xpos--] = (int)x.charAt(i - 1);
				yans[ypos--] = (int)y.charAt(j - 1);
				i--; j--;
			}else if (dp[i - 1][j] + pgap == dp[i][j]){
				xans[xpos--] = (int)x.charAt(i - 1);
				yans[ypos--] = (int)'_';
				i--;
			}else if (dp[i][j - 1] + pgap == dp[i][j]){
				xans[xpos--] = (int)'_';
				yans[ypos--] = (int)y.charAt(j - 1);
				j--;
			}
		}
		
		while (xpos > 0){
			if (i > 0) xans[xpos--] = (int)x.charAt(--i);
			else xans[xpos--] = (int)'_';
		}
		
		while (ypos > 0){
			if (j > 0) yans[ypos--] = (int)y.charAt(--j);
			else yans[ypos--] = (int)'_';
		}

		// Since we have assumed the answer to be n+m long, we need to remove 
		// the extra gaps in the 
		// starting id represents the index from
		// which the arrays xans,yans are useful
		id = 1;
		for (i = l; i >= 1; i--){
			if ((char)yans[i] == '_' && (char)xans[i] == '_'){
				id = i + 1;
				break;
			}
		}		
		ArrayList rval = new ArrayList();
		rval.add(xans);
		rval.add(yans);
		System.err.println("DEBUG xans: "+xans);
		return(rval);
	}	
	
	ArrayList align(){
		System.err.println("findMinPenalty");
		findMinPenalty();
		System.err.println("getAlignment");
		return(getAlignment());
	}
	
	void printAlign(){
		System.err.println("id: "+id);
		System.err.println("l: "+l);
		System.err.println("xans: "+xans);
		for (int i = id; i <= l; i++){
			System.out.print((char)xans[i]);
		}
		System.out.print("\n");
		for (int i = id; i <= l; i++){
			System.out.print((char)yans[i]);
		}
	}
	
}


// Printing the final answer
//System.out.print("Minimum Penalty in " +"aligning the genes = ");
//System.out.print(dp[m][n] + "\n");

/*
System.out.println("The aligned genes are :");
for (i = id; i <= l; i++){
	System.out.print((char)xans[i]);
}
System.out.print("\n");
for (i = id; i <= l; i++){
	System.out.print((char)yans[i]);
}
*/