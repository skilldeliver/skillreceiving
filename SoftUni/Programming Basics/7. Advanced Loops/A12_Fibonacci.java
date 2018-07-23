import java.util.Scanner;

public class A12_Fibonacci {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        int n = Console.nextInt();
        int f0 = 1;
        int f1 = 1;
        int sum = 0;
        if (n < 2) System.out.println(1);
        else {
            for (int i = 2; i <= n; i++){
                sum = f0 + f1;
                f0 = f1;
                f1 = sum;
            }
            System.out.println(sum);
        }

    }
}
