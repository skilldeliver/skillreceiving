import java.util.Scanner;

public class A4_FruitOrVegetable {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        String something = Console.nextLine();


        String [] fruits = {"banana", "apple", "kiwi", "cherry", "lemon", "grapes"};
        String [] vegetables = {"tomato", "cucumber", "pepper", "carrot"};
        boolean yFruit = false;
        boolean yVege = false;

        for (String str: fruits){
            if(str.trim().contains(something)) yFruit = true;

        }
        for (String str: vegetables){
            if(str.trim().contains(something)) yVege = true;

        }
        if (yFruit) System.out.println("fruit");
        else if (yVege) System.out.println("vegetable");
        else System.out.println("unknown");
    }
}