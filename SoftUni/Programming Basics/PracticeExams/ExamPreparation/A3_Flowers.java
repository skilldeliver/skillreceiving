import java.util.Scanner;

public class A3_Flowers {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);

        int hrizantemi = Integer.parseInt(Console.nextLine());
        int rozi = Integer.parseInt(Console.nextLine());
        int laleta = Integer.parseInt(Console.nextLine());
        String season = Console.nextLine();
        String party = Console.nextLine();

        double total = 0;
        if (season.equals("Spring") ||season.equals("Summer")){
            total = hrizantemi * 2.00 + rozi * 4.10 + laleta * 2.50;
        }
        else if (season.equals("Autumn") ||season.equals("Winter")){
            total = hrizantemi * 3.75 + rozi * 4.50 + laleta * 4.15;
        }

        if (party.equals("Y")){
            total *= 1.15;
        }

        if (laleta > 7 && season.equals("Spring")){
            total *= 0.95;
        }
        if (rozi >= 10 && season.equals("Winter")){
            total *= 0.90;
        }
        if (hrizantemi >= 20 || rozi >= 20 || laleta >= 20){
            total *= 0.80;
        }

        System.out.printf("%.2f", total + 2);


    }
}
