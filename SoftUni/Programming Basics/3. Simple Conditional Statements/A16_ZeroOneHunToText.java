import java.util.Scanner;

public class A16_ZeroOneHunToText {
    public static void main(String[] args) {
            Scanner Console = new Scanner(System.in);
            int n = Console.nextInt();
            String[] list1 = { "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "", "fifteen", "one hundred", "invalid number" };
            String[] list2 = { "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"};
            int n1 = n / 10;
            int n2 = n % 10;
            if (n < 0 || n > 100) System.out.println(list1[17]);
            else if (n == 100) System.out.println(list1[16]);
            else if (n >= 0 && n < 14 || n == 15) System.out.println(list1[n]);
            else if (n > 13 && n < 20) System.out.println(list1[n2] + "teen");
            else if (n > 19 && n < 100 && n2 == 0) System.out.println(list2[n1 - 2]);
            else System.out.println(list2[n1 - 2] + " " + list1[n2]);
        }
    }