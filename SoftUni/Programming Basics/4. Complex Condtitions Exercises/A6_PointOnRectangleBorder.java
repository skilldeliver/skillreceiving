import java.util.Scanner;

public class A6_PointOnRectangleBorder {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        double x1 = Double.parseDouble(Console.nextLine());
        double y1 = Double.parseDouble(Console.nextLine());
        double x2 = Double.parseDouble(Console.nextLine());
        double y2 = Double.parseDouble(Console.nextLine());
        double x = Double.parseDouble(Console.nextLine());
        double y = Double.parseDouble(Console.nextLine());

        if (x == x2 || x == x1) {
            if (y >= y1 && y <= y2) System.out.println("Border");
            else System.out.println("Inside / Outside");
        }
        else if (y == y2 || y == y1) {
            if (x >= x1 && x <= x2) System.out.println("Border");
            else System.out.println("Inside / Outside");
        }
        else System.out.println("Inside / Outside");
    }
}