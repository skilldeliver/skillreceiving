import java.util.Scanner;

public class A6_SpecialCombinations {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        int n1 = Integer.parseInt(Console.nextLine());
        int n2 = Integer.parseInt(Console.nextLine());
        int n3 = Integer.parseInt(Console.nextLine());

        boolean fir = false;
        boolean sec = false;
        boolean thi = false;

        for (int i = 1; i <= n1; i++){
            for (int j = 1; j <= n2; j++){
                for (int k = 1; k <= n3; k++){
                    if (i % 2 == 0) fir = true;
                    if (k % 2 == 0) thi = true;
                    if (j == 2 || j == 3 || j == 5 || j == 7) sec = true;

                    if (fir && sec && thi) System.out.println(i + " " + j + " " + k);

                    fir = false;
                    sec = false;
                    thi = false;
                }
            }
        }

    }
}
