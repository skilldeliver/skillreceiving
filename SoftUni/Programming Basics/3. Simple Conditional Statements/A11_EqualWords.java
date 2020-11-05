import java.util.Scanner;

public class A11_EqualWords {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);

        String word1 = Console.nextLine();
        String word2 = Console.nextLine();

        word1 = word1.toLowerCase();
        word2 = word2.toLowerCase();


        if (word1.equals(word2)){
            System.out.println("yes");
        }
        else{
            System.out.println("no");
        }
    }
}
