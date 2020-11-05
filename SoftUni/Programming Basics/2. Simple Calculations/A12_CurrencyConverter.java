
import java.util.Scanner;

public class M_CurrencyConverter {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);

        double money = Double.parseDouble(Console.nextLine());
        String from = Console.nextLine();
        String to = Console.nextLine();
        double course = 0.0;

        switch (from) {
            case "USD":
                if (to.equals("BGN")){
                    course = money * 1.79549;
                    break;
                }
                else if (to. equals("EUR")){
                    course = (money * 1.79549) / 1.95583;
                    break;
                }
                else if (to.equals("GBP")){
                    course = (money * 1.79549) / 2.53405;
                    break;
                }
                break;
            case "BGN":
                if (to.equals("USD")){
                    course = money / 1.79549;
                    break;
                }
                else if (to. equals("EUR")){
                    course = money / 1.95583;
                    break;
                }
                else if (to.equals("GBP")){
                    course = money / 2.53405;
                    break;
                }
                break;
            case "EUR":
                if (to.equals("BGN")){
                    course = money * 1.95583;
                    break;
                }
                else if (to. equals("USD")){
                    course = (money * 1.95583) / 1.79549;
                    break;
                }
                else if (to.equals("GBP")){
                    course = (money * 1.95583) / 2.53405;
                    break;
                }
                break;
            case "GBP":
                if (to.equals("BGN")){
                    course = money * 2.53405;
                    break;
                }
                else if (to. equals("EUR")){
                    course = (money * 2.53405) / 1.95583;
                    break;
                }
                else if (to.equals("USD")){
                    course = (money * 2.53405) / 1.79549;
                    break;
                }
                break;
        }

        System.out.printf("%.2f", course);
        System.out.print(" " + to);

    }
}
