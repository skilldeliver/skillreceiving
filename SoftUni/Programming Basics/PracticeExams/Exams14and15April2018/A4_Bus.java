import java.util.Scanner;

public class A4_Bus {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);

        int passengers = Integer.parseInt(Console.nextLine());
        int stop = Integer.parseInt(Console.nextLine());

        for (int i = 1; i <= stop; i++){
            int out = Integer.parseInt(Console.nextLine());
            int in = Integer.parseInt(Console.nextLine());


            if (i % 2 == 0){
                passengers -= 2;
            }
            else {
                passengers += 2;
            }
            passengers += in;
            passengers -= out;

        }
        System.out.println("The final number of passengers is : " + passengers);

    }
}
