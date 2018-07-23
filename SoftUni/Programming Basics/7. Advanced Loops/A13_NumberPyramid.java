import java.util.Scanner;

public class A13_NumberPyramid {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        int n = Console.nextInt();
        int count = 1;

        for (int i = 1; i <= 999; i++){
            if (count > n) break;
            for (int k = 1; k <= i; k ++){
                if (count > n) break;
                System.out.print(count + " ");
                count += 1;
            }
            System.out.println();
        }
    }
}
