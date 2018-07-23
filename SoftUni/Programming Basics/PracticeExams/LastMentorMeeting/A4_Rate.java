import java.util.Scanner;

public class A4_Rate {
    public static void main(String[] args) {

        Scanner Console = new Scanner(System.in);
        double S = Double.parseDouble(Console.nextLine());
        int moths = Integer.parseInt(Console.nextLine());

        double simple = S;
        double complex = S;

        double per = S * (3.00 / 100.00);
        for (int i = 1; i <= moths; i++){
            simple += per;
            complex = complex + complex * 2.7 / 100;
        }
        System.out.printf("Simple interest rate: %.2f lv.", simple);
        System.out.println();
        System.out.printf("Complex interest rate: %.2f lv.", complex);
        System.out.println();

        if (simple >= complex){
            System.out.printf("Choose a simple interest rate. You will win %.2f lv.", simple - complex);
        }
        else{
            System.out.printf("Choose a complex interest rate. You will win %.2f lv.", complex - simple);
        }
    }
}
