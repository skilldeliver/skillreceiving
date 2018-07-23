import java.util.Scanner;

public class A2_WorkHours {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        int neededHours = Integer.parseInt(Console.nextLine());
        int employees = Integer.parseInt(Console.nextLine());
        int workingDays = Integer.parseInt(Console.nextLine());

        int allHours = employees * workingDays * 8;

        if (allHours >= neededHours){
            System.out.println((allHours - neededHours) + " hours left");
        }
        else{
            System.out.println((neededHours - allHours) + " overtime");
            System.out.println("Penalties: " + (neededHours - allHours) * workingDays);
        }

    }
}
