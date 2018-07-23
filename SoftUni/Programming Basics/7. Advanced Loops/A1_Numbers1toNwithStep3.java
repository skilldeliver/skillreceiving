import java.util.Scanner;

public class A1_Numbers1toNwithStep3{
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        int n = Integer.parseInt(Console.nextLine());

        for (int i = 1; i <= n; i += 3) {
            System.out.println(i);
        }
    }

}
