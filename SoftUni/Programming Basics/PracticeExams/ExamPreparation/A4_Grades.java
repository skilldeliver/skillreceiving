import java.util.Scanner;

public class A4_Grades {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        int students = Integer.parseInt(Console.nextLine());

        double grade = 0.0;

        double s1 = 0;
        double s2 = 0;
        double s3 = 0;
        double s4 = 0;
        double avg = 0.0;

        for (int i = 1; i <= students; i++){
            grade = Double.parseDouble(Console.nextLine());

            if (grade >= 5.00) s1++;
            else if(grade >= 4.00) s2++;
            else if(grade >= 3.00) s3 ++;
            else if(grade < 3.00) s4 ++;

            avg += grade;

        }
        double per = 100 / (double)students;

        System.out.printf("Top students: %.2f",s1 * per);
        System.out.print("%");
        System.out.println();
        System.out.printf("Between 4.00 and 4.99: %.2f",s2 * per);
        System.out.print("%");
        System.out.println();
        System.out.printf("Between 3.00 and 3.99: %.2f",s3 * per);
        System.out.print("%");
        System.out.println();
        System.out.printf("Fail: %.2f",s4 * per);
        System.out.print("%");
        System.out.println();
        System.out.printf("Average: %.2f", avg / students);
    }
}
