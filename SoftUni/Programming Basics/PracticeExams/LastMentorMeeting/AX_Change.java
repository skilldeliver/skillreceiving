import java.util.Scanner;

public class AX_Change {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double change = Double.parseDouble(scanner.nextLine());
        int coinCount = 0;

        int levs = (int) change;

        int stotinki = (int) (change * 100) % 100;

        if (levs % 2 == 1) {
            coinCount += 1;
        }

        levs = levs / 2;
        coinCount += levs;

        if (stotinki / 50 == 1) {
            coinCount += 1;
            stotinki -= 50;
        }

        while (stotinki / 20 > 0) {
            coinCount++;
            stotinki -= 20;
        }

        if (stotinki / 10 == 1) {
            coinCount += 1;
            stotinki -= 10;
        }

        if (stotinki / 5 == 1) {
            coinCount += 1;
            stotinki -= 5;
        }

        while (stotinki / 2 > 0) {
            coinCount++;
            stotinki -= 2;
        }

        if (stotinki == 1) {
            coinCount += 1;
        }

        System.out.println(coinCount);
    }
}
