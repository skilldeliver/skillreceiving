import java.util.Scanner;

public class Problem2 {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);

        double arm = Double.parseDouble(Console.nextLine());
        double front = Double.parseDouble(Console.nextLine());
        String texture = Console.nextLine();
        String idk = Console.nextLine();

        double price = 0.0;
        switch (texture){
            case "Linen":
                price = 15;
                break;
            case "Cotton":
                price = 12;
                break;
            case "Denim":
                price = 20;
                break;
            case "Twill":
                price = 16;
                break;
            case "Flannel":
                price = 11;
                break;
        }
        double total = arm * 2 + front * 2;
        total *= 1.10;
        total /= 100;
        total *= price;
        total += 10;
        if (idk.equals("Yes")){
            total *= 1.20;
        }
        System.out.printf("The price of the shirt is: %.2flv.", total);


    }
}
