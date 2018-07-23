import java.util.Scanner;

public class A3_Numbers1to2onN {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        int n = Console.nextInt();

        for (int i = 0; i <= n; i ++){
            System.out.printf("%.0f", Math.pow(2, i));
            System.out.println();
        }
    }
}
