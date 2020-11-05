import java.util.Scanner;

public class D_ConcatenateData {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        String firstName = Console.nextLine();
        String lastName = Console.nextLine();
        int years = Integer.parseInt(Console.nextLine());
        String town = Console.nextLine();

        System.out.printf("You are %s %s, a %s-years old person from %s.", firstName, lastName, years, town);

    }
}
