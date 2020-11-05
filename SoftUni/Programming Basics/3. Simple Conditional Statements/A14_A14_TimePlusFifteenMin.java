import java.util.Scanner;

public class A14_A14_TimePlusFifteenMin {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);

        int hours = Integer.parseInt(Console.nextLine());
        int minutes = Integer.parseInt(Console.nextLine());

        minutes += 15;

        if (minutes > 59){
            minutes -= 60;
            hours ++;

        }
        if (hours > 23){
            hours = 0;
        }
        if (minutes < 10){
            System.out.printf("%d:0%d", hours, minutes);
        }
        else{
        System.out.printf("%d:%d", hours, minutes);
        }
    }
}
