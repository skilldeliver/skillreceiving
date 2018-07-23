import java.util.Scanner;

public class A12_EqualPairs {
    public static void main(String[] args) {
            Scanner Console = new Scanner(System.in);
            int n = Console.nextInt();
            int sum1 = 0;
            int sum2 = 0;
            int diff = 0;
            int bdiff = 0;

            for (int i = 0; i < n; i++){
                int n1 = Console.nextInt();
                int n2 = Console.nextInt();

                if (i == 0) sum1 = n1 + n2;
                else {
                    sum2 = n1 + n2;
                    diff = Math.abs(sum2 - sum1);
                    if (diff > bdiff) bdiff = diff;
                    sum1 = sum2;

                }

            }
            if (bdiff == 0) System.out.println("Yes, value=" + sum1);
            else System.out.println("No, maxdiff=" + bdiff);

        }
    }
