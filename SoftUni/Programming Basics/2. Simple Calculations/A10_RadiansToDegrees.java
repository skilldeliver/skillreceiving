import java.util.Scanner;
public class K_RadiansToDegrees {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);

        double rad = Console.nextDouble();
        double deg = rad * 180 / Math.PI;

        System.out.println(Math.round(deg));

    }
}
