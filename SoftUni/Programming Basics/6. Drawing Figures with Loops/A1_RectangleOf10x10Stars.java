import java.util.Scanner;

public class A1_RectangleOf10x10Stars {
    public static void main(String[] args) {
        Scanner Conosle = new Scanner(System.in);
        for (int row = 1; row <= 10; row++) {
            for (int col = 1; col <= 10; col++){
                System.out.print("*");
            }
            System.out.println();
        }
    }
}
