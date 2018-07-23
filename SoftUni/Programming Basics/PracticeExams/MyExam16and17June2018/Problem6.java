import java.util.Scanner;

public class Problem6 {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        int days = Integer.parseInt(Console.nextLine());
        int hours = Integer.parseInt(Console.nextLine());


        double tax = 0.0;
        double total = 0.0;
        for (int i = 1; i <= days; i++){
            for (int j = 1; j <= hours; j++){
                if (i % 2 == 0 && j % 2 != 0 ){
                    tax += 2.50;
                }
                else if(i % 2 != 0 && j % 2 == 0){
                    tax += 1.25;
                }
                else {
                    tax += 1;
                }
            }
            System.out.printf("Day: %s - %.2f leva", i, tax);
            System.out.println();
            total += tax;
            tax = 0;
        }
        System.out.printf("Total: %.2f leva", total);

    }
}
