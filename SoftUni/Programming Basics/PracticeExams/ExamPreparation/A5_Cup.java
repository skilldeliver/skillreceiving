import java.util.Scanner;

public class A5_Cup {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        int n = Integer.parseInt(Console.nextLine());
        int x = 5 * n;

        int leftDots = n - 1;
        int rightDots = leftDots;

        for (int i = 1; i <= n / 2; i++) {
            leftDots++;
            rightDots++;
            System.out.println(repeatStr(".", leftDots) + repeatStr("#", x - rightDots - leftDots) + repeatStr(".", rightDots));
        }
        for (int i = 1; i <= n / 2 + 1; i++) {
            leftDots++;
            rightDots++;
            System.out.println(repeatStr(".", leftDots) + "#" + repeatStr(".", x - leftDots - rightDots - 2) + "#" + repeatStr(".", rightDots));
        }
        System.out.println(repeatStr(".", leftDots) + repeatStr("#", x - rightDots - leftDots) + repeatStr(".", rightDots));

        for (int i = 1; i <= n / 2; i++) {
            System.out.println(repeatStr(".", (x - (n + 4)) / 2) + repeatStr("#", n + 4) + repeatStr(".", (x - (n + 4)) / 2));
        }
        System.out.println(repeatStr(".", (x - 10) / 2) + "D^A^N^C^E^" + repeatStr(".", ((x - 10) / 2)));


        for (int i = 1; i <= n / 2 + 1; i++){
            System.out.println(repeatStr(".", (x - (n + 4)) / 2) + repeatStr("#", n + 4) + repeatStr(".", (x - (n + 4)) / 2));
        }

    }
    static String repeatStr (String text,int count){
        StringBuilder result = new StringBuilder();

        for (int i = 0; i < count; i++) {
            result.append(text);

        }
        return result.toString();
    }
}
