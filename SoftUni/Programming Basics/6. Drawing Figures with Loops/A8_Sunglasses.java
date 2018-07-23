import java.util.Scanner;

public class A8_Sunglasses {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        int n = Console.nextInt();

        for (int i = 1; i <= n; i ++){
            if (i == 1 || i == n) {
                System.out.println(repeatStr("*", n * 2) + repeatStr(" ", n) + repeatStr("*", n * 2));
            }
            else if (i == (n - 1) / 2 + 1) System.out.println("*" + repeatStr("/", n * 2 - 2) + "*" + repeatStr("|", n) + "*" + repeatStr("/", n * 2 - 2) + "*");
            else System.out.println("*" + repeatStr("/", n * 2 - 2) + "*" + repeatStr(" ", n) + "*" + repeatStr("/", n * 2 - 2) + "*");
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
