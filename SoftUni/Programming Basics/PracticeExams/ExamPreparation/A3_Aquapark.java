import java.util.Scanner;

public class A3_Aquapark {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);

        String month = Console.nextLine().toLowerCase();
        int hour = Integer.parseInt(Console.nextLine());
        int peoples = Integer.parseInt(Console.nextLine());
        String day = Console.nextLine().toLowerCase();

        double pricePerHuman = 0;
        if (month.equals("march") || month.equals("april") || month.equals("may")){
            if (day.equals("day")){
                pricePerHuman = 10.50;
            }
            else {
                pricePerHuman = 8.40;
            }
        }
        else if(month.equals("june") || month.equals("july") || month.equals("august")){
            if (day.equals("day")){
                pricePerHuman = 12.60;
            }
            else {
                pricePerHuman = 10.20;
            }
        }

        if (peoples >= 4){
            pricePerHuman *= 0.90;
        }
        if (hour >= 5){
            pricePerHuman *= 0.50;
        }

        System.out.printf("Price per person for one hour: %.2f", pricePerHuman);
        System.out.println();
        System.out.printf("Total cost of the visit: %.2f", (pricePerHuman * hour) * peoples);

    }
}
