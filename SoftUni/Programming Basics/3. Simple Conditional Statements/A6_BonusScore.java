import java.util.Scanner;

public class A6_BonusScore {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        int points = Integer.parseInt(Console.nextLine());
        double bonus = 0.0;

        if (points <= 100){
            bonus = 5;
        }
        else if (points > 100 && points <= 1000){
            bonus = points * 0.2;
        }
        else if (points > 1000){
            bonus = points * 0.1;
        }

        if (points % 2 == 0){
            bonus += 1;
        }
        else if (points % 5 == 0){
            bonus += 2;
        }
        System.out.println(bonus);
        System.out.println(points + bonus);

    }
}
