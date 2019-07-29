import java.util.Scanner;

public class A7_FruitShop {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        String fruit = Console.nextLine().toLowerCase();
        String day = Console.nextLine().toLowerCase();
        double amout = Double.parseDouble(Console.nextLine());
        boolean no = false;
        double price = 0.0;

        if (day.equals("monday") || day.equals("tuesday") || day.equals("wednesday") || day.equals("thursday") || day.equals("friday")){
            if (fruit.equals("banana")) price = 2.50;
            else if (fruit.equals("apple")) price = 1.20;
            else if (fruit.equals("orange")) price = 0.85;
            else if (fruit.equals("grapefruit")) price = 1.45;
            else if (fruit.equals("kiwi")) price = 2.70;
            else if (fruit.equals("pineapple")) price = 5.50;
            else if (fruit.equals("grapes")) price = 3.85;
            else no = true;
        }
        else if (day.equals("saturday") || day.equals("sunday")){
            if (fruit.equals("banana")) price = 2.70;
            else if (fruit.equals("apple")) price = 1.25;
            else if (fruit.equals("orange")) price = 0.90;
            else if (fruit.equals("grapefruit")) price = 1.60;
            else if (fruit.equals("kiwi")) price = 3.00;
            else if (fruit.equals("pineapple")) price = 5.60;
            else if (fruit.equals("grapes")) price = 4.20;
            else no = true;
        }
        else no = true;

        if (no) System.out.println("error");
        else System.out.printf("%.2f",(amout * price));
    }
}