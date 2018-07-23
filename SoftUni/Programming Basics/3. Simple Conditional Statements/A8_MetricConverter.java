import java.util.Scanner;

public class A8_MetricConverter {
    public static void main(String[] args) {
        Scanner Console = new Scanner(System.in);

        double value = Double.parseDouble(Console.nextLine());
        String from = Console.nextLine();
        String to = Console.nextLine();

        if (from.equals("mm")){
            value = value / 1000;
        }
        else if (from.equals("cm")){
            value = value / 100;
        }
        else if(from.equals("mi")){
            value = value / 0.000621371192;
        }
        else if(from.equals("in")){
            value = value / 39.3700787;
        }
        else if(from.equals("km")){
            value = value / 0.001;
        }
        else if(from.equals("ft")){
            value = value / 3.2808399;
        }
        else if(from.equals("yd")){
            value = value / 1.0936133;
        }

        if (to.equals("mm")){
            value = value * 1000;
        }
        else if (to.equals("cm")){
            value = value * 100;
        }
        else if(to.equals("mi")){
            value = value * 0.000621371192;
        }
        else if(to.equals("in")){
            value = value * 39.3700787;
        }
        else if(to.equals("km")){
            value = value * 0.001;
        }
        else if(to.equals("ft")){
            value = value * 3.2808399;
        }
        else if(to.equals("yd")){
            value = value * 1.0936133;
        }

        System.out.printf("%.8f %s", value, to);



    }
}
