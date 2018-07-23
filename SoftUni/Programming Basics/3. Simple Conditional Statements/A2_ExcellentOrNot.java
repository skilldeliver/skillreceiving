
import java.util.Scanner;

public class A2_ExcellentOrNot {
    public static void main(String[] args) {
        Scanner console = new Scanner(System.in);

        double grade = Double.parseDouble(console.nextLine());

        if (grade >= 5.50) {
            System.out.println("Excellent!");
        }
        else {
            System.out.println("Not excellent.");
        }
    }
}
