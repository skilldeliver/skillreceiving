import java.util.Scanner;

public class B_InchesToCentimeters {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        double inches = Double.parseDouble(Console.nextLine());
        double cm = inches * 2.54;
        System.out.println(cm);

    }
}
