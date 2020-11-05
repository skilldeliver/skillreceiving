import java.util.Scanner;

public class A9_House {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        int n = Console.nextInt();
        int stars = 1;
        if (n % 2 == 0) stars = 2;

        int tiles = (n - stars) / 2;

        for(int i = 0; i < (n + 1) / 2; i++) {

            System.out.println(repeatStr("-", tiles) + repeatStr("*", stars) + repeatStr("-", tiles));
            stars += 2;
            tiles -= 1;
        }

        for (int i = 0; i < n - (n + 1) / 2; i ++) {
            System.out.println("|" + repeatStr("*", n - 2) + "|");
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
