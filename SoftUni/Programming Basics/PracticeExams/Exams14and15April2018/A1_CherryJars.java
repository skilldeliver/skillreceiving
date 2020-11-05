

import java.util.Scanner;

public class A1_CherryJars {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);

        int jarsComp = Integer.parseInt(Console.nextLine());
        int jarsConf = Integer.parseInt(Console.nextLine());

        jarsComp ++;
        jarsConf ++;

        double cherryComp = (jarsComp * 0.300) * 1.05;
        double cherryConf = (jarsConf * 0.650) * 1.10;

        double total = cherryComp + cherryConf;
        double cherrys = total * 3.20;

        System.out.printf("%.2f", cherrys);


    }
}
