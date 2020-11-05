import java.util.Scanner;

public class A10_Diamond {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        int n = Console.nextInt();
        int stars = 1;
        if (n % 2 == 0) stars = 2;
        float range = ((float)n - 2) / 2;
        System.out.println(repeatStr("-", (n - stars) / 2) + repeatStr("*", stars) +repeatStr("-", (n - stars) / 2));
        for (int i = 0; i < range; i++) {
            System.out.println(repeatStr("-", (n - stars - 2) / 2) + "*" + repeatStr("-", stars) + "*" + repeatStr("-", (n - stars - 2) / 2));
            stars += 2;
        }
        stars -= 2;
        for (int i = 0; i < n - range - 2 - 1; i++){
            stars -= 2;
            System.out.println(repeatStr("-", (n - stars - 2) / 2) + "*" + repeatStr("-", stars) + "*" + repeatStr("-", (n - stars - 2) / 2));
        }
        if (n > 2) System.out.println(repeatStr("-", (n - stars) / 2) + repeatStr("*", stars) +repeatStr("-", (n - stars) / 2));
    }
    static String repeatStr (String text,int count){
        StringBuilder result = new StringBuilder();

        for (int i = 0; i < count; i++) {
            result.append(text);

        }
        return result.toString();
    }
}
