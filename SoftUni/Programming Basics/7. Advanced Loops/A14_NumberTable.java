import java.util.Scanner;

public class A14_NumberTable {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        int n = Console.nextInt();
        int num = 0;
        int slice = 0;

        for (int i = 0; i < n; i ++){
            if (i >= 1) slice += 1;
            for (int k = 0; k < n; k ++){
                num = i + k + 1;
                if (k >= n - slice) System.out.print(2 * n - num + " ");
                else System.out.print(num + " ");
            }
            System.out.println();
        }

    }
}
