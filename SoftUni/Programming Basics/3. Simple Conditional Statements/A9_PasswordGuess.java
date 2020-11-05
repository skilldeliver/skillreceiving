import java.util.Scanner;

public class A9_PasswordGuess {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);

        String pass = Console.nextLine();

        if (pass.equals("s3cr3t!P@ssw0rd")){
            System.out.println("Welcome");
        }
        else{
            System.out.println("Wrong password!");
        }
    }
}