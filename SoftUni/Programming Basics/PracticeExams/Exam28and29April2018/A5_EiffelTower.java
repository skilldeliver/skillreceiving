import java.util.Scanner;

public class A5_EiffelTower {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        int n = Integer.parseInt(Console.nextLine());
        int width = 2 * n + 6;
        int dashes = (width - 2) / 2;

        for (int i = 1; i <= n; i++){
            System.out.println(repeatStr("-", dashes) + "**" + repeatStr("-", dashes));
        }
        dashes --;
        for (int i = 1; i <= n - 2; i ++){
            if (i == n - 2){
                dashes --;
                System.out.println(repeatStr("-", dashes) + "******" + repeatStr("-", dashes));
            }
            else {
                System.out.println(repeatStr("-", dashes) + "****" + repeatStr("-", dashes));
            }
        }
        for (int i = 1; i <= n - 4; i++){
            System.out.println(repeatStr("-", dashes) + "**--**" + repeatStr("-", dashes));
        }
        dashes --;
        for (int i = 1; i <= n - 3; i++){
            System.out.println(repeatStr("-", dashes) + "**----**" + repeatStr("-", dashes));
        }
        dashes --;
        System.out.println(repeatStr("-", dashes) + repeatStr("*", 10) + repeatStr("-", dashes));
        int centerDashesh = 0;

        for (int i = 1; i <= n - 3; i ++){
            dashes--;
            centerDashesh = width - ((dashes * 2) + 4);
            System.out.println(repeatStr("-", dashes) + "**" + repeatStr("-", centerDashesh) + "**" + repeatStr("-", dashes));
        }
        System.out.println("***" + repeatStr("-", centerDashesh) + "***");

    }
    static String repeatStr (String text,int count){
        StringBuilder result = new StringBuilder();

        for (int i = 0; i < count; i++) {
            result.append(text);

        }
        return result.toString();
    }
}
