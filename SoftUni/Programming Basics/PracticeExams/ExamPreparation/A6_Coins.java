import java.util.Scanner;

public class A6_Coins {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        double n = Double.parseDouble(Console.nextLine());

        n = n * 100;
        int n3 = (int)n % 10;
        n = n / 10;
        int n2 = (int)n % 10;
        n = n / 10;
        int n1 = (int) n % 10;


        int coins = 0;
        while (true){
            if (n1 - 2 >= 0){
                n1 -= 2;
                coins += 1;
            }
            else if(n1 - 1 >= 0){
                n1 -= 1;
                coins += 1;
            }
            else if(n2 - 5 >= 0){
                n2 -= 5;
                coins += 1;
            }
            else if(n2 - 2 >= 0){
                n2 -= 2;
                coins += 1;
            }
            else if(n2 - 1 >= 0){
                n2 -= 1;
                coins += 1;
            }
            else if(n3 - 5 >= 0){
                n3 -= 5;
                coins += 1;
            }
            else if(n3 - 2 >= 0){
                n3 -= 2;
                coins += 1;
            }
            else if(n3 - 1 >= 0){
                n3 -= 1;
                coins += 1;
            }

            if (n1 == 0 && n2 == 0 && n3 == 0){
                break;
            }
        }
        System.out.println(coins);

    }
}
