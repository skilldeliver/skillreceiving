import java.util.Scanner;

public class A6_BitcoinCodeGenerator {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        int a = Integer.parseInt(Console.nextLine());
        int b = Integer.parseInt(Console.nextLine());
        int maxCodes = Integer.parseInt(Console.nextLine());

        char i = 32;
        char j = 57;

        int count = 0;
        for (int k = 1; k <= a; k++){
            for (int l = 1; l <= b; l++){
                i ++;
                j ++;
                if (i > 47) i = 33;
                if (j > 64) j = 58;
                count ++;
                System.out.printf("%s%s%s%s%s%s|", i, j, k, l, j, i);
                if (count == maxCodes) return;

                    }
                }

            }
        }

