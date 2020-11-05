import java.util.Scanner;

public class A14_Test {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int a = Integer.parseInt(scanner.nextLine());
        int b = Integer.parseInt(scanner.nextLine());
        int h = Integer.parseInt(scanner.nextLine());

        int freeSpace = a * b * h;
        String command = scanner.nextLine();




            for (int i = 0; i < 9999; i++) {
                if (!command.equals("Done")) {
                    freeSpace -= Integer.parseInt(command);

                    if (freeSpace <= 0) {
                        System.out.printf("No more free space! You need %d Cubic meters more.", Math.abs(freeSpace));
                        break;
                    }
                    command = scanner.nextLine();
                } else {
                    System.out.printf("%d Cubic meters left.", freeSpace);
                    break;

                }
            }
    }
}
