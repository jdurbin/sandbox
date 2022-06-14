
import java.awt.*;
import java.awt.Color;
import java.awt.event.MouseListener;
import java.awt.event.MouseEvent;
import java.awt.event.MouseWheelEvent;
import java.awt.event.MouseMotionListener;
import java.awt.event.MouseWheelListener;
import java.text.NumberFormat;


class ContactHeatmap{
	public static void plotMatrix(int[][] matrix,Graphics g,int pixelsize){
		// Clear it first. 
	    g.setColor(Color.BLACK);
	    g.fillRect(0, 0, matrix.length, matrix.length);	
			
		for(int row = 0;row < matrix.length;row++){
			for(int col = 0;col< matrix.length;col++){	
				int count = matrix[row][col];
				int alpha = (int)count*25;
				alpha = (alpha > 255) ? 255 : alpha;
				int red = 250;
				int grn = 150;
				int blu = 0;
				Color colour = new java.awt.Color(red,grn,blu,alpha);
				g.setColor(colour);
				g.fillRect(col * pixelsize, row * pixelsize, pixelsize, pixelsize);
			}	
		}
	}
}