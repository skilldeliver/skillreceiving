import java.util.Scanner;

public class A10_HalfSumElement {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        int n = Console.nextInt();
        int maxNum = 0;
        int sum = 0;
        for (int i = 1; i <= n; i ++){
            int numbers = Console.nextInt();
            sum += numbers;
            if (numbers > maxNum) {
                maxNum = numbers;
            }

        }
        sum -= maxNum;
        if (maxNum == sum){
            System.out.println("Yes Sum = " + sum);
        }
        else {
            System.out.println("No Diff = " + Math.abs(maxNum - sum));
        }
    }
}