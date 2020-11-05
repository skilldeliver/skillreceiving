import java.util.Scanner;

public class A5_Skyscraper {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        int n = Integer.parseInt(Console.nextLine());
        int x = 2 * n + 1;
        int y = 8 * n - 8;

        int top = n - 2;
        int spaces = n;
        for (int i = 1; i <= top; i++){
            if (i == top){
                spaces --;
                System.out.println(repeatStr(" ", spaces) + "_|_");
            }
            else System.out.println(repeatStr(" ", spaces) + "|");
        }

        for (int i = 1; i <= top; i++){
            if (i == top) {
                spaces --;
                System.out.println(repeatStr(" ", spaces) + "_|-|_");
            }
            else System.out.println(repeatStr(" ", spaces) +"|-|" );
        }
        for (int i = 1; i <= top; i++){
            if (i == top){

                System.out.println(" " + repeatStr("_", (x - 6) / 2) + "|***|" + repeatStr("_", (x - 6) / 2));
            }
            else System.out.println(repeatStr(" ", spaces) + "|***|");
        }
        for (int i = 1; i <= y - (top * 4); i ++){
            if (i == y - (top * 4)){
                System.out.println("_" + repeatStr("|", top) + "---" + repeatStr("|", top) + "_");
            }
            else {
                System.out.println(" " + repeatStr("|", top) + "---" + repeatStr("|", top));
            }
        }
        for (int i = 1; i <= top; i++){
            System.out.println(repeatStr("|", x));
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
