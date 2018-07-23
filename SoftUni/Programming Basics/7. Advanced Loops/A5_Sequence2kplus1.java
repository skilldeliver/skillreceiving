import java.util.Scanner;

public class A5_Sequence2kplus1 {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        int n = Console.nextInt();

        for (int i = 1; i <= n; i = (i * 2) + 1){
            System.out.println(i);
        }

    }
}
