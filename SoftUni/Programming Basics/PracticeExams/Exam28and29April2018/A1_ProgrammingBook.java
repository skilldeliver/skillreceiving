import java.text.DecimalFormat;
import java.text.NumberFormat;
import java.util.Scanner;

public class A1_ProgrammingBook {
    public static void main(String[] args) {
        NumberFormat formatter = new DecimalFormat("#0.00");
        Scanner Console = new Scanner(System.in);
        double pricePerPage = Double.parseDouble(Console.nextLine());
        double pricePerBorder = Double.parseDouble(Console.nextLine());
        int percentPaper =  Integer.parseInt(Console.nextLine());
        double sumDesigner = Double.parseDouble(Console.nextLine());
        int percentTeam = Integer.parseInt(Console.nextLine());

        double book = pricePerPage * 899 + pricePerBorder * 2;
        double bookAfterPer = book - (book * ((double)percentPaper / 100));
        double bookAfterDesign = bookAfterPer + sumDesigner;
        double money = bookAfterDesign - (bookAfterDesign * ((double)percentTeam / 100));
        String moneyStr = formatter.format(money);
        System.out.println("Avtonom should pay " + moneyStr + " BGN." );


    }
}
