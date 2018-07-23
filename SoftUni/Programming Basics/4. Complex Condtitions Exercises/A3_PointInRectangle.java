import java.util.Scanner;

public class A3_PointInRectangle {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);

        double x1 = Double.parseDouble(Console.nextLine());
        double y1 = Double.parseDouble(Console.nextLine());
        double x2 = Double.parseDouble(Console.nextLine());
        double y2 = Double.parseDouble(Console.nextLine());
        double x = Double.parseDouble(Console.nextLine());
        double y = Double.parseDouble(Console.nextLine());
        boolean inX = false;
        boolean inY = false;

        if (x >= x1 && x <= x2) inX = true;

        if (y >= y1 && y <= y2) inY = true;

        if (inX && inY) System.out.println("Inside");
        else System.out.println("Outside");
    }
}
