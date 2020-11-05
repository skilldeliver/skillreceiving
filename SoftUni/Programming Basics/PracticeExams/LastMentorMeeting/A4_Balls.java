import java.util.Scanner;

public class A4_Balls {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        int n = Integer.parseInt(Console.nextLine());

        String ball = " ";
        int total = 0;
        int red = 0;
        int ora = 0;
        int yel = 0;
        int whi = 0;
        int oth = 0;
        int bla = 0;

        int points = 0;
        for (int i = 1; i <= n; i++){
            ball = Console.nextLine();

            if (ball.equals("red")){
                red ++;
                points += 5;
            }
            else if (ball.equals("orange")){
                ora ++;
                points += 10;
            }
            else if (ball.equals("yellow")){
                yel ++;
                points += 15;
            }
            else if (ball.equals("white")){
                whi ++;
                points += 20;
            }
            else if(ball.equals("black")){
                bla ++;
                points /= 2;
            }
            else {
                oth ++;
            }
        }
        System.out.println("Total points: " + points);
        System.out.println("Points from red balls: " + red);
        System.out.println("Points from orange balls: " + ora);
        System.out.println("Points from yellow balls: " + yel);
        System.out.println("Points from white balls: " + whi);
        System.out.println("Other colors picked: " + oth);
        System.out.println("Divides from black balls: " + bla);
    }
}
