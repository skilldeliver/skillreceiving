import java.util.Scanner;

public class A6_LettersCombinations {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);

        char a = Console.nextLine().charAt(0);
        char b = Console.nextLine().charAt(0);
        char c = Console.nextLine().charAt(0);

        int count = 0;

        for (char i = a; i <= b; i++){
            for (char j = a; j <= b; j++){
                for (char k = a; k <= b; k++){
                    if (i != c && j != c && k != c){
                        System.out.print(i + "" + j + "" + k + " ");
                        count += 1;
                    }
                }
            }
        }
        System.out.print(count);
    }
}
