import java.util.Scanner;

public class A4_Moving {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        int widht = Integer.parseInt(Console.nextLine());
        int height = Integer.parseInt(Console.nextLine());
        int lenght = Integer.parseInt(Console.nextLine());

        int cubicM = widht * height * lenght;

        int boxes = 0;
        String command = "";
        while (true){
            command = Console.nextLine();
            if (command.equals("Done")){
                System.out.printf("%d Cubic meters left.", (cubicM - boxes));
                break;
            }
            else if (!command.equals("Done")){
                boxes += Integer.parseInt(command);
            }

            if (boxes > cubicM){
                System.out.printf("No more free space! You need %s Cubic meters more.", (boxes - cubicM));
                break;
            }
        }
    }
}
