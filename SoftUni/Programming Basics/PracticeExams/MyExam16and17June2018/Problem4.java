import java.util.Scanner;

public class Problem4 {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        int cats = Integer.parseInt(Console.nextLine());

        for (int i = 1; i <= cats; i++){
            char smallName = Console.nextLine().charAt(0);
            char family = Console.nextLine().charAt(0);
            int year = Integer.parseInt(Console.nextLine());

            System.out.println(year + "" + (int) smallName + "" + (int) family + "" + i);
        }

    }
}
