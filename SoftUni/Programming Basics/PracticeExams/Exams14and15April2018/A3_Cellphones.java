import java.util.Scanner;

public class A3_Cellphones {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        int budget = Integer.parseInt(Console.nextLine());
        int phones = Integer.parseInt(Console.nextLine());
        String brand = Console.nextLine();

        double price = 0;
        int per = 0;

        switch (brand){
            case "Gsm4e":
                price = 20.50;
                per = 1;
                break;
            case "Mobifon4e":
                price = 50.75;
                per = 2;
                break;
            case "Telefon4e":
                price = 115;
                per = 3;
                break;

        }
        if (phones > 10 && phones <= 20){
            per += 2;
        }
        else if(phones > 20 && phones <= 50){
            per += 5;
        }
        else if (phones > 50){
            per += 7;
        }
        double total = price * phones;
        total = total - (total * ((double)per / 100));


        if (total <= budget){
            System.out.printf("The company bought all mobile phones. %.2f leva left.", (budget - total));
        }
        else {
            System.out.printf("Not enough money for all mobiles. Company needs %.2f more leva.", (total - budget));
        }
    }
}
