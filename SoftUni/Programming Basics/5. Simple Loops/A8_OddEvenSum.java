import java.util.Scanner;

public class A8_OddEvenSum {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        int n = Console.nextInt();
        int oddSum = 0;
        int evenSum = 0;
        for (int i = 1; i <= n; i ++) {
            int numbers = Console.nextInt();
            if (i % 2 == 0) {
                evenSum += numbers;
            }
            else {
                oddSum += numbers;
            }
        }
        if (Math.abs(oddSum - evenSum) == 0) {
            System.out.println("Yes Sum = " + oddSum);
        }
        else {
            System.out.println("No Diff = " + Math.abs(oddSum - evenSum));
        }
    }
}