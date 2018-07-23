import java.util.Scanner;

public class A6_CarNumber {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        int n1 = Integer.parseInt(Console.nextLine());
        int n2 = Integer.parseInt(Console.nextLine());

        for (int i = n1; i <= n2; i++){
            for (int j = n1; j <= n2; j++){
                for (int k = n1; k <= n2; k++){
                    for (int l = n1; l <= n2; l++){
                        if (((i % 2 == 0 && l % 2 != 0) || (l % 2 == 0 && i % 2 != 0)) && i > l){
                            if ((j + k) % 2 == 0) System.out.printf("%s%s%s%s ", i, j, k, l);
                        }
                    }
                }
            }
        }

    }
}
