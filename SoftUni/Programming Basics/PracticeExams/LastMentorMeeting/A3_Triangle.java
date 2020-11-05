import java.text.DecimalFormat;
import java.util.Scanner;


public class A3_Triangle {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);

        double a = Double.parseDouble(Console.nextLine());
        double b = Double.parseDouble(Console.nextLine());
        double c = Double.parseDouble(Console.nextLine());

        DecimalFormat df = new DecimalFormat("0.#");

        if (a < b + c && b < a + c && c < a + b){
            if (a != b && c != b && a != c){
                System.out.println("Triangle with sides " + df.format(a) + ", " + df.format(b) + " and " + df.format(c) + " is scalene.");
            }
            else if(a == b && b == c && a == c){
                System.out.println("Triangle with sides " + df.format(a) + ", " + df.format(b) + " and " + df.format(c) + " is equilateral.");

            }
            else if(a == b || b == c || a == c){
                System.out.println("Triangle with sides " + df.format(a) + ", " + df.format(b) + " and " + df.format(c) + " is isosceles.");

            }
        }
        else {
            System.out.println("There is no triangle with sides " + df.format(a) + ", " + df.format(b) + " and " + df.format(c) + ".");
        }

    }
}