import java.util.Scanner;

public class A2_Airplane {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);

        int h = Integer.parseInt(Console.nextLine());
        int m = Integer.parseInt(Console.nextLine());
        int t = Integer.parseInt(Console.nextLine());

        m += t;

        if (m > 60){
            h += m / 60;
            m = m % 60;
        }
        if(h > 23) h -= 24;

        System.out.println(h + "h " + m + "m");
    }
}
