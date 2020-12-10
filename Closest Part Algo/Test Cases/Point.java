public class Point implements Comparable<Point>{

    public double x;
    public double y;
    
    public Point(double x, double y){
        this.x = x;
        this.y = y;
    }
    
    public String toString(){
        return "(" + this.x + "," + this.y +  ")";
    }
    
    public int compareTo(Point p){
        if(this.x != p.x){
            return this.x - p.x < 0 ? -1 : 1;
        }
        return this.y - p.y < 0 ? -1 : 1;
    }
}
