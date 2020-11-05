import java.util.Scanner;

public class A4_SumNumbers {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        int n = Console.nextInt();
        int sum = 0;
        for (int i = 1; i <= n; i ++){
            int numbers = Console.nextInt();
            sum += numbers;
        }
        System.out.println(sum);

    }
}