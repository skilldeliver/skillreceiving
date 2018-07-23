import java.util.Scanner;

public class A3_AluminiumJoinery {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        int amount = Integer.parseInt(Console.nextLine());
        String type = Console.nextLine();
        String way = Console.nextLine();

        boolean invalidOrder = false;
        if (amount < 10) invalidOrder = true;

        double per = 0;
        int price = 0;
        switch (type) {
            case "90X130":
                if (amount > 30 && amount <= 60){
                    per = 5;
                }
                else if (amount > 60){
                    per = 8;
                }
                price = 110;
                break;
            case "100X150":
                if (amount > 40 && amount <= 80){
                    per = 6;
                }
                else if (amount > 80){
                    per = 10;
                }
                price = 140;
                break;
            case "130X180":
                if (amount > 20 && amount <= 50){
                    per = 7;
                }
                else if (amount > 50){
                    per = 12;
                }
                price = 190;
                break;
            case "200X300":
                if (amount > 25 && amount <= 50){
                    per = 9;
                }
                else if (amount > 50){
                    per = 14;
                }
                price = 250;
                break;
        }

        double total = amount * price;
        if (!(per == 0)) total = total - (total * (per / 100));

        if (way.equals("With delivery")) total += 60;

        if (amount > 99){
            total = total * 0.96;
        }

        if (invalidOrder) System.out.println("Invalid order");
        else System.out.printf("%.2f BGN", total);
    }
}
