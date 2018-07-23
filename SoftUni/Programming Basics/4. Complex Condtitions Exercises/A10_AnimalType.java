import java.util.Scanner;

public class A10_AnimalType {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        String animal = Console.nextLine();

        switch (animal) {
            case "dog":
                System.out.println("mammal");
            case "snake":
                System.out.println("reptile");
            case "tortoise":
                System.out.println("reptile");
            case "crocodile":
                System.out.println("reptile");
            default:
                System.out.println("unknown");
        }
    }
}
