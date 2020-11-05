import java.util.Scanner;

public class A6_PrimePairs {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        int first = Integer.parseInt(Console.nextLine());
        int sec = Integer.parseInt(Console.nextLine());
        int firstEnd = Integer.parseInt(Console.nextLine());
        int secEnd = Integer.parseInt(Console.nextLine());

        boolean firstPrime = true;
        boolean secPrime = true;
        for (int i = first; i <= first + firstEnd; i++){
            for (int k = sec; k <= sec + secEnd; k++){
                for (int n = 2; n < i; n++){
                    if (i % n == 0) firstPrime = false;
                }
                for (int u = 2; u < k; u++){
                    if (k % u == 0) secPrime = false;
                }
                if (firstPrime && secPrime){
                    System.out.println(i + "" + k);
                }
                firstPrime = true;
                secPrime = true;
            }
        }


    }
}
