import java.util.Scanner;

public class A7_LeftAndRightSum {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        int n = Console.nextInt();
        int leftSum = 0;
        int rightSum = 0;
        int stop = n * 2;
        for (int i = 1; i <= stop; i ++) {
            int numbers = Console.nextInt();
            if (i >= 1 && i <= n){
                leftSum += numbers;
            }
            else if(i > n && i <= stop ) {
                rightSum += numbers;
            }

        }
        if (Math.abs(leftSum - rightSum) == 0){
            System.out.println("Yes, sum = " + rightSum);
        }
        else {
            System.out.println("No, diff = " + Math.abs(leftSum - rightSum));
        }


    }
}