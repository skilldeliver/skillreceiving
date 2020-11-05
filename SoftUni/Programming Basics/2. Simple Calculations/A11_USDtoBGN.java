import java.util.Scanner;

public class L_USDtoBGN {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);

        double USD = Console.nextDouble();
        double BGN = USD * 1.79549;

        System.out.printf("%.2f", BGN);
    }
    }