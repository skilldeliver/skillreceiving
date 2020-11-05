import java.util.Scanner;

public class A12_SpeedInfo {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        double speed = Double.parseDouble(Console.nextLine());

        if (speed <= 10){
            System.out.println("slow");
        }
        else if(speed > 10 && speed <= 50){
            System.out.println("average");
        }
        else if(speed > 50 && speed <= 150){
            System.out.println("fast");
        }
        else if(speed > 150 && speed <= 1000){
            System.out.println("ultra fast");
        }
        else{
            System.out.println("extremely fast");
        }
    }
}
