import java.util.Scanner;

public class A3_FitnessCard {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        double sum = Double.parseDouble(Console.nextLine());
        String sex = Console.nextLine();
        int age = Integer.parseInt(Console.nextLine());
        String sport = Console.nextLine();

        double price = 0;
        if (sex.equals("m")){
            if (sport.equals("Gym")){
                price = 42;
            }
            else if (sport.equals("Boxing")){
                price = 41;
            }
            else if (sport.equals("Yoga")){
                price = 45;
            }
            else if (sport.equals("Zumba")){
                price = 34;
            }
            else if (sport.equals("Dances")){
                price = 51;
            }
            else if (sport.equals("Pilates")){
                price = 39;
            }
        }
        else if (sex.equals("f")){
            if (sport.equals("Gym")){
                price = 35;
            }
            else if (sport.equals("Boxing")){
                price = 37;
            }
            else if (sport.equals("Yoga")){
                price = 42;
            }
            else if (sport.equals("Zumba")){
                price = 31;
            }
            else if (sport.equals("Dances")){
                price = 53;
            }
            else if (sport.equals("Pilates")){
                price = 37;
            }
        }
        if (age <= 19){
            price = price * 0.8;
        }

        if (sum >= price){
            System.out.println("You purchased a 1 month pass for " + sport + ".");
        }
        else {
            System.out.printf("You don't have enough money! You need $%.2f more.", (price - sum));
        }

    }
}
