import java.util.Scanner;

public class Problem5 {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        int n = Integer.parseInt(Console.nextLine());
        int x = 4 * n;
        int dots = n - 1;

        System.out.println(repeatStr(".", dots) + "|\\" + repeatStr("/\\", dots) + "/|" + repeatStr(".", dots));
        System.out.println(repeatStr(".", dots) + "|" + repeatStr("~", x - (dots * 2) - 2) + "|" + repeatStr(".", dots));

        int el = n + 1;
        int spaces = -1;
        for (int i = 1; i <= n; i++){
            el --;
            spaces ++;
            System.out.println(repeatStr(".", dots) + "|" + repeatStr(" ", spaces) + repeatStr("{}", el) + repeatStr(" ", spaces) + "|" + repeatStr(".", dots));
        }
        System.out.println(repeatStr(".", dots) + "|" + repeatStr(" ", n - 2) + "MEOW" + repeatStr(" ", n - 2) + "|" + repeatStr(".", dots));
        System.out.println(repeatStr(".", dots) + "|" + repeatStr(" ", n - 2) + "FOOD" + repeatStr(" ", n - 2) + "|" + repeatStr(".", dots));

        el = 0;
        spaces = n;
        for (int i = 1; i <= n; i++){
            el ++;
            spaces --;
            System.out.println(repeatStr(".", dots) + "|" + repeatStr(" ", spaces) + repeatStr("{}", el) + repeatStr(" ", spaces) + "|" + repeatStr(".", dots));

        }
        System.out.println(repeatStr(".", dots) + "|" + repeatStr("~", x - (dots * 2) - 2) + "|" + repeatStr(".", dots));
        System.out.println(repeatStr(".", dots) + "|\\" + repeatStr("/\\", dots) + "/|" + repeatStr(".", dots));

    }

    static String repeatStr (String text,int count){
        StringBuilder result = new StringBuilder();

        for (int i = 0; i < count; i++) {
            result.append(text);

        }
        return result.toString();
    }
}

