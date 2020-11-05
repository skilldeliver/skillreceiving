import java.util.Scanner;

public class A4_CreditSystem {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);

        int n = Integer.parseInt(Console.nextLine());
        double num = 0.0;
        double mark = 0.0;
        double credits = 0.0;
        double sumCredits = 0.0;
        double sumMarks = 0.0;
        for (int i = 1; i <= n; i++){
            num = Double.parseDouble(Console.nextLine());
            mark = num % 10;
            credits = (int)num / 10;

            if (mark == 2){
                credits = 0;
            }
            else if (mark == 3){
                credits = credits * 0.5;
            }
            else if (mark == 4){
                credits = credits * 0.7;
            }
            else if (mark == 5){
                credits = credits * 0.85;
            }
            else if (mark == 6){
                credits = credits;
            }
            sumMarks += mark;
            sumCredits += credits;

        }
        System.out.printf("%.2f", sumCredits);
        System.out.println();
        System.out.printf("%.2f", (sumMarks / (double) n));

    }
}
