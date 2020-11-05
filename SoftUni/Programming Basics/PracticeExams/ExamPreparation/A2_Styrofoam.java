import java.util.Scanner;

public class A2_Styrofoam {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);

        double budget = Double.parseDouble(Console.nextLine());
        double areaHouse = Double.parseDouble(Console.nextLine());
        int windows = Integer.parseInt(Console.nextLine());
        double styrofoam = Double.parseDouble(Console.nextLine());
        double pack = Double.parseDouble(Console.nextLine());

        areaHouse = areaHouse - (double) windows * 2.4;
        areaHouse = areaHouse * 1.1;
        int neededPacks = (int) Math.ceil(areaHouse / styrofoam);
        double spend = (double) neededPacks * pack;

        if (spend <= budget){
            System.out.printf("Spent: %.2f", spend);
            System.out.println();
            System.out.printf("Left: %.2f", (budget - spend));
        }
        else {
            System.out.printf("Need more: %.2f", (spend - budget));
        }



    }
}

