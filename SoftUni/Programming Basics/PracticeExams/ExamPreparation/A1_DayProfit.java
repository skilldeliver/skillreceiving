import java.util.Scanner;

public class A1_DayProfit {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);

        int daysMonth = Integer.parseInt(Console.nextLine());
        double madeMoneyDay = Double.parseDouble(Console.nextLine());
        double dolarLev = Double.parseDouble(Console.nextLine());

        double monthSalary = (double)daysMonth * madeMoneyDay;
        double yearProfit = 12 * monthSalary + monthSalary * 2.5;
        double yearTaks = yearProfit * 0.75;
        yearTaks = yearTaks * dolarLev;

        double perDay = yearTaks / 365;
        System.out.printf("%.2f", perDay);
    }
}
