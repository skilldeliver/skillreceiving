import java.util.Scanner;

public class A9_VowelsSum {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        String s = Console.nextLine();
        int sum = 0;
        for (int i = 0; i <= s.length() - 1; i++){
            switch (s.charAt(i)){
                case 'a': sum += 1; break;
                case 'e': sum += 2; break;
                case 'i': sum += 3; break;
                case 'o': sum += 4; break;
                case 'u': sum += 5; break;
            }

        }
        System.out.println(sum);
    }
}
