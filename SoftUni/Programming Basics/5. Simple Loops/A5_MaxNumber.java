import java.util.Scanner;

public class A5_MaxNumber {
    public static void main(String[] args) {
        int max = 0;
        Scanner Console = new Scanner(System.in);
        int n = Console.nextInt();
        for (int i = 1; i <= n; i++) {
            int numbers = Console.nextInt();
            if (i == 1) {
                max = numbers;
            }
            if (numbers > max) {
                max = numbers;
            }
        }
        System.out.println(max);
    }
}