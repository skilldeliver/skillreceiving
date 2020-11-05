import java.util.Scanner;

public class A6_SumAndProduct {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        int n = Console.nextInt();
        int multiply = 0;
        int sum = 0;
        for (int a = 1; a <= 9; a++){
            for (int b = 9; b >= a; b--){
                for (int c = 0; c <= 9; c++){
                    for (int d = 9; d >= c; d--){
                        multiply = a * b * c * d;
                        sum = a + b + c + d;
                        if (multiply == sum && n % 10 == 5){
                            System.out.print(a);
                            System.out.print(b);
                            System.out.print(c);
                            System.out.print(d);
                            return;
                        }
                        else if (multiply / sum == 3 && (n % 3 == 0)){
                            System.out.print(d);
                            System.out.print(c);
                            System.out.print(b);
                            System.out.print(a);
                            return;
                        }
                    }
                }
            }
        }
        System.out.println("Nothing found");


    }

}
