import java.util.Scanner;

public class A2_Spaceship {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);

        double widthSpaceship = Double.parseDouble(Console.nextLine());
        double heightSpaceship = Double.parseDouble(Console.nextLine());
        double lenght = Double.parseDouble(Console.nextLine());
        double lenghtAstro = Double.parseDouble(Console.nextLine());

        double vRocket = widthSpaceship * heightSpaceship * lenght;
        double vRoom = (lenghtAstro + 0.40) * 2 * 2;

        int astros = (int) Math.floor(vRocket / vRoom);

        if (astros >= 3 && astros <= 10){
            System.out.printf("The spacecraft holds %s astronauts.", astros);
        }
        else if (astros < 3) System.out.println("The spacecraft is too small.");
        else System.out.println("The spacecraft is too big.");


    }
}
