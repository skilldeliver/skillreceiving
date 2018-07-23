import java.util.Scanner;

public class A12_Volleyball {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        String year = Console.nextLine();
        int p = Integer.parseInt(Console.nextLine());
        int h = Integer.parseInt(Console.nextLine());

        double weekendsSofia = (48 - h) * (3.0 / 4);
        double inHomeTown = h;
        double inHoliday = p * (2.0 / 3);

        double sum = weekendsSofia + inHomeTown + inHoliday;
        if (year.equals("leap")){
            sum *= 1.15;
        }
        System.out.println(Math.floor(sum));

    }
}