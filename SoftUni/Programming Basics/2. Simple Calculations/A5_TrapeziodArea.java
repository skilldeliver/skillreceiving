import java.util.Scanner;

public class E_TrapeziodArea {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        double b1 = Double.parseDouble(Console.nextLine());
        double b2 = Double.parseDouble(Console.nextLine());
        double h = Double.parseDouble(Console.nextLine());

        System.out.println(((b1 + b2) * h) / 2);


    }
}
