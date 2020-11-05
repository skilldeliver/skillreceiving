import java.util.Scanner;

public class A5_PIN {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        int n = Integer.parseInt(Console.nextLine());

        int x = 6 * n + 10;
        int y = 2 * n + 2;

        System.out.println("/`" + repeatStr("P", n * 2) + repeatStr(" ", n) + "/`I" + repeatStr(" ", n) + "/`N" + repeatStr(" ", n * 2 + 1) + "N");

        int nSpaces = n * 2 + 1;
        int nSpaces2 = -1;

        for (int i = 1; i <= n - 1; i++){
            nSpaces --;
            nSpaces2 ++;
            System.out.println("| P" + repeatStr(" ", n * 2 - 2) + "P" + repeatStr(" ", n) + "| I" + repeatStr(" ", n) + "| N" + repeatStr(" ", nSpaces2) + "N" + repeatStr(" ", nSpaces) + "N");

        }
        nSpaces --;
        nSpaces2 ++;
        System.out.println("| P" + repeatStr("P", n * 2 - 2) + "P" + repeatStr(" ", n) + "| I" + repeatStr(" ", n) + "| N" + repeatStr(" ", nSpaces2) + "N" + repeatStr(" ", nSpaces) + "N");

        int pS = n / 2;

        for (int i =1; i <= n + 1; i++){
            nSpaces --;
            nSpaces2 ++;
            if ( i == n + 1) {
                System.out.println("\\_" + repeatStr("P", pS) + repeatStr(" ", n * 2 - pS) + repeatStr(" ", n) + "\\_I" + repeatStr(" ", n) + "\\_N" + repeatStr(" ", nSpaces2) + "N" + repeatStr(" ", nSpaces) + "N");
            }
            else {
                System.out.println("| " + repeatStr("P", pS) + repeatStr(" ", n * 2 - pS) + repeatStr(" ", n) + "| I" + repeatStr(" ", n) + "| N" + repeatStr(" ", nSpaces2) + "N" + repeatStr(" ", nSpaces) + "N");
            }
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
