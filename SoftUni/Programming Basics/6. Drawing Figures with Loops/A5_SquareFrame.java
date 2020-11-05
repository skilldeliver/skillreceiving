import java.util.Scanner;

public class A5_SquareFrame {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        int n = Console.nextInt();
        System.out.println("+" + repeatStr(" -", n - 2) + " +");

        for (int row = 1; row <= n - 2; row ++){
            System.out.println("|" + repeatStr(" -", n - 2) + " |");

        }

        System.out.println("+" + repeatStr(" -", n - 2) + " +");

    }

    static String repeatStr(String text, int count) {
        StringBuilder result = new StringBuilder();

        for (int i = 0; i < count; i++) {
            result.append(text);

        }
        return result.toString();
    }
}
