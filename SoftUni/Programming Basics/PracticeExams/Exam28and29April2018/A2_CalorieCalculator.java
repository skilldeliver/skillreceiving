import java.util.Scanner;

public class A2_CalorieCalculator {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        String sex = Console.nextLine();
        double weight = Double.parseDouble(Console.nextLine());
        double height = Double.parseDouble(Console.nextLine());
        int age = Integer.parseInt(Console.nextLine());
        String activity = Console.nextLine();

        double coef = 0.0;
        switch (activity){
            case "sedentary":
                coef = 1.2;
                break;
            case "lightly active":
                coef = 1.375;
                break;
            case "moderately active":
                coef = 1.55;
                break;
            case "very active":
                coef = 1.725;
                break;
        }
        double bnm = 0.0;
        if (sex.equals("m")){
            bnm = 66 + (13.7 * weight) + (5 * (height * 100) - (6.8 * (double) age));

        }
        else {
            bnm = 655 + (9.6 * weight) + (1.8 * (height * 100) - (4.7 * (double) age));
            }

        double total = bnm * coef;
        double totalInt = Math.ceil(total);
        int totalInt2 = (int) totalInt;

        System.out.println("To maintain your current weight you will need " + totalInt2 + " calories per day.");






    }
}
