import java.util.Scanner;

public class A7_SumSeconds {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);

        int first = Integer.parseInt(Console.nextLine());
        int second = Integer.parseInt(Console.nextLine());
        int third = Integer.parseInt(Console.nextLine());

        int sum = first + second + third;
        int mins = 0;

        if (sum >= 60 && sum <= 119){
            mins = 1;
            sum = sum - 60;
        }
        else if(sum >= 120 && sum <= 179) {
            mins = 2;
            sum = sum - 120;
        }

        if (sum < 10){
            System.out.println(mins + ":" + "0" + sum);
        }
        else{
            System.out.println(mins + ":" + sum);
        }

        }
    }

