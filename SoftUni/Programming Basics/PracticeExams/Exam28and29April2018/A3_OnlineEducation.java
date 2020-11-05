import java.util.Scanner;

public class A3_OnlineEducation {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);

        String formPre = Console.nextLine();
        int studentsPre = Integer.parseInt(Console.nextLine());
        String formAll = Console.nextLine();
        int studentsAll = Integer.parseInt(Console.nextLine());
        String formLate = Console.nextLine();
        int studentsLate = Integer.parseInt(Console.nextLine());

        int studentsOnline = 0;
        int studentsOnsite = 0;
        int total = 0;

        if (formPre.equals("onsite")) {
            studentsOnsite += studentsPre;
        }
        else if (formPre.equals("online")) {
            studentsOnline += studentsPre;
        }

        if (formAll.equals("onsite")) {
            studentsOnsite += studentsAll;
        }
        else if (formAll.equals("online")) {
            studentsOnline += studentsAll;
        }

        if (formLate.equals("onsite")){
            studentsOnsite += studentsLate;
        }
        else if (formLate.equals("online")){
            studentsOnline += studentsLate;
        }

        if (studentsOnsite > 600){
            studentsOnline += studentsOnsite - 600;
            studentsOnsite = 600;
        }
        System.out.println("Online students: " + studentsOnline);
        System.out.println("Onsite students: " + studentsOnsite);
        System.out.println("Total students: " + (studentsOnsite + studentsOnline));
    }
    }

