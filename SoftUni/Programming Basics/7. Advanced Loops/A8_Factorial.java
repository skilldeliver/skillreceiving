import java.util.Scanner;

public class A8_Factorial {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        int n = Console.nextInt();
        int fact = 1;
        for (int i = 1; i <= n; i++){
            fact *= i;
        }
        System.out.println(fact);

    }
}
