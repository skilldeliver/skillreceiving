import java.util.Scanner;

public class A1_PaintingHouse {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        double x = Double.parseDouble(Console.nextLine());
        double y = Double.parseDouble(Console.nextLine());
        double h = Double.parseDouble(Console.nextLine());

        double walls = 2 * (x * y) - 2 * 2.25;
        double allWalls = 2 * (x * x) - 2.4 + walls;
        double greenPaint = allWalls / 3.4;
        double roof = 2 * (x * y) + 2 * (x * h / 2);
        double redPaint = roof / 4.3;


        System.out.printf("%.2f", greenPaint);
        System.out.println();
        System.out.printf("%.2f", redPaint);

    }
}
