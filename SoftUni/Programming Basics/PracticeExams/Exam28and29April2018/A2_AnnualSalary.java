import java.util.Scanner;

public class A2_AnnualSalary {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);

        int exp = Integer.parseInt(Console.nextLine());
        String field = Console.nextLine();

        double salary  = 0.0;
        switch (field) {
            case "C# Developer":
                salary = 5400;
                break;
            case "Java Developer":
                salary = 5700;
                break;
            case "Front-End Web Developer":
                salary = 4100;
                break;
            case "UX / UI Designer":
                salary = 3100;
                break;
            case "Game Designer":
                salary = 3600;
                break;
        }
        if (exp <= 5){
            salary = salary - (salary * (65.8 / 100));
        }
        System.out.print("Total earned money: ");
        System.out.printf("%.2f", salary * 12);
        System.out.println(" BGN");

    }
}
