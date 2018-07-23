import java.util.Scanner;

public class I_TriangleArea {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);

        double a = Double.parseDouble(Console.nextLine());
        double h = Double.parseDouble(Console.nextLine());

        double area = a * h / 2;

        System.out.print("Triangle area = ");
        System.out.printf("%.2f", area);

    }
}
