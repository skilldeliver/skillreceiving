import java.util.Scanner;

public class A3_SolarSystem {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);

        String planet = Console.nextLine();
        int daysOnPlanet = Integer.parseInt(Console.nextLine());
        double dist = 0.0;
        boolean invalidDays = false;
        boolean invalidPlanet = false;

        switch ( planet){
            case "Mercury":
                if (daysOnPlanet > 7) invalidDays = true;
                else dist = 0.61;
                break;
            case "Venus":
                if (daysOnPlanet > 14) invalidDays = true;
                else dist = 0.28;
                break;
            case "Mars":
                if (daysOnPlanet > 20) invalidDays = true;
                else dist = 0.52;
                break;
            case "Jupiter":
                if (daysOnPlanet > 5) invalidDays = true;
                else dist = 4.2;
                break;
            case "Saturn":
                if (daysOnPlanet > 3) invalidDays = true;
                else dist = 8.52;
                break;
            case "Uranus":
                if (daysOnPlanet > 3) invalidDays = true;
                else dist = 18.21;
                break;
            case "Neptune":
                if (daysOnPlanet > 2) invalidDays = true;
                else dist = 29.09;
                break;
            default:
                invalidPlanet = true;
        }
        dist = dist * 2;
        double time = (dist * 226) + daysOnPlanet;
        if (invalidPlanet) System.out.println("Invalid planet name!");
        else if (invalidDays) System.out.println("Invalid number of days!");
        else{
            System.out.printf("Distance: %.2f", dist);
            System.out.println();
            System.out.printf("Total number of days: %.2f", time);
        }


    }
}
