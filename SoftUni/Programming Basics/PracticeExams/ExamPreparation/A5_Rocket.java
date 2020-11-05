import java.util.Scanner;

public class A5_Rocket {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        int n = Integer.parseInt(Console.nextLine());
        int x = 3 * n;
        int dots = ((x / 2) - 2) + 2;

        for (int i = 1; i <= n; i++){
            dots --;
            System.out.println(repeatStr(".", dots) + "/" + repeatStr(" ", x - (dots * 2) - 2) + "\\" + repeatStr(".", dots));
        }
        System.out.println(repeatStr(".", dots) + repeatStr("*", x - (dots * 2))  + repeatStr(".", dots));

        for (int i = 1; i <= n * 2; i++){
            System.out.println(repeatStr(".", dots) + "|" + repeatStr("\\", x - (dots * 2) - 2) + "|"  + repeatStr(".", dots));

        }
        dots ++;
        for (int i = 1; i <= n / 2; i++){
            dots --;
            System.out.println(repeatStr(".", dots) + "/" + repeatStr("*", x - (dots * 2) - 2) + "\\"  + repeatStr(".", dots));

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
