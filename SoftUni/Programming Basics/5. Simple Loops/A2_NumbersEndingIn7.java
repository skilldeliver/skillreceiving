import java.util.Scanner;

public class A2_NumbersEndingIn7 {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        for (int i = 1; i <= 1000; i++){
            if (i % 10 == 7){
                System.out.println(i);
            }
        }
    }
}
