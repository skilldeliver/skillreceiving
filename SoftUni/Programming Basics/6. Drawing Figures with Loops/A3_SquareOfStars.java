import java.util.Scanner;

public class A3_SquareOfStars {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);

        int n = Console.nextInt();
        for (int row = 1; row <= n; row++){
            for (int col = 1; col <= n; col++){
                System.out.print("* ");
            }
            System.out.println();
        }
    }
}
