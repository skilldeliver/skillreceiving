import java.util.Scanner;

public class A6_NumberInRange1to100 {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        System.out.println("Еnter a number in the range [1...100]:");
        int n = Console.nextInt();
        while (n < 1 || n > 100) {
            System.out.println("Invalid number!");
            System.out.println("Еnter a number in the range [1...100]:");
            n = Console.nextInt();
        }
        System.out.println("The number is: " + n);
    }
}
