
import java.util.Scanner;

public class A3_EvenOrOdd {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        int num = Integer.parseInt(Console.nextLine());

        if (num % 2 == 0){
            System.out.println("even");
        }
        else {
            System.out.println("odd");
        }
    }
}
