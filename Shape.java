import java.lang.Math;
import java.util.concurrent.RecursiveAction;

import javax.swing.border.EmptyBorder;

public class Shape{
    String color;
    boolean filled;

    public Shape(){
        this("red",true);
    }

    public Shape(String color,boolean filled){
        this.color = color;
        this.filled = filled;
    }

    public String getColor(){
        return this.color;
    }

    public void setColor(String color){
        this.color = color;
    }

    public boolean isFilled(){
        return this.filled;
    }

    public void setFilled(boolean filled){
        this.filled = filled;
    }

    @Override
    public String toString(){
        StringBuffer output = new StringBuffer("A Shape with color of");
        output.append(color);
        output.append(" and ");
        if (this.filled){
            output.append("filled.");
        }else{
            output.append("not filled.");
        }
        return output.toString();
    }

    public static void main(String[] args){
        Circle a = new Circle();
        System.out.print(a);
    }
}

class Circle extends Shape{
     double radius;

    public Circle(){
        this(1.0);
    }

    public Circle(double radius){
        this.radius = radius;
    }

    public Circle(double radius, String color, boolean filled){
        this.radius = radius;
        this.color = color;
        this.filled = filled;
    }

    public double getRadius(){
        return this.radius;
    }

    public void setRadius(double radius){
        this.radius = radius;
    }

    public double getArea(){
        return (Math.pow(this.radius,2)*Math.PI);
    }

    public double getPerimiter(){
        return (2*Math.PI*this.radius);
    }

    @Override
    public String toString(){
        StringBuffer output = new StringBuffer("A Circle of radius ");
        output.append(this.radius);
        output.append(", which is a subclass of ");
        output.append("A shape colored: ");
        output.append(color);
        output.append(" and ");
        if (this.filled){
            output.append("filled.");
        }else{
            output.append("not filled.");
        }

        return output.toString();
    }
}

class Rectangle extends Shape{
    double width;
    double length;

    public Rectangle(){
        this(1.0,1.0);
    }

    public Rectangle(double width, double length){
        this.length = length;
        this.width = width;
    }

    public Rectangle(double width, double length, String color, boolean filled){
        this.length = length;
        this.width = width;
        this.color = color;
        this.filled = filled;
    }

    public double getWidth(){
        return this.width;
    }

    public void setWidth(double width){
        this.width = width;
    }

    public double getLength(){
        return this.length;
    }

    public void setLength(double length){
        this.length = length;
    }

    public double getArea(){
        return (this.width*this.length);
    }

    public double getPerimiter(){
        return((2*this.width)+(2*this.length));
    }

    @Override
    public String toString(){
        StringBuffer output = new StringBuffer("A rectangle with a width ");
        output.append(this.width + " and length " + this.length + ", which is a sublass of a shape with color of " + this.color + " and ");
        if (this.filled){
            output.append("filled.");
        }else{
            output.append("not filled.");
        }
        
        return output.toString();
    }
}

class Square extends Rectangle{
    
}