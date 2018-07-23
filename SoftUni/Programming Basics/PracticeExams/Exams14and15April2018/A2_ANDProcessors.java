import java.util.Scanner;

public class A2_ANDProcessors {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        int amountCPU = Integer.parseInt(Console.nextLine());
        int emloyees = Integer.parseInt(Console.nextLine());
        int workingDays = Integer.parseInt(Console.nextLine());

        int workingHours = emloyees * workingDays * 8;
        int CPUs = workingHours / 3;

        if (CPUs >= amountCPU){
            double profit = (CPUs - amountCPU) * 110.10;
            System.out.printf("Profit: -> %.2f BGN", profit);
        }
        else if (CPUs < amountCPU){
            double loss = (amountCPU - CPUs) * 110.10;
            System.out.printf("Losses: -> %.2f BGN", loss);
        }

    }
}
