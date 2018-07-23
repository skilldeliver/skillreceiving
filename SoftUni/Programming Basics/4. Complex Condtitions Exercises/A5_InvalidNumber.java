import java.util.Scanner;

public class A5_InvalidNumber {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        int num = Console.nextInt();

        if (!(num >= 100 && num <= 200 || num == 0)) {
            System.out.println("invalid");
        }

    }
}