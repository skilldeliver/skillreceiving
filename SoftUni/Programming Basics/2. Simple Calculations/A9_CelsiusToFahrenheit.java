import java.util.Scanner;

public class J_CelsiusToFahrenheit {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);

        double celsium = Console.nextDouble();

        double toFaren = (celsium * 9 / 5) + 32;

        System.out.printf("%.2f", toFaren);


    }
}
