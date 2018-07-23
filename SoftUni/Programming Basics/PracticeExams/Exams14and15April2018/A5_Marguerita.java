import java.util.Scanner;

public class A5_Marguerita {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        int n = Integer.parseInt(Console.nextLine());
        int x = 8 * n + 2;
        int y = 7 * n + 3;

        int innerDots = 0;

        for (int i = 1; i <= n; i++){
            innerDots ++;
            if (i == 1){
                System.out.println(repeatStr("'", innerDots) + "&$" + repeatStr("'", x - innerDots - 2));
            }
            else {
                System.out.println(repeatStr("'", innerDots) + "\\" + repeatStr("'", x - innerDots - 1));
            }
        }
        int leftDots = -1;
        int rightDots = 0;

        for (int i = 1; i <= n; i++){

            if (i == 1){
                System.out.println(repeatStr("^*", x / 2 - 1) + "^'");
            }
            else {
                leftDots ++ ;
                rightDots++;
                System.out.println(repeatStr("'", leftDots) + "\\\\" + repeatStr(" ", n) + "\\" + repeatStr(" ", x - leftDots - rightDots - 5 - n) + "//" + repeatStr("'", rightDots));
            }
        }

        for (int i = 1; i <= n; i++){
            leftDots ++ ;
            rightDots++;
            if (i == 1){
                System.out.println(repeatStr("'", leftDots) + "\\" + repeatStr("~", x - 2 - rightDots - leftDots) + "/" + repeatStr("'", rightDots));

            }
            else if (i == n){
                System.out.println(repeatStr("'", leftDots) + "\\" + repeatStr("_", x - 2 - rightDots - leftDots) + "/" + repeatStr("'", rightDots));
            }
            else {
                System.out.println(repeatStr("'", leftDots) + "\\" + repeatStr(" ", x - 2 - rightDots - leftDots) + "/" + repeatStr("'", rightDots));
            }
        }
        for (int i = 1; i <= n * 2; i++){
            leftDots ++ ;
            rightDots++;
            if (i == 1){
                System.out.println(repeatStr("'", leftDots) + "\\" + repeatStr(".", x - 2 - rightDots - leftDots) + "/" + repeatStr("'", rightDots));

            }
            else if (i == n * 2){
                System.out.println(repeatStr("'", leftDots) + "\\" + repeatStr("_", x - 2 - rightDots - leftDots) + "/" + repeatStr("'", rightDots));
            }
            else {
                System.out.println(repeatStr("'", leftDots) + "\\" + repeatStr(" ", x - 2 - rightDots - leftDots) + "/" + repeatStr("'", rightDots));
            }
        }
        leftDots ++ ;
        rightDots++;
        for (int i = 1; i <= n * 2 + 1; i++){
            System.out.println(repeatStr("'", leftDots) + "|||" + repeatStr("'", rightDots));
        }
        System.out.println(repeatStr("_", x - 1) + "'");
        System.out.println("'" + repeatStr("-", x - 3) + "''");




    }
    static String repeatStr (String text,int count){
        StringBuilder result = new StringBuilder();

        for (int i = 0; i < count; i++) {
            result.append(text);

        }
        return result.toString();
    }
}
