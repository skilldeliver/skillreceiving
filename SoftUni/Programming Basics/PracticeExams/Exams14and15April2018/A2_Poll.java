import java.util.Scanner;

public class A2_Poll{
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        double participants = Integer.parseInt(Console.nextLine());
        int forFirstPlace = Integer.parseInt(Console.nextLine());

        double forSecPlace = forFirstPlace * 0.8;
        double forThirdPlace = forSecPlace * 0.9;

        double total = forFirstPlace + forSecPlace + forThirdPlace;
        double half = participants / 2;

        if (total >= half){
            System.out.printf("First three languages have %.0f votes more", (total - half));
        }
        else {
            System.out.printf("First three languages have %.0f votes less of half votes", (half - total));
        }




    }
}
