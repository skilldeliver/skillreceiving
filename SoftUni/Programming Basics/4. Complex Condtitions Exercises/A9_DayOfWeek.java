import java.util.Scanner;

public class A9_DayOfWeek {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        int num = Console.nextInt();
        String [] days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"};
        switch (num) {
            case 1:
                System.out.println(days[0]);
            case 2:
                System.out.println(days[1]);
            case 3:
                System.out.println(days[2]);
            case 4:
                System.out.println(days[3]);
            case 5:
                System.out.println(days[4]);
            case 6:
                System.out.println(days[5]);
            case 7:
                System.out.println(days[6]);
            default:
                System.out.println("error");
        }
    }
}
