import java.util.Scanner;

public class A4_ASCIICombinations {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);

        int n = Integer.parseInt(Console.nextLine());


        char symbol = ' ';
        int nums = 0;
        int bl = 0;
        int sl = 0;
        int other = 0;
        int max = 0;

        String c1 = "";
        String c2 = "";
        String c3 = "";
        String c4 = "";
        String last = "";

        for (int i = 1; i <= n; i++) {
            symbol = Console.nextLine().charAt(0);

            if (symbol >= 48 && symbol <= 57) {
                nums += symbol;
                c1 += symbol;
                if (nums > max) {
                    max = nums;
                    last = c1;
                }
            }
            else if (symbol >= 65 && symbol <= 90) {
                bl += symbol;
                c2 += symbol;
                if (bl > max) {
                    max = bl;
                    last = c2;
                }
                }
                else if (symbol >= 97 && symbol <= 122) {
                    sl += symbol;
                    c3 += symbol;
                    if (sl > max) {
                        max = sl;
                        last = c3;
                    }
                } else {
                    other += symbol;
                    c4 += symbol;
                    if (other > max) {
                        max = other;
                        last = c4;
                    }
                }


            }
        System.out.printf("Biggest ASCII sum is:%d%n", max);
        System.out.printf("Combination of characters is:%s", last);
        }
    }

