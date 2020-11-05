import java.util.Scanner;

public class A9_SumDigits {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        int n = Console.nextInt();
        int digit = 0;
        int sum = 0;

        while (n > 0) {
            digit = n % 10;
            sum += digit;
            n /= 10;
        }
        System.out.println(sum);

    }
}
