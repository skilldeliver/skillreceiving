import java.util.Scanner;

public class Problem1 {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);

        int perM = Integer.parseInt(Console.nextLine());
        int perP = Integer.parseInt(Console.nextLine());
        int perV = Integer.parseInt(Console.nextLine());
        int totalCal = Integer.parseInt(Console.nextLine());
        int water = Integer.parseInt(Console.nextLine());


        double temp1 = ((perM / 100.0) *  totalCal) / 9;
        double temp2 = (( perP / 100.0) *  totalCal) / 4;
        double temp3 = (( perV / 100.0) *  totalCal) / 4;

        double weight = temp1 + temp2 + temp3;
        double calGram = totalCal / weight;

        calGram = calGram * ( 1 - (water / 100.00));
        System.out.printf("%.4f", calGram);

    }
}
