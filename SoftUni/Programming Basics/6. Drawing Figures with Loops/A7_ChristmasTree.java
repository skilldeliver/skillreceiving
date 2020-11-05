import java.util.Scanner;

public class A7_ChristmasTree {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);

        int n = Console.nextInt();

        for(int i = 1; i <= n + 1; i ++) {
            if (i == 1) System.out.println(repeatStr(" ", n + 1) + "|");
            else System.out.println(repeatStr(" ", n + 1 - i) + repeatStr("*", i - 1) + " | " + repeatStr("*", i - 1));
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
