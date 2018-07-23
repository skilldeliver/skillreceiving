import java.util.Scanner;

public class A11_Cinema {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        String type = Console.nextLine();
        int rows = Console.nextInt();
        int cols = Console.nextInt();
        double price = 0.0;

        switch (type){
            case "Premiere":
                price = 12.00;
                break;
            case "Normal":
                price = 7.50;
                break;
            case "Discount":
                price = 5.00;
                break;
        }
        double all = (rows * cols) * price;
        System.out.printf("%.2f", all);
        System.out.println(" leva");
    }
}
