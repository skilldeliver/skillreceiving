import java.util.Scanner;

public class Problem3 {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);
        String breed = Console.nextLine();
        String gender = Console.nextLine();

        int years = 0;
        switch (breed){
            case "British Shorthair":
                if (gender.equals("m")){
                    years = 13;
                }
                else {
                    years = 14;
                }
                break;
            case "Siamese":
                if (gender.equals("m")){
                years = 15;
            }
            else {
                years = 16;
            }
                break;
            case "Persian":
                if (gender.equals("m")){
                    years = 14;
                }
                else {
                    years = 15;
                }
                break;
            case "Ragdoll":
                if (gender.equals("m")){
                    years = 16;
                }
                else {
                    years = 17;
                }
                break;
            case "American Shorthair":
                if (gender.equals("m")){
                    years = 12;
                }
                else {
                    years = 13;
                }
                break;
            case "Siberian":
                if (gender.equals("m")){
                    years = 11;
                }
                else {
                    years = 12;
                }
                break;
             default:
                 System.out.println(breed + " is invalid cat!");
                 return;
        }
        int months = (years * 12) / 6;

        System.out.println(months + " cat months");
    }
}
