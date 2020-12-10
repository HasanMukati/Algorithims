import java.util.*;
import java.io.*;
import java.util.Scanner;
import java.time.*;

/*
* This class is here to help you to verify that your algorithm is correct. You should not modify anything in this file.
* We have provided 7 tests for you. In here, we run all 7 test cases on both your D&C implementation as well as a quadratic impelmentation
* If your algorithm is correct, you should see that both algorithms give the same answer, 
* but the D&C implementation will run faster for larger inputs. 
* The "big.txt" test ran approximately 10x longer for quadratic than for D&C on our machines.
* If the answers to the two problems are different (by more than floating-point error) then your algorithm does not produce the correct answer.
* If the running times are close for large inputs then your algorithm is not actually nlogn time.
* After you submit, we'll re-run your code on similar (but different) tests.
* If you get the correct answer, the running times seem reasonable, and you follow directions, then you can expect full marks on this assignment.
*/

public class ClosestPairTester{
    public static String[] tests = {"small.txt", "medium.txt", "vertical.txt", "horizontal.txt", "runway.txt", "exponential.txt", "big.txt"};
    
    // Test case descriptions:    
    // small.txt: a small number of random points
    // medium.txt: a medium number of random points
    // vertical.txt: all points have the same x coordinate
    // horizontal.txt: all points have the same y coordinate
    // runway.txt: points near to each other in the x dimension, but distant in the y dimension
    // exponential.txt: points are arranged in columns with exponentially-large gaps between columns
    // big.txt: a large number of random points
    
    public static Point[] read_test(String filename){
        ArrayList<Point> points = new ArrayList<Point>();
        File test_file = new File(filename);
        try{
            Scanner filereader = new Scanner(test_file);
            while (filereader.hasNextLine()) {
                String line = filereader.nextLine();
                double x = Double.parseDouble(line.split(" ")[0]);
                double y = Double.parseDouble(line.split(" ")[1]);
                Point p = new Point(x,y);
                points.add(p);
            }
            filereader.close();
        }
        catch(Exception e){
            System.out.println(e);
        }
      return points.toArray(new Point[points.size()]);
    }
    
    public static void main(String[] args){
        for(int i = 0; i < tests.length; i++){
            String test_file = tests[i];
            Point[] test_points = read_test(test_file);
            System.out.println("Running " + test_file);
            System.out.println("input size: " + test_points.length);
            
            System.out.println("Divide and Conquer");
            Instant before = Instant.now();
            double d = ClosestPair.closest_pair(test_points);
            Instant after = Instant.now();
            System.out.println("distance: " + d + " time: " + Duration.between(before, after).toMillis());
            
            System.out.println("Quadratic");
            before = Instant.now();
            d = ClosestPair.quadratic_closest(test_points).getKey();
            after = Instant.now();
            System.out.println("distance " + d + " time: " + Duration.between(before, after).toMillis());
            
            System.out.println();
        }
    }
}
