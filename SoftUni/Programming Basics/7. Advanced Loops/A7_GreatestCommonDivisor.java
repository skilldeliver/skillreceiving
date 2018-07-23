import java.util.Scanner;

public class A7_GreatestCommonDivisor {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        int a = Console.nextInt();
        int b = Console.nextInt();

        if (b != 0) {
            while (b != 0) {
                int t = b;
                b = a % b;
                a = t;
            }
        }
        System.out.println(a);

    }
}
