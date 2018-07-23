import javax.print.CancelablePrintJob;
import java.util.Scanner;

public class A1_Moon {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);

        double speed = Double.parseDouble(Console.nextLine());
        double fuel = Double.parseDouble(Console.nextLine());

        double distance = 384400 * 2;
        int time = (int) Math.ceil(distance / speed) + 3;
        double totalFuel = ((fuel * distance) / 100);
        System.out.println(time);
        System.out.printf("%.0f", totalFuel);


    }
}
