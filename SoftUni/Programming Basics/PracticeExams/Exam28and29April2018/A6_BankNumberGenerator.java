import java.util.Scanner;

public class A6_BankNumberGenerator {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        int a = Integer.parseInt(Console.nextLine());
        char b = Console.nextLine().charAt(0);
        char c = Console.nextLine().charAt(0);
        char d = Console.nextLine().charAt(0);
        int e = Integer.parseInt(Console.nextLine());
        int n = Integer.parseInt(Console.nextLine());

        int count = 0;

        for (int i = a; i <= 99; i++){
            for (char j = b; j <= 'Z'; j++){
                for (char k = c; k <= 'z'; k++){
                    for (char l = d; l <= 'Z'; l++){
                        for (int m = e; m >= 10; m--){
                            if (i % 10 == 2 && m % 10 == 5){
                                count += 1;
                                if (count == n){
                                    System.out.printf("%s%s%s%s%s", i, j, k, l, m);
                                    break;
                                }
                            }
                        }
                    }
                }
            }
        }


    }
}
