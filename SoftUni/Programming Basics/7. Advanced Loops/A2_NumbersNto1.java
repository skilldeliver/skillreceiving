import java.util.Scanner;

public class A2_NumbersNto1 {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        int n = Console.nextInt();

        for (int i = n; i > 0; i--){
            System.out.println(i);
        }
    }
}
