import java.util.Scanner;

public class A6_PasswordGenerator {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        int a = Integer.parseInt(Console.nextLine());
        char b = Console.nextLine().toUpperCase().charAt(0);
        char c = Console.nextLine().toLowerCase().charAt(0);
        int d = Integer.parseInt(Console.nextLine());
        int e = Integer.parseInt(Console.nextLine());
        int f = Integer.parseInt(Console.nextLine());
        int num = Integer.parseInt(Console.nextLine());

        int count = 0;
        for (int i = 1; i <= a; i ++){
            for (char j = 'A'; j <= b; j++){
                for (char k = 'a'; k <= c; k++){
                    for (int l = 1; l <= d; l++){
                        for (int m = 1; m <= e; m++){
                            for (int n = 1; n <= f; n++){
                                count += 1;
                                if (count == num){
                                    System.out.printf("%s%s%s%s%s%s", i, j, k, l, m, n);
                                    return;
                                }
                            }
                        }
                    }
                }

            }
        }
        System.out.println("No password on this position");



    }
}
