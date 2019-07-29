import java.util.Scanner;

public class A8_TradeComissions {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        String town = Console.nextLine();
        double s = Double.parseDouble(Console.nextLine());
        double percent = 0.0;
        boolean keep = true;

        if (town.equals("Sofia")){
            if (s >= 0 && s <= 500) percent = 5;
            else if (s > 500 && s <= 1000) percent = 7;
            else if (s > 1000 && s <= 10000) percent = 8;
            else if (s > 10000) percent = 12;
        }
        else if (town.equals("Plovdiv")) {
            if (s >= 0 && s <= 500) percent = 5.5;
            else if (s > 500 && s <= 1000) percent = 8;
            else if (s > 1000 && s <= 10000) percent = 12;
            else if (s > 10000) percent = 14.5;
        }
        else if (town.equals("Varna")) {
            if (s >= 0 && s <= 500) percent = 4.5;
            else if (s > 500 && s <= 1000) percent = 7.5;
            else if (s > 1000 && s <= 10000) percent = 10;
            else if (s > 10000) percent = 13;
        }

        if (percent == 0) {
            System.out.println("error");
            keep = false;
        }


        if (keep) System.out.printf("%.2f", (s * (percent / 100)));

    }
}
