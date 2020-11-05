import java.util.Scanner;

public class A11_EnterEventNumber {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);

        int n = 0;
        do
        {
            try
            {
                System.out.print("Emter even number: ");
                n = Integer.parseInt(Console.nextLine());
                if (n % 2 == 0)
                {
                    break;
                }
                System.out.println("The number is not even");

            }
            catch (Exception e)
            {
                System.out.println("Invalid number!");
            }
        } while (true);

        System.out.print("Even number entered: " + n);
    }
}
