// Hasan Mukati
// Algorithms 4102
// Divide and Conquer

// Goal: Implementing closest pair of points.

import java.util.*;
import javafx.util.Pair;
import java.lang.Math;


public class ClosestPair{
    public static double distance(Point p1, Point p2){
        // a function to compute the distance between two points
        // Do not modify this function
        double deltax = p1.x - p2.x;
        double deltay = p1.y - p2.y;
        return Math.sqrt(deltax * deltax + deltay * deltay);
    }

    public static Pair<Double, Point[]> quadratic_closest(Point[] points){
        // A quadratic procedure for finding closest pair of points. Use this for timing comparison.
        // This can also serve as your base case if you'd like.
        // It returns a pair of values: the distance of the closest pair and the list of points re-sorted by y.
        // Do not modify this function
        double closest = Double.MAX_VALUE;
        for(int i = 0; i < points.length; i++){
            Point p1 = points[i];
            for(int j = i+1; j < points.length; j++){
                Point p2 = points[j];
                double d = distance(p1, p2);
                if(d < closest){
                    closest = d;
                }
            }
        }
        Arrays.sort(points, new Comparator<Point>() {
          public int compare(Point p1, Point p2) {
            if(p1.y != p2.y){
                return p1.y - p2.y < 0 ? -1 : 1;
            }
            return p1.x - p2.x < 0 ? -1 : 1;
          }});
        return new Pair<Double, Point[]> (closest, points);
    }

    private static Point[] get_runway(Point[] y_sorted, double median_x, double delta){
        // A procedure to extract all points in the runway
        // I found this function to be useful, but you're not required to implement and use it if you don't want to
        ArrayList<Point> runway = new ArrayList<Point>();
        for(Point point:y_sorted){
            if(Math.abs(point.x-median_x) < delta) runway.add(point);
        }
        Point [] runway_array = new Point[runway.size()];
        return runway.toArray(runway_array);
    }

    private static Point[] merge(Point[] left, Point[] right){
        // A procedure to merge the points by y value
        // You'll almost certainly need to use this one, but it's ok if you don't use it.
        Point[] merged = new Point[left.length + right.length];

        for(int i = 0, j=0, k=0; k < merged.length; k++){
            if(i < left.length && j < right.length){
                if(left[i].y <= right[j].y) {
                    merged[k] = new Point(left[i].x, left[i].y);
                    i++;
                }
                else {
                    merged[k] = new Point(right[j].x, right[j].y);
                    j++;
                }
            } else if(i == left.length) {
                merged[k] = new Point(right[j].x, right[j].y);
                j++;
            } else if(j == right.length) {
                merged[k] = new Point(left[i].x, left[i].y);
                i++;
            }
        }


        return merged;
    }

    public static Pair<Double, Point[]> dc_closest(Point[] x_sorted){
        //The divide and conquer closest pair of points algorithm
        // The input is a list of points sorted by x value
        // The output is a pair comprised of the closest pair of points from among the given points, and the given points re-sorted by y
        // Your assignment is to implement this function. It's required that your algorithm runs in nlogn time, and that it follow the divide and conquer format.
        
        //BASE CASE
        // You'll need to have a base case. I've provided one, but you may change it if you prefer something else
        // We will not run your code on any test cases with fewer than 2 points.
        if(x_sorted.length < 2){
            return quadratic_closest(x_sorted);
        }
        
        //DIVIDE STEP
        // For the divide step, split the list of points into two sub-lists of length n/2
        // Save the median x coordinate, you'll need that later for COMBINE
        int numberOfPoints = x_sorted.length;
        double median_x = x_sorted[numberOfPoints/2].x;
        Point[] leftSetOfPoints = Arrays.copyOfRange(x_sorted, 0, numberOfPoints/2);
        Point[] rightSetOfPoints = Arrays.copyOfRange(x_sorted, numberOfPoints/2, numberOfPoints);
        
        //CONQUER STEP
        // For this step, recursively solve closest pair of points on the two halves
        // You'll need both the distance returned as well as the points sorted by y value
        Pair<Double, Point[]> left_solution = dc_closest(leftSetOfPoints);
        double left_distance = left_solution.getKey();
        Point[] left_y_sorted = left_solution.getValue();

        Pair<Double, Point[]> rightSolution = dc_closest(rightSetOfPoints);
        double right_distance = rightSolution.getKey();
        Point[] right_y_sorted = rightSolution.getValue();

        //COMBINE STEP
        // For this step, you'll need to merge points by y value,
        // identify the points in the "runway",
        // and find the closest pair which crosses the divide
        Point[] merged_points = merge(left_y_sorted, right_y_sorted);
        Point[] runway_points = get_runway(merged_points, median_x, Math.min(left_distance, right_distance));

        double current_min_distance = Double.MAX_VALUE;
        for(int i =0; i<runway_points.length; i++){
            Point p1 = runway_points[i];
            for(int j=i+1; j<i+15 && j<runway_points.length; j++){
                Point p2 = runway_points[j];
                double d = distance(p1, p2);
                if(d < current_min_distance){
                    current_min_distance = d;
                }
            }
        }

        
        //RETURN VALUE
        // The return value will be the distance of the closest pair found and all points sorted by y value
        double min_distance = Math.min(Math.min(left_distance, right_distance), current_min_distance);
        return new Pair<Double, Point[]>(min_distance, merged_points);
    }
    
    public static double closest_pair(Point[] points){
        // Helper function to hide the recursion since the recursive function needs a second return value
        // All this does is sort the points by x, invoke the D&C algorithm, and return only the distance
        Arrays.sort(points);
        Pair<Double, Point[]> ret_val = dc_closest(points);
        return ret_val.getKey();
    }

    private static void print_points(Point[] points){
        System.out.println("Points:");
        for(int i=0; i<points.length; i++){
            System.out.println("(" + points[i].x + " " + points[i].y + ")");
        }
    }

    public static void main(String[]args){
        Point[] points = {
                new Point(1.0, 2.1),
                new Point(2.0, 2.0),
                new Point(3.0, 3.0),
                new Point(4.0, 4.0),
                new Point(6.0, 5.0),
                new Point(5.0, 6.0)
        };


        System.out.println(closest_pair(points));
        Pair<Double, Point[]> return_value_dc = dc_closest(points);
        double distance_dc = return_value_dc.getKey();
        Point[] y_sorted_dc = return_value_dc.getValue();
        System.out.println(distance_dc);
        System.out.println("Points:");
        for(Point point : y_sorted_dc){
            System.out.println(point);
        }

        Pair<Double, Point[]> return_value = quadratic_closest(points); // example invocation of quadratic algorithm
        double distance = return_value.getKey(); // to get the first of the two return values, call getKey() on the pair returned
        Point[] y_sorted = return_value.getValue(); // to get the second of the two return values, call getValue() on the pair returned
        System.out.println(distance);
        System.out.println("Points:");
        for(Point point : y_sorted){
            System.out.println(point);
        }
    }

}
