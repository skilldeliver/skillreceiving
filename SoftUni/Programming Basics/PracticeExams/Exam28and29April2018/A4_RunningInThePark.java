import java.util.Scanner;

public class A4_RunningInThePark {
    public static void main(String[] args) {
        Scanner Conzole = new Scanner(System.in);
        int n = Integer.parseInt(Conzole.nextLine());
        int mitutes = 0;
        int time = 0;
        double distance = 0;
        String type = " ";
        double total = 0;
        for (int i = 1; i <= n; i++){
            mitutes = Integer.parseInt(Conzole.nextLine());
            distance = Double.parseDouble(Conzole.nextLine());
            type = Conzole.nextLine();

            if (type.equals("m")){
                distance = distance / 1000;
            }
            time += mitutes;
            total += distance;

        }
        double temp =  (double) time / 20;
        double calories = temp * 400;
        System.out.printf("He ran %.2fkm for %s minutes and burned %.0f calories.", total, time, calories);

    }
}
