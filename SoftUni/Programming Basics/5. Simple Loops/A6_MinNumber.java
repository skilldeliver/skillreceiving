import java.util.Scanner;

public class A6_MinNumber {
    public static void main(String[] args) {
        int min = 0;
        Scanner Console = new Scanner(System.in);
        int n = Console.nextInt();
        for (int i = 1; i <= n; i++) {
            int numbers = Console.nextInt();
            if (i == 1) {
                min = numbers;
            }
            if (numbers < min) {
                min = numbers;
            }
        }
        System.out.println(min);
    }
}