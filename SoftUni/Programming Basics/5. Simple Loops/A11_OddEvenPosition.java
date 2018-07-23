import java.text.DecimalFormat;
import java.util.Scanner;

public class A11_OddEvenPosition {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        DecimalFormat df = new DecimalFormat("#.##");
        int n = Console.nextInt();
        Double oddSum = 0.0;
        Double evenSum = 0.0;

        Double oddMax = -100000000.0;
        Double oddMin = 100000000.0;
        Double evenMax = -100000000.0;
        Double evenMin = 100000000.0;
        for (int i = 1; i <= n; i++) {
            Double numbers = Console.nextDouble();
            if (i % 2 == 0) {
                evenSum += numbers;
                if (numbers > evenMax) {
                    evenMax = numbers;
                }
                if (numbers < evenMin) {
                    evenMin = numbers;
                }
            } else {
                oddSum += numbers;
                if (numbers > oddMax) {
                    oddMax = numbers;
                }
                if (numbers < oddMin) {
                    oddMin = numbers;
                }
            }

        }
        System.out.println("OddSum=" + df.format(oddSum) + ",");
        if (oddMin == 100000000.0) {
            System.out.println("OddMin=No,");
        } else {
            System.out.println("OddMin=" +  df.format(oddMin) + ",");
        }
        if (oddMax == -100000000.0) {
            System.out.println("OddMax=No,");
        } else {
            System.out.println("OddMax=" +  df.format(oddMax) + ",");
        }

        System.out.println("EvenSum=" +  df.format(evenSum) + ",");
        if (evenMin == 100000000.0) {
            System.out.println("EvenMin=No,");
        } else {
            System.out.println("EvenMin=" +  df.format(evenMin) + ",");
        }
        if (evenMax == -100000000.0) {
            System.out.println("EvenMax=No,");
        } else {
            System.out.println("EvenMax=" +  df.format(evenMax));
        }
    }
}