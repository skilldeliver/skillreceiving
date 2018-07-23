import java.util.Scanner;

public class A4_EvenPowersOf2 {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        int n = Console.nextInt();

        for (int i = 0; i <= n; i++){
            if (i % 2 == 0){
                System.out.printf("%.0f", Math.pow(2, i));
                System.out.println();
            }
        }
    }
}
