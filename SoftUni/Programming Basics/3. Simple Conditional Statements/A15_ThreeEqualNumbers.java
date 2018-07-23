import java.util.Scanner;

public class A15_ThreeEqualNumbers {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);

        int num1 = Integer.parseInt(Console.nextLine());
        int num2 = Integer.parseInt(Console.nextLine());
        int num3 = Integer.parseInt(Console.nextLine());

        boolean state = false;

        if (num1 == num2){
            state = true;
        }
        if (num1 == num3 && state){
            System.out.println("yes");
        }
        else{
            System.out.println("no");
        }

    }
}
