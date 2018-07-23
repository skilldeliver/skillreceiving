import java.util.Scanner;

public class A1_MiningRig {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);

        int priceGPU = Integer.parseInt(Console.nextLine());
        int priceAdapter = Integer.parseInt(Console.nextLine());
        double consumGPU = Double.parseDouble(Console.nextLine());
        double profitGPU = Double.parseDouble(Console.nextLine());

        double sum = 13 * priceAdapter + 13 * priceGPU + 1000;
        double profit = (profitGPU - consumGPU) * 13;
        double days = Math.ceil(sum / profit);
        System.out.printf("%.0f", sum);
        System.out.println();
        System.out.printf("%.0f", days);
    }
}

