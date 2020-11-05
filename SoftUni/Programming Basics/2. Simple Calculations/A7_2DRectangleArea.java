import java.util.Scanner;

public class G_2DRectangleArea {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        double x1 = Double.parseDouble(Console.nextLine());
        double y1 = Double.parseDouble(Console.nextLine());
        double x2 = Double.parseDouble(Console.nextLine());
        double y2 = Double.parseDouble(Console.nextLine());

        double a = Math.abs(x2 - x1);
        double b = Math.abs(y2 - y1);

        double area = a * b;
        double per = (a * 2) + (b * 2);

        System.out.println(area);
        System.out.println(per);
    }
}
