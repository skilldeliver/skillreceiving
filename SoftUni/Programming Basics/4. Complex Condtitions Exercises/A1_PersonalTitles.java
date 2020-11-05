import java.util.Scanner;

public class A1_PersonalTitles {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        double age = Double.parseDouble(Console.nextLine());
        String gender = Console.nextLine();

        if (gender.equals("m")) {
            if (age >= 16) System.out.println("Mr.");
            else System.out.println("Master");
        }
        else if(gender.equals("f")) {
            if (age >= 16) System.out.println("Ms.");
            else System.out.println("Miss");
        }

    }
}
