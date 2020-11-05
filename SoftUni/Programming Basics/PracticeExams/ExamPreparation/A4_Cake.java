import java.util.Scanner;

public class A4_Cake {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);

        int width = Integer.parseInt(Console.nextLine());
        int height = Integer.parseInt(Console.nextLine());

        int pieces = width * height;
        String command = "";
        while ( pieces >= 0){
            command = Console.nextLine();
            if (command.equals("STOP")){
                System.out.println(pieces + " pieces are left.");
                return;
            }
            pieces -= Integer.parseInt(command);
        }
        System.out.printf("No more cake left! You need %s pieces more.", Math.abs(pieces));


    }
}
