import java.util.Scanner;

public class F_CircleAreaAndPerimeter {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        double r = Double.parseDouble(Console.nextLine());
        double area = Math.PI * r * r;
        double perimeter =  2 * Math.PI * r;

        System.out.print("Area = ");
        System.out.println(area);
        System.out.print("Perimeter = ");
        System.out.println(perimeter);
    }

}
