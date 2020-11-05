import java.util.Scanner;

public class A4_TriangleOfDollars {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);

        int n = Console.nextInt();
        int i = 0;

        for (int row = 1; row <= n; row++ ){
            i++;
            for (int col = 1; col <= i; col++){
                System.out.print("$ ");
            }
            System.out.println();
        }
    }
}
