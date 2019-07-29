import java.util.Scanner;

public class A13_PointInTheFigure {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        int h = Console.nextInt();
        int x = Console.nextInt();
        int y = Console.nextInt();

        boolean ab1 = false;
        boolean ab2 = false;
        boolean border = false;
        boolean ab1R = false;
        boolean ab2R = false;

        if ((x > h && x < h * 2) && (y > h && y < h * 4)) ab1 = true;
        if ((x > 0 && x < h * 3) && (y > 0 && y < h)) ab2 = true;
        if (y == h && (x > h && x < 2 * h)) border = true;
        if ((x < h || x > h * 2) || (y < h || y > h * 4)) ab1R = true;
        if ((x < 0 || x > h * 3) || (y < 0 || y > h)) ab2R = true;

        if (ab1 || ab2 || border) System.out.println("inside");
        else if (ab1R && ab2R) System.out.println("outside");
        else System.out.println("border");
    }
}

