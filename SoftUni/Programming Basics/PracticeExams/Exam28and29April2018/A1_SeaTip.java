import java.util.Scanner;

public class A1_SeaTip {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        double moneyForFood = Double.parseDouble(Console.nextLine());
        double moneyForStuff = Double.parseDouble(Console.nextLine());
        double moneyForHotel = Double.parseDouble(Console.nextLine());

        double benzin = 54.39;
        double ForFoodAndStuff = (3 * moneyForFood) + (3 * moneyForStuff);
        double hotelFirstDay = moneyForHotel * 0.9;
        double hotelSecDay = moneyForHotel * 0.85;
        double hotelThiDay = moneyForHotel * 0.8;

        double Total = benzin + ForFoodAndStuff + hotelFirstDay + hotelSecDay + hotelThiDay;

        System.out.println(String.format("Money needed: %.2f", Total));
    }
}
