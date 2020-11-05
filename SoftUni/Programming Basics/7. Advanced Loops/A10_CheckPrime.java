import java.util.Scanner;

public class A10_CheckPrime {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        int n  = Console.nextInt();
        boolean Prime = true;
        if (n < 2) Prime = false;

        for (int i = 1; i <= Math.sqrt(n); i++) {
            if (n % i == 0 && i != 1) {
                Prime = false;
            }
        }
        if (Prime) System.out.println("Prime");
        else System.out.println("Not Prime");
    }
}
