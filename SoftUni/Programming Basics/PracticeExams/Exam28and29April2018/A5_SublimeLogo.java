import java.util.Scanner;

public class A5_SublimeLogo {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        int n = Integer.parseInt(Console.nextLine());
        int width = 2 * n;
        int stars = 0;
        int spaces = 0;

        for (int i = 1; i <= n; i ++){
            stars += 2;
            spaces = width - stars;
            System.out.println(repeatStr(" ", spaces) + repeatStr("*", stars));
        }
        spaces = 0;
        for (int i = 1; i <= 4; i++){
            if (i <= 2){
                spaces += 2;
            }
            else {
                spaces -= 2;
            }
            stars = width - spaces;

            System.out.println(repeatStr("*", stars));

        }
        for (int i = 1; i <= 3; i++){
            if (i == 3){
                spaces -= 2;
            }
            else {
                spaces += 2;
            }
            stars = width - spaces;
            System.out.println(repeatStr(" ", spaces) + repeatStr("*", stars));
        }
        stars = -2;
        spaces = 0;

        for (int i = 1; i <= n; i ++){
            stars += 2;
            spaces = width - stars;
            System.out.println( repeatStr("*", spaces));
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
