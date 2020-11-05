import java.text.DecimalFormat;
import java.util.Scanner;

public class A13_AreaOfFigures {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);

        String type = Console.nextLine();
        double area = 0.0;

        if (type.equals("square")){
            double a = Double.parseDouble(Console.nextLine());
            area = a * a;
        }
        else if(type.equals("rectangle")){
            double a = Double.parseDouble(Console.nextLine());
            double b = Double.parseDouble(Console.nextLine());
            area = a * b;

        }
        else if(type.equals("circle")){
            double r = Double.parseDouble(Console.nextLine());
            area = Math.pow(r, 2) * Math.PI;
        }
        else if(type.equals("triangle")){
            double a = Double.parseDouble(Console.nextLine());
            double h = Double.parseDouble(Console.nextLine());
            area = a * h / 2;

        }
        DecimalFormat DF = new DecimalFormat("###.###");
        System.out.println(DF.format(area));
    }
}
