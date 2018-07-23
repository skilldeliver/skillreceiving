import java.util.Scanner;

public class A6_RhombusOfStars {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        int n = Console.nextInt();

        for (int row = 0; row < n; row++) {

            System.out.println(repeatStr(" ", n - 1 - row) + repeatStr("* ", 1 + row));

        }

        for (int row = n - 1; row >= 0; row--) {
            System.out.println(repeatStr(" ", n - row) + repeatStr("* ", row));

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
